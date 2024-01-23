---
license: mit
---
This dataset contains information about the 9761 witches from the Crypto Coven NFT project (https://www.cryptocoven.xyz/) collected using OpenSea API. 

The folder 'witch_images' includes the images of each witch in three different sizes.

I briefly describe the data in the `witches.csv` below:

- `id`: the id of the witch
- `num_sales`: number of sales in the past (till 4/21/2022 the day I collected the data)
- `name`: the name of the witch
- `description`: the description of the witch
- `external_link`: the link to the official page for the witch
- `permalink`: the OpenSea link for the witch
- `token_metadata`: the metadata JSON file about the witch
- `token_id`: the token_id of the NFT
- `owner.user.username`: the user name of the current owner
- `owner.address`: the wallet address of the current owner
- `last_sale.total_price`: the price of the last sale in gwei. Note that the unit here is gwei (giga and wei) and 1 ether = 1 billion gwei (18 zeros)
- `last_sale.payment_token.usd_price`: the USD price of 1 ether (ETH) for the last sale
- `last_sale.transaction.timestamp`: the timestamp of the last sale
- `properties`: there are 32 properties of each witch covering the different design elements of each witch, such as Skin Tone,  Eyebrows, Body Shape, etc. 


`witches_full.csv` is the full data provided by the OpenSea API, such as https://api.opensea.io/api/v1/asset/0x5180db8f5c931aae63c74266b211f580155ecac8/50. I just simply flattened the JSON returned by the API.