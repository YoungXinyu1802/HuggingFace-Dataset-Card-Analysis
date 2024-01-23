# PersianQA: a dataset for Persian Question Answering
Persian Question Answering (PersianQA) Dataset is a reading comprehension dataset on Persian Wikipedia. The crowd-sourced dataset consists of more than 9,000 entries. Each entry can be either an impossible to answer or a question with one or more answers spanning in the passage (the context) from which the questioner proposed the question. Much like the SQuAD2.0 dataset, the impossible or unanswerable questions can be utilized to create a system which "knows that it doesn't know the answer".
On top of that, the dataset has 900 test data available. Moreover, the first models trained on the dataset, Transformers, are available.
All the crowd workers of the dataset are native Persian speakers. Also, it worth mentioning that the contexts are collected from all categories of the Wiki (Historical, Religious, Geography, Science, etc.)
At the moment, each context has 7 pairs of questions with one answer and 3 impossible questions.

## Dataset 
###  Access/Download

- You can find the data under the [`dataset/`](https://github.com/sajjjadayobi/PersianQA/tree/main/dataset) directory. and use it like this
```python
import read_qa # is avalible at src/read_ds.py
train_ds = read_qa('pqa_train.json')
test_ds  = read_qa('pqa_test.json')
```
- Alternatively, you can also access the data through the HuggingFace🤗 datasets library
    - First, you need to install datasets using this command in your terminal:
```sh
pip install -q datasets
```
- Then import `persian_qa` dataset using `load_dataset`:
```python 
from datasets import load_dataset
dataset = load_dataset("SajjadAyoubi/persian_qa")
```

### Examples

| Title |         Context         |  Question  | Answer |
| :---: | :---------------------: | :--------: | :----: |
| خوب، بد، زشت | خوب، بد، زشت یک فیلم درژانر وسترن اسپاگتی حماسی است که توسط سرجو لئونه در سال ۱۹۶۶ در ایتالیا ساخته شد. زبانی که بازیگران این فیلم به آن تکلم می‌کنند مخلوطی از ایتالیایی و انگلیسی است. این فیلم سومین (و آخرین) فیلم از سه‌گانهٔ دلار (Dollars Trilogy) سرجو لئونه است. این فیلم در حال حاضر در فهرست ۲۵۰ فیلم برتر تاریخ سینما در وب‌گاه IMDB با امتیاز ۸٫۸ از ۱۰، رتبهٔ هشتم را به خود اختصاص داده‌است و به عنوان بهترین فیلم وسترن تاریخ سینمای جهان شناخته می‌شود. «خوب» (کلینت ایستوود، در فیلم، با نام «بلوندی») و «زشت» (ایلای والاک، در فیلم، با نام «توکو») با هم کار می‌کنند و با شگرد خاصی، به گول زدن کلانترهای مناطق مختلف و پول درآوردن از این راه می‌پردازند. «بد» (لی وان کلیف) آدمکشی حرفه‌ای است که به‌خاطر پول حاضر به انجام هر کاری است. «بد»، که در فیلم او را «اِنجل آیز (اِینجل آیز)» (به انگلیسی: Angel Eyes) صدا می‌کنند. به‌دنبال گنجی است که در طی جنگ‌های داخلی آمریکا، به دست سربازی به نام «جکسون»، که بعدها به «کارسون» نامش را تغییر داده، مخفی شده‌است. | در فیلم خوب بد زشت شخصیت ها کجایی صحبت می کنند؟ |     مخلوطی از ایتالیایی و انگلیسی   |
| قرارداد کرسنت | قرارداد کرسنت قراردادی برای فروش روزانه معادل ۵۰۰ میلیون فوت مکعب، گاز ترش میدان سلمان است، که در سال ۱۳۸۱ و در زمان وزارت بیژن نامدار زنگنه در دولت هفتم مابین شرکت کرسنت پترولیوم و شرکت ملی نفت ایران منعقد گردید. مذاکرات اولیه این قرارداد از سال ۱۹۹۷ آغاز شد و در نهایت، سال ۲۰۰۱ (۱۳۸۱) به امضای این تفاهم نامه مشترک انجامید. بر اساس مفاد این قرارداد، مقرر شده بود که از سال ۲۰۰۵ با احداث خط لوله در خلیج فارس، گاز فرآورده نشده میدان سلمان (مخزن مشترک با ابوظبی)، به میزان روزانه ۵۰۰ میلیون فوت مکعب (به قول برخی منابع ۶۰۰ میلیون فوت مکعب) به امارات صادر شود. این قرارداد مطابق قوانین داخلی ایران بسته شده‌ و تنها قرارداد نفتی ایران است که از طرف مقابل خود، تضمین گرفته‌است. اجرای این پروژه در سال ۱۳۸۴ با دلایل ارائه شده از سوی دیوان محاسبات ایران از جمله تغییر نیافتن بهای گاز صادراتی و ثابت ماندن آن در هفت سال اول اجرای قرارداد متوقف شد. این در حالی است که طبق تعریف حقوقی، دیوان محاسبات ایران، حق دخالت در قراردادها، پیش از آنکه قراردادها اجرایی و مالی شوند را ندارد.  | طرفین قرار داد کرسنت کیا بودن؟ | کرسنت پترولیوم و شرکت ملی نفت ایران |
| چهارشنبه‌سوری | چهارشنبه‌سوری یکی از جشن‌های ایرانی است که از غروب آخرین سه‌شنبه ی ماه اسفند، تا پس از نیمه‌شب تا آخرین چهارشنبه ی سال، برگزار می‌شود و برافروختن و پریدن از روی آتش مشخصهٔ اصلی آن است. این جشن، نخستین جشن از مجموعهٔ جشن‌ها و مناسبت‌های نوروزی است که با برافروختن آتش و برخی رفتارهای نمادین دیگر، به‌صورت جمعی در فضای باز برگزار می‌شود. به‌گفتهٔ ابراهیم پورداوود چهارشنبه‌سوری ریشه در گاهنبارِ هَمَسْپَتْمَدَم زرتشتیان و نیز جشن نزول فروهرها دارد که شش روز پیش از فرارسیدن نوروز برگزار می‌شد. احتمال دیگر این است که چهارشنبه‌سوری بازمانده و شکل تحول‌یافته‌ای از جشن سده باشد، که احتمال بعیدی است. علاوه برافروختن آتش، آیین‌های مختلف دیگری نیز در بخش‌های گوناگون ایران در زمان این جشن انجام می‌شوند. برای نمونه، در تبریز، مردم به چهارشنبه‌بازار می‌روند که با چراغ و شمع، به‌طرز زیبایی چراغانی شده‌است. هر خانواده یک آینه، دانه‌های اسفند، و یک کوزه برای سال نو خریداری می‌کنند. همه‌ساله شهروندانی از ایران در اثر انفجارهای ناخوشایند مربوط به این جشن، کشته یا مصدوم می‌شوند. | نام جشن اخرین شنبه ی سال چیست؟ | No Answer |

### Statistic

| Split | # of instances | # of unanswerables | avg. question length | avg. paragraph length | avg. answer length |
| :---: | :------------: | :----------------: | :------------------: | :-------------------: | :----------------: |
| Train |     9,000      |       2,700        |         8.39         |        224.58         |        9.61        |
| Test  |      938       |        280         |         8.02         |        220.18         |        5.99        |

The lengths are on the token level.

- for more about data and more example see [here](https://github.com/sajjjadayobi/PersianQA/tree/main/dataset#readme)

## Models
Currently, two models (baseline) on [HuggingFace🤗](https://huggingface.co/SajjadAyoubi/) model hub are using the dataset.

## Citation
Yet, we didn't publish any papers on the work.
However, if you did, please cite us properly with an entry like one below.
```bibtex
@misc{PersianQA,
  author          = {Ayoubi, Sajjad \& Davoodeh, Mohammad Yasin},
  title           = {PersianQA: a dataset for Persian Question Answering},
  year            = 2021,
  publisher       = {GitHub},
  journal         = {GitHub repository},
  howpublished    = {\url{https://github.com/SajjjadAyobi/PersianQA}},
}
```

