## Dataset: Swiss Legislation

### Description
This dataset contains legislation texts in five languages: 
- German _(17,559 entries)_
- French _(11,197 entries)_
- Italian _(6,201 entries)_
- Romansh _(534 entries)_
- English _(207 entries)_
  
The total number of texts in the dataset is 35,698. The dataset is saved in _lexfind_v2.jsonl_ format.

### Data
Each entry in the dataset is a dictionary with the following keys:
- `canton`: the canton of origin of the legislation
  - example: "ag"
- `language`: the language of the legislation
  - example: "de"
- `uuid`: a unique identifier for the legislation
  - example: "ec312f57-05fe-4552-ba50-8c9c269e0f3b"
- `title`: the title of the legislation
  - example: "Gesetz über die Geoinformation im Kanton Aargau"
- `short`: a short description of the legislation
  - example: "Kantonales Geoinformationsgesetz"
- `abbreviation`: an abbreviation for the legislation
  - example: "KGeoIG"
- `sr_number`: a reference number for the legislation
  - example: "740.100"
- `is_active`: whether the legislation is currently in force
  - example: true
- `version_active_since`: the date since when the legislation's current version is active
  - example: "2021-09-01"
- `family_active_since`: the date since when the legislation's current version's family is active
  - example: "2011-05-24"
- `version_inactive_since`: the date since when the legislation's current version is inactive
  - example: null
- `version_found_at`: the date the legislation's current version was found
  - example: "2021-09-01"
- `pdf_url`: a link to the legislation's pdf
  - example: "https://www.lexfind.ch/tol/1557/de"
- `html_url`: a link to the legislation's html
  - example: "https://gesetzessammlungen.ag.ch/app/de/texts_of_law/740.100")_
- `pdf_content`: the legislation's pdf content
  - example: "740.100 - Gesetz über..."
- `html_content`: the legislation's html content
  - example: ""
- `changes`: a list of changes made to the legislation
  - example: []
- `history`: a list of the legislation's history
  - example: []
- `quotes`: a list of quotes from the legislation
  - example: []

### Splits
There is only one split in this dataset, which contains all the legislation texts.

