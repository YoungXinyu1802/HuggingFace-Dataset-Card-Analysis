---
dataset_info:
  features:
  - name: url
    dtype: string
  - name: repository_url
    dtype: string
  - name: labels_url
    dtype: string
  - name: comments_url
    dtype: string
  - name: events_url
    dtype: string
  - name: html_url
    dtype: string
  - name: id
    dtype: int64
  - name: node_id
    dtype: string
  - name: number
    dtype: int64
  - name: title
    dtype: string
  - name: user
    struct:
    - name: login
      dtype: string
    - name: id
      dtype: int64
    - name: node_id
      dtype: string
    - name: avatar_url
      dtype: string
    - name: gravatar_id
      dtype: string
    - name: url
      dtype: string
    - name: html_url
      dtype: string
    - name: followers_url
      dtype: string
    - name: following_url
      dtype: string
    - name: gists_url
      dtype: string
    - name: starred_url
      dtype: string
    - name: subscriptions_url
      dtype: string
    - name: organizations_url
      dtype: string
    - name: repos_url
      dtype: string
    - name: events_url
      dtype: string
    - name: received_events_url
      dtype: string
    - name: type
      dtype: string
    - name: site_admin
      dtype: bool
  - name: labels
    list:
    - name: id
      dtype: int64
    - name: node_id
      dtype: string
    - name: url
      dtype: string
    - name: name
      dtype: string
    - name: color
      dtype: string
    - name: default
      dtype: bool
    - name: description
      dtype: string
  - name: state
    dtype: string
  - name: locked
    dtype: bool
  - name: assignee
    struct:
    - name: login
      dtype: string
    - name: id
      dtype: int64
    - name: node_id
      dtype: string
    - name: avatar_url
      dtype: string
    - name: gravatar_id
      dtype: string
    - name: url
      dtype: string
    - name: html_url
      dtype: string
    - name: followers_url
      dtype: string
    - name: following_url
      dtype: string
    - name: gists_url
      dtype: string
    - name: starred_url
      dtype: string
    - name: subscriptions_url
      dtype: string
    - name: organizations_url
      dtype: string
    - name: repos_url
      dtype: string
    - name: events_url
      dtype: string
    - name: received_events_url
      dtype: string
    - name: type
      dtype: string
    - name: site_admin
      dtype: bool
  - name: assignees
    list:
    - name: login
      dtype: string
    - name: id
      dtype: int64
    - name: node_id
      dtype: string
    - name: avatar_url
      dtype: string
    - name: gravatar_id
      dtype: string
    - name: url
      dtype: string
    - name: html_url
      dtype: string
    - name: followers_url
      dtype: string
    - name: following_url
      dtype: string
    - name: gists_url
      dtype: string
    - name: starred_url
      dtype: string
    - name: subscriptions_url
      dtype: string
    - name: organizations_url
      dtype: string
    - name: repos_url
      dtype: string
    - name: events_url
      dtype: string
    - name: received_events_url
      dtype: string
    - name: type
      dtype: string
    - name: site_admin
      dtype: bool
  - name: milestone
    dtype: 'null'
  - name: comments
    sequence: string
  - name: created_at
    dtype: timestamp[s]
  - name: updated_at
    dtype: timestamp[s]
  - name: closed_at
    dtype: timestamp[s]
  - name: author_association
    dtype: string
  - name: active_lock_reason
    dtype: 'null'
  - name: draft
    dtype: bool
  - name: pull_request
    struct:
    - name: url
      dtype: string
    - name: html_url
      dtype: string
    - name: diff_url
      dtype: string
    - name: patch_url
      dtype: string
    - name: merged_at
      dtype: timestamp[s]
  - name: body
    dtype: string
  - name: reactions
    struct:
    - name: url
      dtype: string
    - name: total_count
      dtype: int64
    - name: '+1'
      dtype: int64
    - name: '-1'
      dtype: int64
    - name: laugh
      dtype: int64
    - name: hooray
      dtype: int64
    - name: confused
      dtype: int64
    - name: heart
      dtype: int64
    - name: rocket
      dtype: int64
    - name: eyes
      dtype: int64
  - name: timeline_url
    dtype: string
  - name: performed_via_github_app
    dtype: 'null'
  - name: state_reason
    dtype: string
  - name: is_pull_request
    dtype: bool
  splits:
  - name: train
    num_bytes: 386968
    num_examples: 100
  download_size: 169642
  dataset_size: 386968
---
# Dataset Card for "github-issues"
annotations_creators:
- expert-generated
language:
- en
language_creators:
- found
license:
- cc-by-nc-sa-3.0
multilinguality:
- monolingual
paperswithcode_id: null
pretty_name: Hugging Face GitHub Issues
size_categories:
- 1K<n<10K
source_datasets:
- original
tags:
- bio
- paper
task_categories:
- text-classification
- table-to-text
task_ids:
- multi-class-classification
- sentiment-classification
[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)