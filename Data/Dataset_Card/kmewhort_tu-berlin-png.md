---
license: cc-by-4.0
dataset_info:
  features:
  - name: image
    dtype: image
  - name: label
    dtype:
      class_label:
        names:
          '0': airplane
          '1': alarm clock
          '2': angel
          '3': ant
          '4': apple
          '5': arm
          '6': armchair
          '7': ashtray
          '8': axe
          '9': backpack
          '10': banana
          '11': barn
          '12': baseball bat
          '13': basket
          '14': bathtub
          '15': bear (animal)
          '16': bed
          '17': bee
          '18': beer-mug
          '19': bell
          '20': bench
          '21': bicycle
          '22': binoculars
          '23': blimp
          '24': book
          '25': bookshelf
          '26': boomerang
          '27': bottle opener
          '28': bowl
          '29': brain
          '30': bread
          '31': bridge
          '32': bulldozer
          '33': bus
          '34': bush
          '35': butterfly
          '36': cabinet
          '37': cactus
          '38': cake
          '39': calculator
          '40': camel
          '41': camera
          '42': candle
          '43': cannon
          '44': canoe
          '45': car (sedan)
          '46': carrot
          '47': castle
          '48': cat
          '49': cell phone
          '50': chair
          '51': chandelier
          '52': church
          '53': cigarette
          '54': cloud
          '55': comb
          '56': computer monitor
          '57': computer-mouse
          '58': couch
          '59': cow
          '60': crab
          '61': crane (machine)
          '62': crocodile
          '63': crown
          '64': cup
          '65': diamond
          '66': dog
          '67': dolphin
          '68': donut
          '69': door
          '70': door handle
          '71': dragon
          '72': duck
          '73': ear
          '74': elephant
          '75': envelope
          '76': eye
          '77': eyeglasses
          '78': face
          '79': fan
          '80': feather
          '81': fire hydrant
          '82': fish
          '83': flashlight
          '84': floor lamp
          '85': flower with stem
          '86': flying bird
          '87': flying saucer
          '88': foot
          '89': fork
          '90': frog
          '91': frying-pan
          '92': giraffe
          '93': grapes
          '94': grenade
          '95': guitar
          '96': hamburger
          '97': hammer
          '98': hand
          '99': harp
          '100': hat
          '101': head
          '102': head-phones
          '103': hedgehog
          '104': helicopter
          '105': helmet
          '106': horse
          '107': hot air balloon
          '108': hot-dog
          '109': hourglass
          '110': house
          '111': human-skeleton
          '112': ice-cream-cone
          '113': ipod
          '114': kangaroo
          '115': key
          '116': keyboard
          '117': knife
          '118': ladder
          '119': laptop
          '120': leaf
          '121': lightbulb
          '122': lighter
          '123': lion
          '124': lobster
          '125': loudspeaker
          '126': mailbox
          '127': megaphone
          '128': mermaid
          '129': microphone
          '130': microscope
          '131': monkey
          '132': moon
          '133': mosquito
          '134': motorbike
          '135': mouse (animal)
          '136': mouth
          '137': mug
          '138': mushroom
          '139': nose
          '140': octopus
          '141': owl
          '142': palm tree
          '143': panda
          '144': paper clip
          '145': parachute
          '146': parking meter
          '147': parrot
          '148': pear
          '149': pen
          '150': penguin
          '151': person sitting
          '152': person walking
          '153': piano
          '154': pickup truck
          '155': pig
          '156': pigeon
          '157': pineapple
          '158': pipe (for smoking)
          '159': pizza
          '160': potted plant
          '161': power outlet
          '162': present
          '163': pretzel
          '164': pumpkin
          '165': purse
          '166': rabbit
          '167': race car
          '168': radio
          '169': rainbow
          '170': revolver
          '171': rifle
          '172': rollerblades
          '173': rooster
          '174': sailboat
          '175': santa claus
          '176': satellite
          '177': satellite dish
          '178': saxophone
          '179': scissors
          '180': scorpion
          '181': screwdriver
          '182': sea turtle
          '183': seagull
          '184': shark
          '185': sheep
          '186': ship
          '187': shoe
          '188': shovel
          '189': skateboard
          '190': skull
          '191': skyscraper
          '192': snail
          '193': snake
          '194': snowboard
          '195': snowman
          '196': socks
          '197': space shuttle
          '198': speed-boat
          '199': spider
          '200': sponge bob
          '201': spoon
          '202': squirrel
          '203': standing bird
          '204': stapler
          '205': strawberry
          '206': streetlight
          '207': submarine
          '208': suitcase
          '209': sun
          '210': suv
          '211': swan
          '212': sword
          '213': syringe
          '214': t-shirt
          '215': table
          '216': tablelamp
          '217': teacup
          '218': teapot
          '219': teddy-bear
          '220': telephone
          '221': tennis-racket
          '222': tent
          '223': tiger
          '224': tire
          '225': toilet
          '226': tomato
          '227': tooth
          '228': toothbrush
          '229': tractor
          '230': traffic light
          '231': train
          '232': tree
          '233': trombone
          '234': trousers
          '235': truck
          '236': trumpet
          '237': tv
          '238': umbrella
          '239': van
          '240': vase
          '241': violin
          '242': walkie talkie
          '243': wheel
          '244': wheelbarrow
          '245': windmill
          '246': wine-bottle
          '247': wineglass
          '248': wrist-watch
          '249': zebra
  splits:
  - name: train
    num_bytes: 590878465.7704024
    num_examples: 19879
  - name: test
    num_bytes: 6007805.400597609
    num_examples: 201
  download_size: 590867064
  dataset_size: 596886271.171
---

# TU-Berlin Sketch Dataset

This is the full PNG dataset from [TU-Berlin](https://cybertron.cg.tu-berlin.de/eitz/projects/classifysketch/).

