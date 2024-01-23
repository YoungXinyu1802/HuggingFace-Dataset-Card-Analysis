---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: label
    dtype:
      class_label:
        names:
          '0': 001.Black_footed_Albatross
          '1': 002.Laysan_Albatross
          '2': 003.Sooty_Albatross
          '3': 004.Groove_billed_Ani
          '4': 005.Crested_Auklet
          '5': 006.Least_Auklet
          '6': 007.Parakeet_Auklet
          '7': 008.Rhinoceros_Auklet
          '8': 009.Brewer_Blackbird
          '9': 010.Red_winged_Blackbird
          '10': 011.Rusty_Blackbird
          '11': 012.Yellow_headed_Blackbird
          '12': 013.Bobolink
          '13': 014.Indigo_Bunting
          '14': 015.Lazuli_Bunting
          '15': 016.Painted_Bunting
          '16': 017.Cardinal
          '17': 018.Spotted_Catbird
          '18': 019.Gray_Catbird
          '19': 020.Yellow_breasted_Chat
          '20': 021.Eastern_Towhee
          '21': 022.Chuck_will_Widow
          '22': 023.Brandt_Cormorant
          '23': 024.Red_faced_Cormorant
          '24': 025.Pelagic_Cormorant
          '25': 026.Bronzed_Cowbird
          '26': 027.Shiny_Cowbird
          '27': 028.Brown_Creeper
          '28': 029.American_Crow
          '29': 030.Fish_Crow
          '30': 031.Black_billed_Cuckoo
          '31': 032.Mangrove_Cuckoo
          '32': 033.Yellow_billed_Cuckoo
          '33': 034.Gray_crowned_Rosy_Finch
          '34': 035.Purple_Finch
          '35': 036.Northern_Flicker
          '36': 037.Acadian_Flycatcher
          '37': 038.Great_Crested_Flycatcher
          '38': 039.Least_Flycatcher
          '39': 040.Olive_sided_Flycatcher
          '40': 041.Scissor_tailed_Flycatcher
          '41': 042.Vermilion_Flycatcher
          '42': 043.Yellow_bellied_Flycatcher
          '43': 044.Frigatebird
          '44': 045.Northern_Fulmar
          '45': 046.Gadwall
          '46': 047.American_Goldfinch
          '47': 048.European_Goldfinch
          '48': 049.Boat_tailed_Grackle
          '49': 050.Eared_Grebe
          '50': 051.Horned_Grebe
          '51': 052.Pied_billed_Grebe
          '52': 053.Western_Grebe
          '53': 054.Blue_Grosbeak
          '54': 055.Evening_Grosbeak
          '55': 056.Pine_Grosbeak
          '56': 057.Rose_breasted_Grosbeak
          '57': 058.Pigeon_Guillemot
          '58': 059.California_Gull
          '59': 060.Glaucous_winged_Gull
          '60': 061.Heermann_Gull
          '61': 062.Herring_Gull
          '62': 063.Ivory_Gull
          '63': 064.Ring_billed_Gull
          '64': 065.Slaty_backed_Gull
          '65': 066.Western_Gull
          '66': 067.Anna_Hummingbird
          '67': 068.Ruby_throated_Hummingbird
          '68': 069.Rufous_Hummingbird
          '69': 070.Green_Violetear
          '70': 071.Long_tailed_Jaeger
          '71': 072.Pomarine_Jaeger
          '72': 073.Blue_Jay
          '73': 074.Florida_Jay
          '74': 075.Green_Jay
          '75': 076.Dark_eyed_Junco
          '76': 077.Tropical_Kingbird
          '77': 078.Gray_Kingbird
          '78': 079.Belted_Kingfisher
          '79': 080.Green_Kingfisher
          '80': 081.Pied_Kingfisher
          '81': 082.Ringed_Kingfisher
          '82': 083.White_breasted_Kingfisher
          '83': 084.Red_legged_Kittiwake
          '84': 085.Horned_Lark
          '85': 086.Pacific_Loon
          '86': 087.Mallard
          '87': 088.Western_Meadowlark
          '88': 089.Hooded_Merganser
          '89': 090.Red_breasted_Merganser
          '90': 091.Mockingbird
          '91': 092.Nighthawk
          '92': 093.Clark_Nutcracker
          '93': 094.White_breasted_Nuthatch
          '94': 095.Baltimore_Oriole
          '95': 096.Hooded_Oriole
          '96': 097.Orchard_Oriole
          '97': 098.Scott_Oriole
          '98': 099.Ovenbird
          '99': 100.Brown_Pelican
          '100': 101.White_Pelican
          '101': 102.Western_Wood_Pewee
          '102': 103.Sayornis
          '103': 104.American_Pipit
          '104': 105.Whip_poor_Will
          '105': 106.Horned_Puffin
          '106': 107.Common_Raven
          '107': 108.White_necked_Raven
          '108': 109.American_Redstart
          '109': 110.Geococcyx
          '110': 111.Loggerhead_Shrike
          '111': 112.Great_Grey_Shrike
          '112': 113.Baird_Sparrow
          '113': 114.Black_throated_Sparrow
          '114': 115.Brewer_Sparrow
          '115': 116.Chipping_Sparrow
          '116': 117.Clay_colored_Sparrow
          '117': 118.House_Sparrow
          '118': 119.Field_Sparrow
          '119': 120.Fox_Sparrow
          '120': 121.Grasshopper_Sparrow
          '121': 122.Harris_Sparrow
          '122': 123.Henslow_Sparrow
          '123': 124.Le_Conte_Sparrow
          '124': 125.Lincoln_Sparrow
          '125': 126.Nelson_Sharp_tailed_Sparrow
          '126': 127.Savannah_Sparrow
          '127': 128.Seaside_Sparrow
          '128': 129.Song_Sparrow
          '129': 130.Tree_Sparrow
          '130': 131.Vesper_Sparrow
          '131': 132.White_crowned_Sparrow
          '132': 133.White_throated_Sparrow
          '133': 134.Cape_Glossy_Starling
          '134': 135.Bank_Swallow
          '135': 136.Barn_Swallow
          '136': 137.Cliff_Swallow
          '137': 138.Tree_Swallow
          '138': 139.Scarlet_Tanager
          '139': 140.Summer_Tanager
          '140': 141.Artic_Tern
          '141': 142.Black_Tern
          '142': 143.Caspian_Tern
          '143': 144.Common_Tern
          '144': 145.Elegant_Tern
          '145': 146.Forsters_Tern
          '146': 147.Least_Tern
          '147': 148.Green_tailed_Towhee
          '148': 149.Brown_Thrasher
          '149': 150.Sage_Thrasher
          '150': 151.Black_capped_Vireo
          '151': 152.Blue_headed_Vireo
          '152': 153.Philadelphia_Vireo
          '153': 154.Red_eyed_Vireo
          '154': 155.Warbling_Vireo
          '155': 156.White_eyed_Vireo
          '156': 157.Yellow_throated_Vireo
          '157': 158.Bay_breasted_Warbler
          '158': 159.Black_and_white_Warbler
          '159': 160.Black_throated_Blue_Warbler
          '160': 161.Blue_winged_Warbler
          '161': 162.Canada_Warbler
          '162': 163.Cape_May_Warbler
          '163': 164.Cerulean_Warbler
          '164': 165.Chestnut_sided_Warbler
          '165': 166.Golden_winged_Warbler
          '166': 167.Hooded_Warbler
          '167': 168.Kentucky_Warbler
          '168': 169.Magnolia_Warbler
          '169': 170.Mourning_Warbler
          '170': 171.Myrtle_Warbler
          '171': 172.Nashville_Warbler
          '172': 173.Orange_crowned_Warbler
          '173': 174.Palm_Warbler
          '174': 175.Pine_Warbler
          '175': 176.Prairie_Warbler
          '176': 177.Prothonotary_Warbler
          '177': 178.Swainson_Warbler
          '178': 179.Tennessee_Warbler
          '179': 180.Wilson_Warbler
          '180': 181.Worm_eating_Warbler
          '181': 182.Yellow_Warbler
          '182': 183.Northern_Waterthrush
          '183': 184.Louisiana_Waterthrush
          '184': 185.Bohemian_Waxwing
          '185': 186.Cedar_Waxwing
          '186': 187.American_Three_toed_Woodpecker
          '187': 188.Pileated_Woodpecker
          '188': 189.Red_bellied_Woodpecker
          '189': 190.Red_cockaded_Woodpecker
          '190': 191.Red_headed_Woodpecker
          '191': 192.Downy_Woodpecker
          '192': 193.Bewick_Wren
          '193': 194.Cactus_Wren
          '194': 195.Carolina_Wren
          '195': 196.House_Wren
          '196': 197.Marsh_Wren
          '197': 198.Rock_Wren
          '198': 199.Winter_Wren
          '199': 200.Common_Yellowthroat
  splits:
  - name: test
    num_bytes: 5095337196.0
    num_examples: 6000
  download_size: 5009478428
  dataset_size: 5095337196.0
---
# Dataset Card for "CUB-SD"

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)


The CUB dataset re-created using Stable Diffusion 2.0


<table>
  <tr>
    <td><img alt="Showcase" src="https://huggingface.co/datasets/taesiri/CUB-SD/resolve/main/sample_images/4__Blue%20Jay.png"/></td>
    <td><img alt="Showcase" src="https://huggingface.co/datasets/taesiri/CUB-SD/resolve/main/sample_images/11__Kentucky%20Warbler.png"/></td>
  </tr>
  <tr>
    <td><img alt="Showcase" src="https://huggingface.co/datasets/taesiri/CUB-SD/resolve/main/sample_images/9__House%20Sparrow.png"/></td>
    <td><img alt="Showcase" src="https://huggingface.co/datasets/taesiri/CUB-SD/resolve/main/sample_images/23__Scarlet%20Tanager.png"/></td>
  </tr>
</table>
