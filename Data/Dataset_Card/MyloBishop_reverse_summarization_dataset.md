# Overview

Converted from these datasets:
> https://huggingface.co/datasets/jordiclive/scored_summarization_datasets -> labeled "data" \
> https://huggingface.co/datasets/jordiclive/wikipedia-summary-dataset -> labeled "wiki" \

wiki dataset is split between "description" (cleaner, more popular articles) and "no description" (less clean, less popular)

Consist of parquet files with cols: `instruction, response, source`

full_to_summary (fts) consist of the following prompts infront of the instruction \
the full text is the instruction in these files
```
  full_to_summary = [
      "Summarize the following text: {}",
      "Make a summary of the following text: {}",
      "Provide a summary of the following text: {}",
      "Change the following text into a summary: {}",
      "Create a summary of the following text: {}",
      "Give a brief overview of the following text: {}",
      "Condense the following text into a summary: {}",
      "Provide a condensed version of the following text: {}",
      "Make a brief summary of the following text: {}",
      "Create a condensed overview of the following text: {}",
  ]
```

summary_to_full (stf) consist of the following prompts infront of the instruction \
the summary is the instruction in these files
```
  summary_to_full = [
      "Write the original text for the following summary: {}",
      "Write the full text for the following summary: {}",
      "Provide the inputted source that provided the following summary: {}",
      "Revert the following summary back into the original text: {}",
      "Write a text that could've provided the following summary: {}",
      "Write the original text that generated the following summary: {}",
      "Provide the full text for the following summary: {}",
      "Create the inputted source that provided the following summary: {}",
      "Write the original source that provided the following summary: {}",
      "Convert the following summary back into the original text: {}",
      "Provide a text that could have been the input for the following summary: {}",
  ]
```