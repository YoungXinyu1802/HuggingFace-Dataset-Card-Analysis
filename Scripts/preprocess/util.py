import tqdm
import re
import pandas as pd
import numpy as np
import json
import mistune
from mistune.plugins import plugin_table

"""
section type definition based on the HuggingFace dataset card template:
https://github.com/huggingface/datasets/blob/main/templates/README_guide.md
"""
section_type_dict = {
    'table of contents': ['table of contents'],
    'dataset description': ['dataset description', 'dataset summary', 'supported tasks and leaderboards', 'languages'],
    'dataset structure': ['dataset structure', 'data instances', 'data fields', 'data splits'],
    'dataset creation': ['dataset creation',
                         'curation rationale', 'source data', 'initial data collection', 'who are the source language producers',
                         'annotations', 'annotation process', 'who are the annotators',
                         'personal and sensitive information'],
    'considerations for using the data': ['considerations for using the data', 'social impact of dataset', 'discussion of biases', 'other known limitations'],
    'additional information': ['additional information', 'dataset curators', 'licensing information', 'citation information', 'contributions'],
}

"""
use mistune to parse the markdown content
version: mistune==2.0.4
more information about mistune: https://mistune.lepture.com/en/latest/ and https://github.com/lepture/mistune
"""
markdown = mistune.create_markdown(renderer=mistune.AstRenderer(), 
                    plugins=['table', 'url', 'footnotes', 'strikethrough'])

def extract_content(c_markdown, extract_heading = False, extract_raw = False, s=''):
    """
    extract the content of the markdown content
    param c_markdown: the markdown content
    param extract_heading: whether to extract the heading
    param extract_raw: whether to extract raw content or clean content (exclude code, table, link)
    param s: the string to store the content
    """
    if c_markdown['type'] == 'table' and extract_raw == False:
        return ''
    elif c_markdown['type'] == 'block_code' and extract_raw == False:
        return ''
    elif c_markdown['type'] == 'list_item' or c_markdown['type'] == 'list':
        s = '\n' + s
    elif c_markdown['type'] == 'heading' and not extract_heading:
        s = '\n'+'#' * c_markdown['level'] + ' '
    if 'text' in c_markdown:
        text = c_markdown['text']
        text = re.sub(r'<div[^>]*>([\s\S]*?)</div>', ' ', text)
        text = re.sub(r'<style[^>]*>([\s\S]*?)</style>', ' ', text)
        text = re.sub(r'<span[^>]*>([\s\S]*?)</span>', ' ', text)
        text = re.sub(r'<pre><code[^>]*>([\s\S]*?)</code></pre>', ' ', text)
        text = re.sub(r'<table[^>]*>([\s\S]*?)</table>', ' ', text)
        text = re.sub(r'<[^>]*>', ' ', text)
        
        # consider [more information needed] as empty
        text = re.sub(r'more information needed', '', text, flags=re.IGNORECASE).replace('[]', '')
        s += text
        if c_markdown['type'] == 'heading':
            s += '\n'
        return s
    elif 'children' in c_markdown and c_markdown['children'] != None:
        for i in c_markdown['children']:
            s += extract_content(i)
    return s

def section_content_extraction(index, c_markdown, section_level, raw):
    """
    extract the content of the section
    param index: the index of the markdown content to the whole markdown content
    param c_markdown: the whole markdown content
    param section_level: the level of the section
    param raw: whether to extract raw content or clean content (exclude code, table, link)
    """
    text = ''
    if raw == True:
        for i in range(index + 1, len(c_markdown)):
            if c_markdown[i]['type'] == 'heading':
                head_level = c_markdown[i]['level']
                head_content = extract_content(c_markdown[i], extract_heading=True)
                if classify_category(head_content, section_type_dict) != 'other' or head_level <= section_level:
                    break
            text += extract_content(c_markdown[i], extract_heading=False, extract_raw=True)
        text = text.strip()
    else:
        for i in range(index + 1, len(c_markdown)):
            if c_markdown[i]['type'] == 'heading':
                head_level = c_markdown[i]['level']
                head_content = extract_content(c_markdown[i], extract_heading=True)
                if classify_category(head_content, section_type_dict) != 'other' or head_level <= section_level:
                    break     
            if c_markdown[i]['type'] == 'block_code':
                continue
            if c_markdown[i]['type'] == 'table':
                continue
            if c_markdown[i]['type'] == 'link':
                continue        
            text += extract_content(c_markdown[i])
        text = re.sub(r'\n\s*\n', '\n', text).strip()
    return text

