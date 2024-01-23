---
license: apache-2.0
---

## OIG-riverbed-filtered-small

A small filtered version of https://huggingface.co/datasets/laion/OIG, used for experimenting with filtering, clustering and visualizing the data in the OIG dataset.
```
'unatural_instructions': 33110,
'ul2_plus_oscar_en_00300': 32439,
'infil_dbpedia': 81913,
'synth_qa': 11056,
'rallio': 192978,
'unifiedskg': 34692,
'soda_dialog': 40233,
'merged_code_xp3': 50000,
'laion_image_prompts': 10572,
'oscar_en_00000': 27713,
'prosocial': 14543,
'xp3_sample': 38833,
'mathqa': 10674,
'anthrop_helpful': 4816,
'flanv2_cot_qed_train': 2370,
'dahoas': 27534,
'flanv2_cot_esnli_train': 11325,
'flanv2_cot_creak_train': 1809,
'conala': 2669,
'synth_code': 3206,
'flanv2_cot_gsm8k_train': 3356,
'kojma_cot': 3135,
'essays': 1531,
'plot_screenplay_books': 8135,
'safety_image_prompt': 5001,
'synth_depression': 944,
'cuad': 497,
'flanv2_cot_sensemaking_train': 1589,
'anthrop_redteam': 1142,
'flanv2_cot_strategyqa_train': 357,
'flanv2_cot_ecqa_train': 2862,
'flanv2_cot_aqua_train': 1157,
'flanv2_cot_qasc_train': 516,
'wiki_toxic_nontoxic': 103
```

Topic map for a subset of the data:

