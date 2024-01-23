---
license: cc
---

Real estate ads in Russia are published on the websites avito.ru, realty.yandex.ru, cian.ru, sob.ru, youla.ru, n1.ru, moyareklama.ru. The ads-api.ru service allows you to upload real estate ads for a fee. The parser of the service works strangely and duplicates real estate ads in the database if the authors extended them after some time. Also in the Russian market there are a lot of outbids (bad realtors) who steal ads and publish them on their own behalf. Before publishing this dataset, my task was to select the original ad from a bunch of ads.
Russian real estate services allow ad authors to manually write data about an apartment or house. Therefore, it often happens that a user can publish an ad with errors or typos. Also, the user may not know, for example, the type of walls near his house.
The user also specifies the address of the object being sold. He may make a mistake and simply indicate the address, for example, "Moscow". Which street? Which house? We will never know.

# Dataset
The real estate market in Russia is of two types, in the dataset it is used as object type 0 - Secondary real estate market; 2 - New building.
I found it necessary to determine the geolocation for each ad address and add the coordinates to this dataset. Also there is a number of the region of Russia. For example, the number of the Chuvash region is 21. Additionally, there is a house number that is synchronized through the federal public database of the Federal Tax Service "FIAS". Since the data is obtained through a paid third party service, I cannot publish the results, however, I can anonymize them and publish parameters such as Street ID and House ID.
Basically, all houses are built from blocks such as brick, wood, panel and others. I marked them with numbers: building type - 0 - Don't know. 1 - Other. 2 - panel. 3 - Monolithic. 4 - Brick. 5 - blocky. 6- Wooden

The number of rooms can also be as 1, 2 or more. However, there is a type of apartment that is called a studio apartment. I've labeled them "-1".

# Ideas
I hope that the publication of this dataset will improve developments in the field of global real estate.
You can create apartment price forecasts.
You can analyze real estate markets.
You can understand that there is a need to publish free real estate datasets.
And much more

# Others

The license for this dataset is public, you can use it in your scientific research, design work and other works. The only condition is the publication of a link to this dataset.
You can send suggestions (or complaints) on the dataset by mail daniilakk@gmail.com

You can find more information about the data on the website https://dom.realtycloud.ru/
