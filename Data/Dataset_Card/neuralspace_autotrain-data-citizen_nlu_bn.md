---
language:
- bn
task_categories:
- text-classification

---
# AutoTrain Dataset for project: citizen_nlu_bn

## Dataset Descritpion

This dataset has been automatically processed by AutoTrain for project citizen_nlu_bn.

### Languages

The BCP-47 code for the dataset's language is bn.

## Dataset Structure

### Data Instances

A sample from this dataset looks as follows:

```json
[
  {
    "text": "\u0997\u09a4 \u09e8 \u09ae\u09be\u09b8 \u0986\u09ae\u09be\u09b0 \u0986\u0997\u09c7 \u0995\u09b0\u09cb \u09a8\u09be \u0986\u09ae\u09bf \u0995\u09a4 \u09a6\u09bf\u09a8 \u09aa\u09b0\u09c7 \u09b0\u0995\u09cd\u09a4 \u09a6\u09bf\u09a4\u09c7 \u09aa\u09be\u09b0\u09bf?",
    "target": 3
  },
  {
    "text": "\u09b9\u09a0\u09be\u09ce \u0986\u09ae\u09bf \u09a6\u09cb\u0995\u09be\u09a8\u09c7 \u09af\u09be\u0993\u09af\u09bc\u09be\u09b0 \u099c\u09a8\u09cd\u09af \u098f\u0995\u099f\u09bf \u0996\u09be\u09b2\u09bf \u09b0\u09be\u09b8\u09cd\u09a4\u09be\u09af\u09bc \u09b9\u09be\u0981\u099f\u099b\u09bf\u09b2\u09be\u09ae \u09b8\u09be\u09a6\u09be \u09b0\u0999\u09c7\u09b0 \u0993\u09ac\u09bf 005639 \u0986\u09ae\u09bf \u09b0\u09bf\u09aa\u09cb\u09b0\u09cd\u099f \u0995\u09b0\u09ac \u09af\u0996\u09a8 \u0986\u09ae\u09bf \u09a4\u09be\u09b0 \u0995\u09be\u099b\u09c7 \u0986\u09b8\u09ac \u098f\u09ac\u0982 \u09a7\u09be\u0995\u09cd\u0995\u09be \u09a6\u09bf\u09af\u09bc\u09c7 \u099a\u09b2\u09c7 \u09af\u09be\u09ac",
    "target": 44
  }
]
```

### Dataset Fields

The dataset has the following fields (also called "features"):

```json
{
  "text": "Value(dtype='string', id=None)",
  "target": "ClassLabel(num_classes=55, names=['ContactRealPerson', 'Eligibility For BloodDonationWithComorbidities', 'EligibilityForBloodDonationAgeLimit', 'EligibilityForBloodDonationCovidGap', 'EligibilityForBloodDonationForPregnantWomen', 'EligibilityForBloodDonationGap', 'EligibilityForBloodDonationSTD', 'EligibilityForBloodReceiversBloodGroup', 'EligitbilityForVaccine', 'InquiryForCovidActiveCasesCount', 'InquiryForCovidDeathCount', 'InquiryForCovidPrevention', 'InquiryForCovidRecentCasesCount', 'InquiryForCovidTotalCasesCount', 'InquiryForDoctorConsultation', 'InquiryForQuarantinePeriod', 'InquiryForTravelRestrictions', 'InquiryForVaccinationRequirements', 'InquiryForVaccineCost', 'InquiryForVaccineCount', 'InquiryOfContact', 'InquiryOfCovidSymptoms', 'InquiryOfEmergencyContact', 'InquiryOfLocation', 'InquiryOfLockdownDetails', 'InquiryOfTiming', 'InquiryofBloodDonationRequirements', 'InquiryofBloodReceivalRequirements', 'InquiryofPostBloodDonationCareSchemes', 'InquiryofPostBloodDonationCertificate', 'InquiryofPostBloodDonationEffects', 'InquiryofPostBloodReceivalCareSchemes', 'InquiryofPostBloodReceivalEffects', 'InquiryofVaccinationAgeLimit', 'IntentForBloodDonationAppointment', 'IntentForBloodReceivalAppointment', 'ReportingAnimalAbuse', 'ReportingAnimalPoaching', 'ReportingChildAbuse', 'ReportingCyberCrime', 'ReportingDomesticViolence', 'ReportingDowry', 'ReportingDrugConsumption', 'ReportingDrugTrafficing', 'ReportingHitAndRun', 'ReportingMissingPerson', 'ReportingMissingPets', 'ReportingMissingVehicle', 'ReportingMurder', 'ReportingPropertyTakeOver', 'ReportingSexualAssault', 'ReportingTheft', 'ReportingTresspassing', 'ReportingVehicleAccident', 'StatusOfFIR'], id=None)"
}
```

### Dataset Splits

This dataset is split into a train and validation split. The split sizes are as follow:

| Split name   | Num samples         |
| ------------ | ------------------- |
| train        | 27146 |
| valid        | 6800 |