```
.
├─Military Documents and Sentences____
│    ├─Burlington County Images and Employment Chart____
│    │    ├─Reports and assessments on risk analysis, data management, and industrial hygiene standards for tran
│    │    │    ├─NCHRP Reports for Transportation Management and Planning____
│    │    │    │    ├─■──Guidelines for Design of Corrosion-Damaged Bridge Superstructure with nchrp report____ ── Topic: 70
│    │    │    │    └─■──Transportation and Risk Management Practices____ ── Topic: 16
│    │    │    └─Assessment and Review of Chemical Agent Destruction Pilot Plants for Waste Disposal____
│    │    │         ├─■──Space Science and Technology Documents____ ── Topic: 18
│    │    │         └─Waste disposal, chemical agent destruction pilot plants review and assessment____
│    │    │              ├─■──Chemical Agent Destruction Pilot Plant Review and Assessment____ ── Topic: 48
│    │    │              └─■──Radioactive Waste Disposal and Alternative Treatments: Review of Various Documents____ ── Topic: 45
│    │    └─Highlighted Townships in Burlington County, NJ with Inset Maps____
│    │         ├─Township Highlighted in Burlington County - Image Prompts____
│    │         │    ├─Township Highlighting in Burlington County, New Jersey____
│    │         │    │    ├─■──Images and landmarks of Jonesboro, Waycross, and their respective counties in Arkansas and Georgia__ ── Topic: 97
│    │         │    │    └─■──Highlighted townships in Burlington County, New Jersey____ ── Topic: 26
│    │         │    └─Images and Workshop Summary Documents Related to Gulf Research Program, Mississippi River Basin Wate
│    │         │         ├─Geography and Environmental Issues in North and South America____
│    │         │         │    ├─■──Arctic Sea Ice Extent and Stability Analysis____ ── Topic: 96
│    │         │         │    └─Document topics related to rivers, maps, disasters, and ecosystem resilience in southern and eastern
│    │         │         │         ├─Geographic features in North and South America including rivers, watersheds, and ecosystems____
│    │         │         │         │    ├─■──Image Prompts for Cartographic Maps of Various Locations including South America, New Zealand, and t ── Topic: 19
│    │         │         │         │    └─■──Rivers and Ecosystems: Research and Monitoring in the Gulf and Oregon Watersheds____ ── Topic: 15
│    │         │         │         └─■──Disaster Resilience and Preparedness: Perspectives from Workshops and Case Studies____ ── Topic: 41
│    │         │         └─Geologic Survey and Cartographic Image Prompt with State Summary Information and District Boundaries
│    │         │              ├─■──Geological surveys and information on mineral resources in state parks____ ── Topic: 93
│    │         │              └─■──Drawings of geological features and caves including limestone, Coronado, and Pirinexus challenges___ ── Topic: 49
│    │         └─Graphical analysis of energy-related costs and trends over time____
│    │              ├─Graphs showing changes in U.S. employment, gasoline prices, energy expenditures, and employment cost
│    │              │    ├─■──Climate assessment and biogeochemical cycles with precipitation trends and image prompts.____ ── Topic: 56
│    │              │    └─Graphs showing changes in employment, natural gas electric generating capacity, and residential elec
│    │              │         ├─■──Energy Trends and Prices____ ── Topic: 6
│    │              │         └─■──Employment Trends in Selected Metropolitan Areas____ ── Topic: 3
│    │              └─■──Occupational injuries and illnesses rates and incidents in selected state and local government indus ── Topic: 63
│    └─Military operations and command updates in 2019____
│         ├─Health-related Workshop Proceedings and Image Prompts for Cancer, HIV, Health Literacy, and Accounti
│         │    ├─■──Promoting mental and behavioral health through effective therapy and preventive strategies____ ── Topic: 84
│         │    └─Health and healthcare approaches for various illnesses and conditions, including COVID-19, HIV, and 
│         │         ├─Health care and COVID-19: Cancer treatment, innovation, and accounting approaches in low-resource ar
│         │         │    ├─■──Images related to Covid-19 vaccination and prevention____ ── Topic: 10
│         │         │    └─■──Health Policy Workshop Proceedings and Image Covers for Cancer, Workforce, Literacy, and Accounting  ── Topic: 4
│         │         └─■──Annual Medical College Announcements in Philadelphia and Pennsylvania____ ── Topic: 67
│         └─Air Force documents covering various topics such as commanders, training, veterans, and change of co
│              ├─Air Force Operations and Training Documents____
│              │    ├─■──Documents related to military training and operations of Marine Corps and Army forces in 2013, 2017, ── Topic: 2
│              │    └─■──Images of Air Force Change of Command Ceremonies____ ── Topic: 1
│              └─Images and news related to the United States Defense Secretary James Mattis____
│                   ├─Images of Defense Secretary James Mattis in Meetings and Testimonies.____
│                   │    ├─■──Images related to Russian and Kazakh politicians including Solzhenitsyn, Yanukovych, Navalny, Aliyev ── Topic: 88
│                   │    └─■──Images featuring Defense Secretary James Mattis in official meetings and events.____ ── Topic: 7
│                   └─Police and Law Enforcement Activities and Incidents in Various Canadian Cities____
│                        ├─■──Protests and Demonstrations with Activists and Slogans____ ── Topic: 32
│                        └─■──Police activities in Windsor and Victoria, including commendations, dedicated flag, and crime scene  ── Topic: 22
└─Clipart use for teaching materials with unlimited access for Abcteach members____
     ├─Printable worksheets for kindergarten learning and coloring pages with image prompts and sensory act
     │    ├─Sports Image Prompts featuring Football, Cricket, Hockey and American Football Players____
     │    │    ├─Various Image Prompts for Drawings Related to Football and Valparaiso Football Season Disappointment
     │    │    │    ├─■──Valparaiso Crusaders Football Season____ ── Topic: 106
     │    │    │    └─Sports-themed image prompts and podcast related to football and basketball.____
     │    │    │         ├─■──Sports images with football players and throwback Riddell helmets____ ── Topic: 13
     │    │    │         └─■──Basketball and Kardashian-West sightings____ ── Topic: 23
     │    │    └─Indian Cricket - Matches, Images, and Cheer____
     │    │         ├─Indian Premier League and Cricket Matches____
     │    │         │    ├─■──Soccer Matches and Teams in Various Leagues____ ── Topic: 12
     │    │         │    └─■──Cricket matches and fans in India, featuring IPL teams Kings XI Punjab and Kolkata Knight Riders, Bo ── Topic: 9
     │    │         └─Olympic awards and championships won by athletes in various sports and attended by celebrities, with
     │    │              ├─Olympics-related Image and Sentence Prompts____
     │    │              │    ├─■──Images of Ricky Gervais, Jennifer Aniston, and Rachel Brosnahan at various award shows in Beverly Hi ── Topic: 8
     │    │              │    └─■──Olympic Medals and Champions in Tennis____ ── Topic: 21
     │    │              └─■──Mixed Combat Sports Culture with Boxing and Wrestling Championships____ ── Topic: 64
     │    └─Collection of Printable Worksheets for Kindergarten and Grade Levels____
     │         ├─Designing school hooded sweatshirts with super-soft cotton/poly fleece____
     │         │    ├─Collection of Robert Dennis Stereoscopic Views - Image Drawing Prompts____
     │         │    │    ├─Images of Greek and Byzantine Empires under different dynasties in ancient and medieval times, inclu
     │         │    │    │    ├─Images of the Byzantine Empire under various dynasties and territories in ancient times____
     │         │    │    │    │    ├─■──Cultural highlights of Asia - temples, burial complexes, and historic figures____ ── Topic: 78
     │         │    │    │    │    └─Byzantine Empire under various dynasties and territories in medieval times____
     │         │    │    │    │         ├─■──Art and History Document Prompts____ ── Topic: 47
     │         │    │    │    │         └─■──Byzantine Empire and its Dynasties with Territory and Depicted Borders____ ── Topic: 90
     │         │    │    │    └─■──Greek language and culture in modern and ancient Greece with various areas, religions, and historica ── Topic: 89
     │         │    │    └─Robert Dennis Stereoscopic Views image prompts and stability prompt____
     │         │    │         ├─Collection of Stereoscopic Views by Robert Dennis for Image Prompts____
     │         │    │         │    ├─Lamborghini and Ducati Racing Footage and Newsreels in Different Battle Zones and Civil Wars____
     │         │    │         │    │    ├─Lamborghini and Motorsports - Super Trofeo Races and Co-Branded Collections____
     │         │    │         │    │    │    ├─■──Motorsports and Racing with Schumacher, Capps, and more____ ── Topic: 74
     │         │    │         │    │    │    └─■──Lamborghini Super Trofeo and Automobili Celebrations____ ── Topic: 43
     │         │    │         │    │    └─Images prompts for various topics including Civil War, New York Stock Exchange, and Star Wars: Dange
     │         │    │         │    │         ├─Historical events and footage related to battles, wars, and stock exchange in different countries an
     │         │    │         │    │         │    ├─■──Various Battles and War-related Topics____ ── Topic: 27
     │         │    │         │    │         │    └─■──Stock newsreel videos of historical events in New York City____ ── Topic: 68
     │         │    │         │    │         └─Korean dramas with various casts and release dates, including "Window," "One Ordinary Day," "NCT 24h
     │         │    │         │    │              ├─■──Image prompts for various topics including Pickett N901-ES simplex slide rule, October issue of Peac ── Topic: 108
     │         │    │         │    │              └─■──Korean dramas and their cast and release dates, featuring "Racket Boys", "One Ordinary Day", "NCT 24 ── Topic: 104
     │         │    │         │    └─Stereoscopic views by Robert Dennis collection - Image prompts for drawing____
     │         │    │         │         ├─Retirement Banquet at Centennial Student Union, Mankato State University____
     │         │    │         │         │    ├─Religion and Faith Diversity in Infographics, Icons, and Images.____
     │         │    │         │         │    │    ├─■──Religious Icons and Symbols____ ── Topic: 38
     │         │    │         │         │    │    └─■──Images and Infographics Related to Muslims and Islamophobia____ ── Topic: 61
     │         │    │         │         │    └─Retirement Banquet at Mankato State University in June with Awards and Speakers____
     │         │    │         │         │         ├─Retirement banquet at Centennial Student Union, Mankato State University with awards and speakers.__
     │         │    │         │         │         │    ├─Images of African Union, Women's History Month, and Indigenous Tribes____
     │         │    │         │         │         │    │    ├─■──Celebrating Women's History Month and Women's Rights Activists____ ── Topic: 98
     │         │    │         │         │         │    │    └─Indigenous and African Union Partnerships in Tradition and Development____
     │         │    │         │         │         │    │         ├─■──Cultural Traditions and Sovereignty of Indigenous Peoples____ ── Topic: 29
     │         │    │         │         │         │    │         └─■──African Union Partnership for COVID-19 Media Outreach and Prevention____ ── Topic: 30
     │         │    │         │         │         │    └─Retirement Banquet at Centennial Student Union, Mankato State University____
     │         │    │         │         │         │         ├─■──Retirement Banquet Image Prompts at Mankato State University's Centennial Student Union, June____ ── Topic: 35
     │         │    │         │         │         │         └─■──Queensland State Archives images of Brisbane and surrounding areas in 1930s____ ── Topic: 100
     │         │    │         │         │         └─Drawings of Skyscrapers and Landmarks in Indianapolis and Tampa____
     │         │    │         │         │              ├─■──Images and documents related to Smithsonian, Whitney Museum of American Art, and Panama-Pacific Inte ── Topic: 58
     │         │    │         │         │              └─■──City Skylines - Indianapolis and Tampa____ ── Topic: 87
     │         │    │         │         └─Image prompts from Robert N. Dennis Collection of Stereoscopic Views for drawing different sceneries
     │         │    │         │              ├─Image prompts from Robert N. Dennis collection of stereoscopic views____
     │         │    │         │              │    ├─Images of animals and their interactions with humans in various settings____
     │         │    │         │              │    │    ├─■──Wildlife Encounters and Human Interactions in National Parks____ ── Topic: 110
     │         │    │         │              │    │    └─■──Images of dogs and their owners in various settings and activities (e.g. training, running marathons ── Topic: 91
     │         │    │         │              │    └─Image prompts from Robert Dennis Collection of Stereoscopic Views____
     │         │    │         │              │         ├─Garden Image Prompts - Wellington, Marengo, Sutton Place, Unidentified____
     │         │    │         │              │         │    ├─■──Images of Gardens and Outdoor Decor____ ── Topic: 14
     │         │    │         │              │         │    └─■──Wellington Real Estate Auctions and Subdivisions (with Cartographic Material)____ ── Topic: 46
     │         │    │         │              │         └─Robert Dennis Stereoscopic Views Collection Images of Cities and Landscapes____
     │         │    │         │              │              ├─■──Stereoscopic Views from Robert Dennis Collection of Various Cities____ ── Topic: 17
     │         │    │         │              │              └─■──Various Cathedrals and Landmarks in Different Locations____ ── Topic: 73
     │         │    │         │              └─Royal Family Events and Visits____
     │         │    │         │                   ├─■──Royal Events and Visits including Duchess of Cornwall, Duke and Duchess of Cambridge, Prince Harry,  ── Topic: 40
     │         │    │         │                   └─■──Funerals and Coffins of Victims in Ireland____ ── Topic: 113
     │         │    │         └─Memes, Invention, Archery, Politics, and Corrupt Politicians____
     │         │    │              ├─■──Memes, aliens, politics, and corruption in Minnesota____ ── Topic: 116
     │         │    │              └─■──Drawing memes related to inventions, archery, and humor.____ ── Topic: 39
     │         │    └─Invoice Design and Template Assistance for Pepperdine University Community____
     │         │         ├─Invoice and template design for Pepperdine University with remarkable dashboard and software feature
     │         │         │    ├─RTCA 2013 Brochure Provides Information on Current Telecom Projects and Successes____
     │         │         │    │    ├─VC Funds and Industry Analysis for Funding Rounds in Asia and Location Based Services during Recent 
     │         │         │    │    │    ├─■──VC Funds and Funding Rounds in Various Industries____ ── Topic: 71
     │         │         │    │    │    └─■──Drawings of blockchain and cryptocurrency-related events and companies, including Rio DeFi, Healthur ── Topic: 51
     │         │         │    │    └─RTCA 2013 Brochure Provides Information on Current Telecommunications Projects and Recent Successes_
     │         │         │    │         ├─Technology Innovation and Communications Engineering____
     │         │         │    │         │    ├─■──Innovation, Patents, Technology, Leadership, and Impact Trends____ ── Topic: 75
     │         │         │    │         │    └─■──Technology and Engineering Strategies for Outsourcing Telecommunications and Business Analytics____ ── Topic: 28
     │         │         │    │         └─■──rtca 2013 brochure provides current news and successes of projects____ ── Topic: 52
     │         │         │    └─Invoicing and Dashboard Templates for Pepperdine University and Business Use____
     │         │         │         ├─Wiring Diagrams for Home and Office____
     │         │         │         │    ├─Wiring Diagrams for Home and Office____
     │         │         │         │    │    ├─Wiring Diagrams for Manufacturing and Repair____
     │         │         │         │    │    │    ├─Small Machine Shop Owners' Reactions to Automated Manufacturing Research Facility____
     │         │         │         │    │    │    │    ├─■──Image prompts for small machine shop owners' reactions to automated manufacturing and CNC machine to ── Topic: 101
     │         │         │         │    │    │    │    └─■──Ford maintenance and repair manuals for various vehicle models including Bronco, Festiva, Ranger, an ── Topic: 53
     │         │         │         │    │    │    └─Electrical Wiring Diagrams for Various Applications____
     │         │         │         │    │    │         ├─■──Electrical Wiring Diagrams for Various Applications____ ── Topic: 25
     │         │         │         │    │    │         └─■──Various Images of Trains and Railways____ ── Topic: 69
     │         │         │         │    │    └─Furniture and Dining Table Ideas____
     │         │         │         │    │         ├─■──Various Lighting Ideas and Products for Different Settings and Purposes____ ── Topic: 65
     │         │         │         │    │         └─■──Drawing furniture and dining table sets with linen fabric and mahogany finish from image prompts.___ ── Topic: 31
     │         │         │         │    └─Roofing Companies and Services____
     │         │         │         │         ├─■──Product Recalls and Safety Hazards____ ── Topic: 99
     │         │         │         │         └─Roofing Companies and Services in Various Locations____
     │         │         │         │              ├─■──Wildland Firefighters and Fire Management Research____ ── Topic: 94
     │         │         │         │              └─■──Roofing Contractors and Services in Various Locations with Additional Related Keywords.____ ── Topic: 77
     │         │         │         └─Invoice Design and Approval at Pepperdine University's Community Platform.____
     │         │         │              ├─Invoice design template and approval process at Pepperdine University's communitypepperdineedu____
     │         │         │              │    ├─Pepperdine University invoice design and approval process____
     │         │         │              │    │    ├─Invoice Template and Dashboard for Pepperdine University and Business Invoicing with Free Downloads 
     │         │         │              │    │    │    ├─■──Pepperdine University Invoice Templates____ ── Topic: 44
     │         │         │              │    │    │    └─■──Image prompts for drawing related to business, contracts, and agreements____ ── Topic: 92
     │         │         │              │    │    └─Logo design entries in a contest for various businesses____
     │         │         │              │    │         ├─Logo Design Contest Entries____
     │         │         │              │    │         │    ├─Dell EMC IT Certifications and Technologies____
     │         │         │              │    │         │    │    ├─Illustration, Mendelian Genetics, and Irwaddy Dolphin's Skeleton in Museo di Storia Naturale____
     │         │         │              │    │         │    │    │    ├─■──Genetic mechanisms and structure of prokaryotic and eukaryotic cells____ ── Topic: 42
     │         │         │              │    │         │    │    │    └─■──Images of natural history specimens exhibited in museums with keywords including irrawaddy dolphin,  ── Topic: 111
     │         │         │              │    │         │    │    └─■──Dell EMC certification exam image prompts for networking, cloud infrastructure and services, and pow ── Topic: 54
     │         │         │              │    │         │    └─Logo Design Contest Entries for Various Businesses____
     │         │         │              │    │         │         ├─■──Logo Design Contest Entries____ ── Topic: 36
     │         │         │              │    │         │         └─■──Legal Documents Management for Law Firms and Corporate Legal Departments____ ── Topic: 86
     │         │         │              │    │         └─English subtitles download for various movies and shows____
     │         │         │              │    │              ├─Cannabis and Biome Grow Companies, Health Effects and Business Plan for Investors, and Doc Hollidaze
     │         │         │              │    │              │    ├─■──Cannabis Business and Cultivation featuring Highland Grow and Doc Hollidaze Premium Cannabis____ ── Topic: 107
     │         │         │              │    │              │    └─■──Board Results and Examinations across India (CBSE, ICSE, Punjab, Rajasthan, Tripura) including Suppl ── Topic: 117
     │         │         │              │    │              └─■──Subtitles Download for English Movies____ ── Topic: 105
     │         │         │              │    └─News and Reading Platforms for Sangrur and Barnala in Punjabi Jagran in 2014 for iPad, iPhone, and S
     │         │         │              │         ├─■──Smartphone brands and features - iPhone, Samsung Galaxy, Nokia launches and latest updates.____ ── Topic: 34
     │         │         │              │         └─■──News and e-paper articles in Punjabi and Hindi for Sangrur and Barnala on tablets and smartphones in ── Topic: 85
     │         │         │              └─Cyberbullying Prevention and Tactics____
     │         │         │                   ├─Image prompts for drawing based on podcast episodes with plugins for managing work and product grids
     │         │         │                   │    ├─■──Drawing image prompts for podcast episodes with various plugin features____ ── Topic: 79
     │         │         │                   │    └─■──Various topics related to Zuckerberg, Facebook, and related events____ ── Topic: 115
     │         │         │                   └─Cyberbullying Prevention Tactics with iPredator and Michael Nuccitelli____
     │         │         │                        ├─Investment in Gold and Silver Commodities on Comex by Managed Money with Speculative Positioning, ba
     │         │         │                        │    ├─■──Comex Managed Money Speculative Positions on Gold and Silver Futures and Options____ ── Topic: 95
     │         │         │                        │    └─■──Various Diamond Jewelry Images and Prompts____ ── Topic: 82
     │         │         │                        └─Cyberbullying Prevention Tactics____
     │         │         │                             ├─■──Scams and Romance - Protecting Yourself Online and Offline____ ── Topic: 102
     │         │         │                             └─■──Cyberbullying Prevention and Tactics through iPredator and Michael Nuccitelli's Work____ ── Topic: 83
     │         │         └─School Hooded Sweatshirts in Super-Soft Cotton/Poly Fleece____
     │         │              ├─Essays on Christmas, Macbeth, Romeo and Juliet with image prompts____
     │         │              │    ├─English literature analysis and critical essays on Macbeth, Romeo and Juliet, and The Catcher in the
     │         │              │    │    ├─■──Poetry and Essays by Various Famous Poets____ ── Topic: 76
     │         │              │    │    └─■──Essays on Shakespeare's Macbeth and Romeo and Juliet, as well as other literary works____ ── Topic: 37
     │         │              │    └─Price comparison of books on various subjects at popular e-commerce sites, and image prompts for dra
     │         │              │         ├─Price comparison of educational books on mathematics and psychology at popular online bookstores____
     │         │              │         │    ├─Price comparison and edition analysis for various subjects on Flipkart, Amazon, and other online boo
     │         │              │         │    │    ├─Price comparison of books on mathematics and psychology across major online retailers including Flip
     │         │              │         │    │    │    ├─■──Disney, Fantasyland, Imagineers, Walter Elias Disney, gravestone, plaque, inscribed.____ ── Topic: 80
     │         │              │         │    │    │    └─■──Price comparison for books on mathematics and psychology on various platforms (Flipkart, Amazon, etc ── Topic: 60
     │         │              │         │    │    └─Image prompts for physical fitness and science discussions____
     │         │              │         │    │         ├─Fitness, Mathematics, and Environmental Changes - Image Prompts for Physical Activity and Scientific
     │         │              │         │    │         │    ├─■──Fitness and Workout Mats – Improving Aerobic Fitness and Health with Non-Slip Exercise Mats____ ── Topic: 81
     │         │              │         │    │         │    └─■──Visual prompts and dialogues on changing physical and mathematical environments, coursework on nichr ── Topic: 72
     │         │              │         │    │         └─■──Career Pathways and Development Resources____ ── Topic: 114
     │         │              │         │    └─Christmas-themed Preschool Activity Ideas____
     │         │              │         │         ├─Christmas preschool theme with image prompts and activities incorporating alphabet, counting, and ho
     │         │              │         │         │    ├─■──Christmas themed image prompts, online shopping, and holiday traditions____ ── Topic: 55
     │         │              │         │         │    └─■──Preschool Alphabet Book Crafts____ ── Topic: 59
     │         │              │         │         └─■──Book covers and adventure novels____ ── Topic: 66
     │         │              │         └─Nutrition and Food Images and Prompts____
     │         │              │              ├─Agriculture and Horticulture Topics in Georgia, including Cotton, Wheat, and Greenhouse Management__
     │         │              │              │    ├─■──Agricultural innovations and community support in Holland, Burkina Faso, and Uganda____ ── Topic: 118
     │         │              │              │    └─■──Wheat crop and horticulture practices____ ── Topic: 62
     │         │              │              └─Nutrition and Food Science____
     │         │              │                   ├─■──Canned meats and fruits, stability and quality symposium, and image prompts for food drawings____ ── Topic: 33
     │         │              │                   └─■──Nutrition and Image Prompts____ ── Topic: 57
     │         │              └─School Hooded Cotton Sweatshirts with Super-Soft Fleece____
     │         │                   ├─Dress and Fashion Image Prompts, Medieval Fantasy Paper Dresses, and Elegant Tulle Prom Dresses____
     │         │                   │    ├─■──Fantasy Paper Doll Outfits and Image Prompts____ ── Topic: 103
     │         │                   │    └─■──Fashion and Dresses Inspiration____ ── Topic: 11
     │         │                   └─High school hooded sweatshirts in super-soft cotton/poly fleece____
     │         │                        ├─■──High School Hooded Sweatshirts - Super Soft Cotton/Poly Fleece to Keep You Warm on the Sidelines____ ── Topic: 20
     │         │                        └─■──High School Racerback Tank Tops with District Threads____ ── Topic: 109
     │         └─Worksheets and Printables for Math, Kindergarten, and Beyond____
     │              ├─Math and Reading Worksheets for Grades 7-9____
     │              │    ├─■──Printable worksheets for math, reading, and kindergarten learning with image prompts.____ ── Topic: 5
     │              │    └─■──Math Games and Activities for Engaging Students in Homeschool and Classroom Settings____ ── Topic: 112
     │              └─■──Coloring Pages for Various Themes and Sizes____ ── Topic: 24
     └─Clipart use for teaching materials with unlimited access for members on abcteach____
          ├─■──Clipart use for teaching materials in commercial format with unlimited illustrations as an abcteach  ── Topic: 0
          └─■──Flags Clipart for Teaching with Abcteach Membership____ ── Topic: 50

```
Thanks to LAION volunteers: @Rallio, @Kenhktsui, @Danielpatrickhug  @Vyprix and @Summer. 

