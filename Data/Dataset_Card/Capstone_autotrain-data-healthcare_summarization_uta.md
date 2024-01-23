---
language:
- en
task_categories:
- conditional-text-generation

---
# AutoTrain Dataset for project: healthcare_summarization_uta

## Dataset Description

This dataset has been automatically processed by AutoTrain for project healthcare_summarization_uta.

### Languages

The BCP-47 code for the dataset's language is en.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "We get people to do things that are good for them. And you. | Make the world a healthier place, one person at a time. | Healthcare today is nothing short of amazing. Yet all of it only works when people connect with it. And too often, they dont. Healthcare can be impersonal. Confusing. All elbows. The record scratch at lifes party. Were here to help connect healthcare with the people who need it. Which is everyone. How? By listening. Collaborating. And inspiring. Were pioneering a better way forward. Were making healthcare more human. | In 2020, Revel + NovuHealth joined forces to create Icario because we knew we could do better togethercreating value by uniting pioneering technology, data science, and behavioral insights to make the world a healthier place, one person at a time. | There is an island in the Aegean Sea where people live extremely long lives. Theyre happy, too. Families are close. They eat well. They exercise. And they stay connected with each other, and not just by smartphone. This got us thinking. What if we apply what we learn from the Blue Zone island of Ikaria (our namesake), add pioneering technology and exabytes of data, and help healthcare connect better with everyone? Well have a lot more healthy, happy people, and thats a pretty good thing. | As an organization, were a collaborative team of pioneers, inventors, and systems thinkers. We speak truth, are driven by data, and sweat the details. Were a friendly and easygoing group, but we work hard because we are mission-driven, we know a better way, and were here to make it happen. | The Icario name and brand represent a successful, growing business that deeply understands people and is focused on making healthcare more human through personalized communication. | ",
    "target": "We're putting people first in healthcare. In order to create value by fusing cutting-edge technology, data science, and behavioral insights to improve the world's health one person at a time, Revel and NovuHealth partnered to become Icario in 2020. The Icario name and brand speak for a prosperous, expanding company that has a keen understanding of people and is committed to enhancing healthcare through individualized communication."
  },
  {
    "text": "Medicat is the industry leader in College Health Software and serves more college and university campuses than all other college health software companies combined. From the largest universities to the smallest colleges, Medicat specializes in workflow efficiency and has been improving outcomes for campus health centers since 1993. | Over 500 clients, covering 5+ million students across 48 states and three countries, use Medicats total EHR solution to deliver higher quality care more efficiently with the industrys most secure software platform offerings. Medicat offers private cloud hosting with unmatched security and has continued to improve its offering over 29 years, leading the industry in response to client needs. | The industry leader in College Health EHR | Medicat has the leading market share in the college health EHR industry, serving more college and university campuses than all other college health EHR companies combined. From the largest universities to the smallest colleges, Medicat specializes in workflow efficiency and a seamless transition from other EHRs or less efficient manual, paper-based systems to reap the benefits of going digital. | Two kinds of clients are switching from other systems to Medicat: Colleges who are with small niche EHR companies that dont have the capabilities or the security infrastructure; and those who are with larger companies that dont offer Medicats specialized expertise and support in college health. Wherever you fit in, Medicat can help; lets talk! | Medicat is the #1 health management system supporting college health. We support healthcare providers at over 500 universities, from the largest universities to the smallest colleges, covering more than 5 million students. Our software and services are co-created with healthcare professionals to address the unique workflow challenges of medical and mental health practitioners | 303 Perimeter Center North, Suite 450Atlanta, GA 30346 | Toll-Free: (866) 633-4053Phone: (404) 252-2295Fax: (404) 252-2298 |  2022 MEDICAT. | Notifications",
    "target": "Medicat is the industry leader in College Health Software and serves more college and university campuses than all other college health software companies combined. From the largest universities to the smallest colleges, Medicat specializes in workflow efficiency and has been improving outcomes for campus health centers since 1993. Over 500 clients, covering 5+ million students across 48 states and three countries, use Medicats total EHR solution to deliver higher quality care more efficiently with the industrys most secure software platform offerings. Medicat offers private cloud hosting with unmatched security and has continued to improve its offering over 29 years, leading the industry in response to client needs. The industry leader in College Health EHR Medicat has the leading market share in the college health EHR industry, serving more college and university campuses than all other college health EHR companies combined."
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "Value(dtype='string', id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 63 |
| valid        | 16 |