def count_word(str):
    # replace punctuations and special characters, then count words
    s = re.sub(r'[\s*[^A-Za-z0-9]+\s*]', '', str)
    return len(s.split())

def classify_category(title, category_dict):
    # classify the section into different categories
    title = title.lower()
    for category, category_list in category_dict.items():
        for item in category_list:
            if item in title:
                return category
    return 'other'

def clean_card(x):
    pattern = r'---(.*?)---'
    if x is None:
        return None
    else:
        return re.sub(pattern, '', x, count=1, flags=re.DOTALL)

def get_section_info(dataset_card):
    """
    get the section information of dataset card
    section information includes:
    1. "has_section": whether the dataset card has the section
    2. "section_length_proportion": the proportion of the section length in the whole dataset card
    3. "subsection_title": the title of subsections in the section
    4. "section_content": the plain text of the section
    5. "word_cnt": the word count of the section
    6. "not_empty": whether the section is empty
    """
    category_list = [k for k in section_type_dict.keys()] + ['other']
    category_pandas = {k:pd.DataFrame(columns=['has_section', 'section_length_proportion', 'subsection_title', 'section_content', 'word_cnt', 'not_empty'], \
                                      index=[i for i in dataset_card['dataset_name'].values.tolist()]) \
                        for k in category_list if k != 'table of contents'}
    for v in category_pandas.values():
        v.loc[:] = [0, 0, None, None, 0, 0]

    for i in tqdm.tqdm(range(len(dataset_card))):
        m = dataset_card.loc[i, 'dataset_name']
        c = clean_card(dataset_card.loc[i, 'dataset_card'])
        card_markdown = markdown(c)
        
        category_content_clean = {i : [] for i in category_list}
        category_heading = {i : [] for i in category_list}
        category_content_raw = {i : [] for i in category_list}
        head_category = set()
        
        total_percentage = 0
        for i in range(len(card_markdown)):
            if card_markdown[i]['type'] == 'heading':
                head_content = extract_content(card_markdown[i], extract_heading=True)
                # is license, skip
                section_level = card_markdown[i]['level']
                section_clean = section_content_extraction(i, card_markdown, section_level, raw=False)
                section_content = head_content + '\n' + section_clean
                section_raw = section_content_extraction(i, card_markdown, section_level, raw=True)                    
                category = classify_category(head_content, section_type_dict)

                if category != 'other' and count_word(section_raw)>0:
                    head_category.add(category)
                    if head_content.lower() != category:
                        category_heading[category].append(head_content)             
                    category_content_clean[category].append(section_content)
                    category_content_raw[category].append(section_raw)             
                    continue
                if section_level == 2 and category == 'other' and count_word(section_raw)>0:
                    head_category.add(category)              
                    category_content_clean[category].append(section_content)
                    category_content_raw[category].append(section_raw)
                    category_heading[category].append(head_content)
                    continue
        
        total_word_cnt = 0
        for i in head_category:
            if i == 'table of contents':
                continue
            plain_content = '\n'.join(category_content_clean[i])
            plain_content = re.sub(r'\n\s*\n', '\n', plain_content)            
            total_word_cnt += count_word(plain_content)

        for i in head_category:
            section_title = ';'.join(set(category_heading[i]))
            plain_content = '\n'.join(category_content_clean[i])
            # delete empty line of plain_content
            plain_content = re.sub(r'\n\s*\n', '\n', plain_content)
            raw_content = ' '.join(category_content_raw[i])  
            word_cnt = count_word(plain_content)
            if i == 'table of contents':
                coverage = 0
                continue
            else:
                if i != 'other':
                    coverage = word_cnt / total_word_cnt
                    total_percentage += coverage
                else:
                    coverage = 1 - total_percentage
            not_empty = 0 if count_word(raw_content) < 5 else 1
            category_pandas[i].loc[m] = [1, coverage, section_title, plain_content, word_cnt, not_empty]
    return category_pandas
