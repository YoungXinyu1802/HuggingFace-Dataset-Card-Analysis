# README 
## Annotated Student Feedback
---
annotations_creators: []
language:
- en
license:
- mit
---
This resource contains 3000 student feedback data that have been annotated for aspect terms, opinion terms, polarities of the opinion terms towards targeted aspects, document-level opinion polarities, and sentence separations.

### Folder Structure of the resource,

```bash
    └───Annotated Student Feedback Data
    ├───Annotator_1
    │   ├───Annotated_part_1
    │   ├───Annotated_part_2
    │   └───towe-eacl_recreation_data_set
    │       ├───defomative comment removed
    │       └───less than 100 lengthy comment
    ├───Annotator_2
    │   ├───Annotated_part_3
    │   ├───Annotated_part_4
    │   └───Annotated_part_5
    └───Annotator_3
        └───Annotated_part_6
```

Each Annotated_part_# folders contain three files. Those are in XMI, XML, and ZIP formats. 
XMI files contain the annotated student feedback data and XML files contain tagsets used for annotation.

Find the code for reading data from XML and XMI files in `code_for_read_annotated_data.py`
