---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: label
    dtype:
      class_label:
        names:
          0: apple_pie
          1: baby_back_ribs
          2: baklava
          3: beef_carpaccio
          4: beef_tartare
          5: beet_salad
          6: beignets
          7: bibimbap
          8: boeuf_bourguignon
          9: bread_pudding
          10: breakfast_burrito
          11: bruschetta
          12: caesar_salad
          13: cannoli
          14: caprese_salad
          15: carrot_cake
          16: ceviche
          17: cheese_plate
          18: cheesecake
          19: chicken_curry
          20: chicken_quesadilla
          21: chicken_wings
          22: chocolate_cake
          23: chocolate_mousse
          24: churros
          25: clam_chowder
          26: club_sandwich
          27: crab_cakes
          28: creme_brulee
          29: croque_madame
          30: cup_cakes
          31: deviled_eggs
          32: donuts
          33: dumplings
          34: edamame
          35: eggs_benedict
          36: escargots
          37: falafel
          38: filet_mignon
          39: fish_and_chips
          40: foie_gras
          41: french_fries
          42: french_onion_soup
          43: french_toast
          44: fried_calamari
          45: fried_rice
          46: frozen_yogurt
          47: garlic_bread
          48: gnocchi
          49: greek_salad
          50: grilled_cheese_sandwich
          51: grilled_salmon
          52: guacamole
          53: gyoza
          54: hamburger
          55: hot_and_sour_soup
          56: hot_dog
          57: huevos_rancheros
          58: hummus
          59: ice_cream
          60: lasagna
          61: lobster_bisque
          62: lobster_roll_sandwich
          63: macaroni_and_cheese
          64: macarons
          65: miso_soup
          66: mussels
          67: nachos
          68: omelette
          69: onion_rings
          70: oysters
          71: pad_thai
          72: paella
          73: pancakes
          74: panna_cotta
          75: peking_duck
          76: pho
          77: pizza
          78: pork_chop
          79: poutine
          80: prime_rib
          81: pulled_pork_sandwich
          82: ramen
          83: ravioli
          84: red_velvet_cake
          85: risotto
          86: samosa
          87: sashimi
          88: scallops
          89: seaweed_salad
          90: shrimp_and_grits
          91: spaghetti_bolognese
          92: spaghetti_carbonara
          93: spring_rolls
          94: steak
          95: strawberry_shortcake
          96: sushi
          97: tacos
          98: takoyaki
          99: tiramisu
          100: tuna_tartare
          101: waffles
  splits:
  - name: test
    num_bytes: 1461368965.25
    num_examples: 25500
  - name: train
    num_bytes: 4285789478.25
    num_examples: 76500
  download_size: 5534173074
  dataset_size: 5747158443.5
---
# Dataset Card for "food102"

This is based on the [food101](https://huggingface.co/datasets/food101) dataset with an extra class generated with a Stable Diffusion model. 

A detailed walk-through is available on [YouTube](https://youtu.be/sIe0eo3fYQ4).
