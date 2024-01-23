This dataset includes 2 images: one of the [IAM Handwriting Database](https://fki.tic.heia-fr.ch/databases/iam-handwriting-database) and one of the [SRIOE](https://rrc.cvc.uab.es/?ch=13) dataset.

They are used for testing OCR models that are part of the HuggingFace Transformers library. See [here](https://github.com/huggingface/transformers/search?q=fixtures_ocr) for details.

More specifically, they are used inside `test_modeling_vision_encoder_decoder_model.py`, for testing the TrOCR models.