Simple English Wikipedia it has only about 170k articles. We split these articles into paragraphs. wikipedia_filepath = 'simplewiki-2020-11-01.jsonl.gz'

if not os.path.exists(wikipedia_filepath): util.http_get('http://sbert.net/datasets/simplewiki-2020-11-01.jsonl.gz', wikipedia_filepath)

embedded into vectors using SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')