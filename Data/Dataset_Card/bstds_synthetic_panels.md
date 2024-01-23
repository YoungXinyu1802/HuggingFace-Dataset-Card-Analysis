---
dataset_info:
  features:
  - name: UNIQUE_PERSON_ID
    dtype: int64
  - name: AGE
    dtype: int64
  - name: NAME
    dtype: string
  - name: NAME_EN
    dtype: string
  - name: DISTRICT
    dtype: string
  - name: MARITAL_STATUS
    dtype: string
  - name: GENDER
    dtype: string
  - name: DATE_OF_BIRTH
    dtype: int64
  - name: BUSINESS_LINE
    dtype: int64
  - name: CITY
    dtype: string
  - name: CITY_HE
    dtype: string
  - name: NUM_INSURANCE_PRODUCTS
    dtype: int64
  - name: LOANS_ON_FUNDS
    dtype: float64
  - name: MORTGAGE_IND
    dtype: int64
  - name: MORTGAGE_LIFE_INSURANCE
    dtype: float64
  - name: PROPERTY_ROOM_NUM
    dtype: float64
  - name: AVERAGE_REAL_ESTATE_PRICE
    dtype: float64
  - name: SALARY
    dtype: float64
  - name: NUM_MINORS_INSURED
    dtype: float64
  - name: PAYMENT_ISSUES_IND
    dtype: int64
  - name: CUSTOMER_VALUE
    dtype: float64
  - name: CONTACT_DETAILS
    dtype: string
  - name: LOB_IND
    dtype: int64
  - name: SUPPL_PENSION_IND
    dtype: int64
  - name: ACCUM_IN_MMP
    dtype: float64
  - name: NORM_ACCUM_PER_AGE_MMP
    dtype: float64
  - name: AGENT_IND_MMP
    dtype: int64
  - name: SUBSCR_PENSION_CLRHOUSE_IND
    dtype: int64
  - name: ACCUM_INTERNAL_CLRHOUSE
    dtype: float64
  - name: EXECUTIVE_INSURANCE
    dtype: float64
  - name: CRITICAL_ILLNESS_INSURANCE
    dtype: float64
  - name: ABROAD_INSURANCE_LOC
    dtype: string
  - name: ABROAD_INSURANCE_DURATION
    dtype: int64
  - name: MORTGAGE_RISK_IND
    dtype: int64
  - name: MEDICAL_EXCLUSIONS
    dtype: string
  - name: ACCUM_SAVING_POLICY
    dtype: float64
  - name: MONTHLY_SAVINGS_PAYMENT
    dtype: float64
  - name: AGENT_IND_MMH
    dtype: int64
  - name: VEHICLE
    dtype: string
  - name: AVERAGE_KM_PER_YEAR
    dtype: float64
  - name: RELEVANT_INS_POLICY
    dtype: int64
  - name: WIN_POLICY_DETAILS
    dtype: string
  - name: CAR_INS_AMOUNT
    dtype: float64
  - name: CAR_INS_NEG_HISTORY
    dtype: int64
  - name: HOME_INS_AMOUNT
    dtype: float64
  splits:
  - name: train
    num_bytes: 805109157
    num_examples: 2000000
  download_size: 331325790
  dataset_size: 805109157
---
# Dataset Card


* AVERAGE_REAL_ESTATE_PRICE - [stats](https://www.cbs.gov.il/en/publications/madad/Pages/2023/Average-Housing-Indices-and-Prices%20-January-2023.aspx)
* CAR_INS_AMOUNT - 2.5%-7% of the car price and car prices are from [here](https://centro.co.il/en/auto/used)

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)