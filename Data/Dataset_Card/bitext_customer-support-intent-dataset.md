Bitext - Customer Service Tagged Training Dataset for Intent Detection
======================================================================

Overview
--------

The dataset can be used to train intent recognition models on Natural Language Understanding (NLU) platforms: LUIS, Dialogflow, Lex, RASA and more.
The dataset covers the "Customer Service" domain and includes:
  - 11 categories or intent groups
  - 27 intents assigned to one of the 11 categories
  - 8,175 utterances assigned to the 27 intents

Additionally, each utterance is enriched with tags that indicate the type of language variation that the utterance expresses. Examples include:
  - The tag “COLLOQUIAL” indicates that the utterance contains informal expressions: “can u close my account”
  - The tag “INTERROGATIVE” indicates that the utterance is a question: “how do I open an account”
  - The tag “OFFENSIVE” indicates that the utterance contains offensive expressions: “open my f****** account”

There are a total of 11 tags. See below for a full list of tags, categories and intents.

The purpose of these tags is to customize the dataset so the trained bot can easily adapt to different user language profiles. A bot that sells sneakers and targets a younger population should be proficient in colloquial language; while a classical retail banking bot should be able to handle more formal or polite language.

These intents have been selected from Bitext's collection of 20 domain-specific datasets (banking, retail, utilities...), covering the intents that are common across all 20 domains. For a full list of domains see https://www.bitext.com/chatbot-verticals/.

Utterances and Linguistic Tags
------------------------------------
The dataset contains 8,175 training utterances, with between 290 and 324 utterances per intent. 

The dataset has been split into training (80%), validation (10%) and testing (10%) sets, preserving the distribution of intents and linguistic phenomena.

The dataset also reflects commonly occurring linguistic phenomena of real-life chatbots, such as: spelling mistakes, run-on words, punctuation errors…

Each entry in the dataset contains the following four fields:
  - utterance: a user utterance from the Customer Service domain
  - intent: the intent corresponding to the user utterance
  - category: the high-level semantic category for the intent
  - tags: different tags that reflect the types of language variations expressed in the utterance

The dataset contains tags that reflect different language phenomena like colloquial or offensive language. So if an utterance for intent “cancel_order” contains the “COLLOQUIAL” tag, the utterance will express an informal language variation like: “can u cancel my order”

Each utterance is enriched with one or more of these tags:
 - Register tags: colloquial language, polite language…
    - Q - Colloquial variation
    - P - Politeness variation
 - Content tags: offensive language, keyword language…
    - W - Offensive language
    - K - Keyword language
 - Linguistic tags: syntactic and morphological tags (interrogative sentence, coordinated sentence…) 
    - B - Basic syntactic structure
    - C - Coordinated syntactic structure
    - I - Interrogative structure
    - M - Morphological variation (plurals, tenses…)
    - L - Lexical variation (synonyms)
    - E - Expanded abbreviations (I'm -> I am, I'd -> I would…)
 - Real-life errors: spelling errors, punctuation errors…
    - Z - Noise phenomena like spelling or punctuation errors

These tags indicate the type of language variation that the utterance expresses. When associated to each utterance, they allow Conversational Designers to customize training datasets to different user profiles with different uses of language. Through these tags, many different datasets can be created to make the resulting assistant more accurate and robust. A bot that sells sneakers should be mainly targeted to younger population that use a more colloquial language; while a classical retail banking bot should be able to handle more formal or polite language.

Categories and Intents
----------------------
The categories and intents covered by the dataset are:
  - ACCOUNT: create_account, delete_account, edit_account, recover_password, registration_problems, switch_account
  - CANCELLATION_FEE: check_cancellation_fee
  - CONTACT: contact_customer_service, contact_human_agent
  - DELIVERY: delivery_options, delivery_period
  - FEEDBACK: complaint, review
  - INVOICE: check_invoice, get_invoice
  - NEWSLETTER: newsletter_subscription, 
  - ORDER: cancel_order, change_order, place_order, track_order
  - PAYMENT: check_payment_methods, payment_issue
  - REFUND: check_refund_policy, get_refund, track_refund
  - SHIPPING_ADDRESS: change_shipping_address, set_up_shipping_address

(c) Bitext Innovations, 2022
