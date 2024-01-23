---
license: mit
---

please use the following code to load data:

```python
# start data loading
!git lfs install
!git clone https://huggingface.co/datasets/nlp-guild/non-linear-classification

def load_dataset(path='dataset.npy'):
    """
    :return:
        f_and_xs: numpy array of size [sample_number, channels, sample_length]
        label_0, label_1, label_2: one-hot encodes of size [sample_number, number_bins]
    """

    r = np.load(path, allow_pickle=True).item()
    f_and_xs = r['f_and_xs']
    label_0 = r['l_0']
    label_1 = r['l_1']
    label_2 = r['l_2']
    return f_and_xs, label_0, label_1, label_2

f_and_xs, label_0, label_1, label_2 = load_dataset('/content/Nonlinear-System-Identification-with-Deep-Learning/dataset.npy')
# end data loading
```

