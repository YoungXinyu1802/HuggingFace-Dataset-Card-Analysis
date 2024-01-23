---
languages:
- en
task_categories:
- text-classification

---
# AutoNLP Dataset for project: devign_raw_test

## Dataset Descritpion

This dataset has been automatically processed by AutoNLP for project devign_raw_test.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "void ff_avg_h264_qpel16_mc32_msa ( uint8_t * dst , const uint8_t * src , ptrdiff_t stride ) { avc_lu[...]",
    "target": 0
  },
  {
    "text": "static void sd_cardchange ( void * opaque , bool load ) { SDState * sd = opaque ; qemu_set_irq ( sd [...]",
    "target": 0
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=2, names=['0', '1'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 21188 |
| valid        | 5298 |
