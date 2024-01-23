---
license: cc-by-sa-4.0
---

## Message Content Rephrasing Dataset
Introduced by Einolghozati et al. in Sound Natural: Content Rephrasing in Dialog Systems https://aclanthology.org/2020.emnlp-main.414/

We introduce a new task of rephrasing for amore natural virtual assistant. Currently, vir-tual assistants work in the paradigm of intent-slot tagging and the slot values are directlypassed as-is to the execution engine. However,this setup fails in some scenarios such as mes-saging when the query given by the user needsto be changed before repeating it or sending itto another user. For example, for queries like‘ask my wife if she can pick up the kids’ or ‘re-mind me to take my pills’, we need to rephrasethe content to ‘can you pick up the kids’ and‘take your pills’. In this paper, we study theproblem of rephrasing with messaging as ause case and release a dataset of 3000 pairs oforiginal query and rephrased query. We showthat BART, a pre-trained transformers-basedmasked language model with auto-regressivedecoding, is a strong baseline for the task, andshow improvements by adding a copy-pointerand copy loss to it. We analyze different trade-offs of BART-based and LSTM-based seq2seqmodels, and propose a distilled LSTM-basedseq2seq as the best practical model.
