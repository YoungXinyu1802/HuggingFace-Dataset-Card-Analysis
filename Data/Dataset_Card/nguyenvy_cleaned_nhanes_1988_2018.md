---
license: cc-by-4.0
---

Description: The National Health and Nutrition Examination Survey (NHANES) provides data on the health and environmental exposure of the non-institutionalized US population. Such data have considerable potential to understand how the environment and behaviors impact human health. These data are also currently leveraged to answer public health questions such as prevalence of disease. However, these data need to first be processed before new insights can be derived through large-scale analyses. NHANES data are stored across hundreds of files with multiple inconsistencies. Correcting such inconsistencies takes systematic cross examination and considerable efforts but is required for accurately and reproducibly characterizing the associations between the exposome and diseases (e.g., cancer mortality outcomes). Thus, we developed a set of curated and unified datasets and accompanied code by merging 614 separate files and harmonizing unrestricted data across NHANES III (1988-1994) and Continuous (1999-2018), totaling 134,310 participants and 4,740 variables. The variables convey 1) demographic information, 2) dietary consumption, 3) physical examination results, 4) occupation, 5) questionnaire items (e.g., physical activity, general health status, medical conditions), 6) medications, 7) mortality status linked from the National Death Index, 8) survey weights, 9) environmental exposure biomarker measurements, and 10) chemical comments that indicate which measurements are below or above the lower limit of detection. We also provide a data dictionary listing the variables and their descriptions to help researchers browse the data. We also provide R markdown files to show example codes on calculating summary statistics and running regression models to help accelerate high-throughput analysis of the exposome and secular trends on cancer mortality.

csv Data Record: The curated NHANES datasets and the data dictionaries includes 13 .csv files and 1 excel file. The curated NHANES datasets involves 10 .csv formatted files, one for each module and labeled as the following:  1) mortality, 2) dietary, 3) demographics, 4) response, 5) medications, 6) questionnaire, 7) chemicals, 8) occupation, 9) weights, and 10) comments. The eleventh file is a dictionary that lists the variable name, description, module, category, units, CAS Number, comment use, chemical family, chemical family shortened, number of measurements, and cycles available for all 4,740 variables in NHANES (“dictionary_nhanes.csv”). The 12th csv file contains the harmonized categories for the categorical variables (“dictionary_harmonized_categories.csv”). The 13th file contains the dictionary for descriptors on the drugs codes (“dictionary_drug_codes.csv”). The 14th file is an excel file that contains the cleaning documentation, which records all the inconsistencies for all affected variables to help curate each of the NHANES datasets (“nhanes_inconsistencies_documentation.xlsx”). 

R Data Record: For researchers who want to conduct their analysis in the R programming language, the curated NHANES datasets and the data dictionaries can be downloaded as a .zip file which include an .RData file and an .R file. We provided an .RData file that contains all the aforementioned datasets as R data objects (“w - nhanes_1988_2018.RData”). Also in this .RData file, we make available all R scripts on customized functions that were written to curate the data. We also provide an .R file that shows how we used the customized functions (i.e. our pipeline) to curate the data (“m - nhanes_1988_2018.R”).

Example starter codes: The set of starter code to help users conduct exposome analysis consists of four R markdown files (.Rmd). We recommend going through the tutorials in order. “example_0 - merge_datasets_together.Rmd” demonstrates how to merge the curated NHANES datasets together. “example_1 - account_for_nhanes_design.Rmd” demonstrates how to conduct a linear regression model, a survey-weighted regression model, a Cox proportional hazard model, and a survey-weighted Cox proportional hazard model. “example_2 - calculate_summary_statistics.Rmd” demonstrates how to calculate summary statistics for one variable and multiple variables with and without accounting for the NHANES sampling design. “example_3 - run_multiple_regressions.Rmd” demonstrates how run multiple regression models with and without adjusting for the sampling design.