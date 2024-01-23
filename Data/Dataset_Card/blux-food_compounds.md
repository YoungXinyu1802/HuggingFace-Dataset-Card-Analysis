# Definición de campos

1. **uci_id**: UniChEM identifier.
2. **chembl_id**: ChEMBL identifier.
3. **molecule_type**: Type of molecule (Small molecule, Protein, Antibody, Oligosaccharide, Oligonucleotide, Cell, Unknown).⁶
4. **alogp**: Calculated ALogP. Ghose-Crippen-Viswanadhan octanol-water partition coefficient (ALogP).¹ ²
5. **aromatic_rings**: number of aromatic rings. Aromatic rings are common structural components of polymers.
6. **cx_logd**: The calculated octanol/water distribution coefficient at pH7.4 using ChemAxon v17.29.0.³
7. **cx_logp**: The calculated octanol/water partition coefficient using ChemAxon v17.29.0.³
8. **cx_most_apka**: The most acidic pKa calculated using ChemAxon v17.29.0.³
9. **cx_most_bpka**: The most basic pKa calculated using ChemAxon v17.29.0.³
10. **full_molformula**: Molecular formula for the full compound (including any salt).⁴
11. **full_mwt**: Molecular weight of the full compound including any salts.⁴
12. **hba**: Number hydrogen bond acceptors.⁴
13. **hba_lipinski**: Number of hydrogen bond acceptors calculated according to Lipinski's original rules (i.e., N + O count)).⁴
14. **hbd**: Number hydrogen bond donors.⁴
15. **hbd_lipinski**: Number of hydrogen bond donors calculated according to Lipinski's original rules (i.e., NH + OH count).⁴
16. **heavy_atoms**: Number of heavy (non-hydrogen) atoms.⁴
17. **molecular_species**: Indicates whether the compound is an acid/base/neutral.⁵
18. **mw_freebase**: Molecular weight of parent compound.⁴
19. **mw_monoisotopic**: Monoisotopic parent molecular weight.⁴
20. **num_lipinski_ro5_violations**: Number of violations of Lipinski's rule of five using HBA_LIPINSKI and HBD_LIPINSKI counts.⁵
21. **num_ro5_violations**: Number of violations of Lipinski's rule-of-five, using HBA and HBD definitions.⁵
22. **psa**: Polar surface area.⁴
23. **qed_weighted**: Weighted quantitative estimate of drug likeness (as defined by Bickerton et al., Nature Chem 2012).⁴
24. **ro3_pass**: Indicates whether the compound passes the rule-of-three (mw < 300, logP < 3 etc).⁵
25. **rtb**: Number rotatable bonds.⁴
26. **canonical_smiles**: Canonical smiles, with no stereochemistry information. Generated using pipeline pilot.⁵
27. **standard_inchi**: IUPAC standard InChI for the compound.⁵
28. **standard_inchi_key**: IUPAC standard InChI key for the compound.⁵
29. **natural_product**: Indicates whether the compound is natural product-derived (currently curated only for drugs).⁶
30. **inorganic_flag**: Indicates whether the molecule is inorganic (i.e., containing only metal atoms and <2 carbon atoms).⁶
31. **therapeutic_flag**: Indicates that a drug has a therapeutic application (as opposed to e.g., an imaging agent, additive etc).⁶
32. **biotherapeutic**: A single related resource. Can be either a URI or set of nested resource data.⁶
33. **polymer_flag**: Indicates whether a molecule is a small molecule polymer (e.g., polistyrex).⁶
34. **prodrug**: Indicates that the molecule is a pro-drug (see molecule hierarchy for active component, where known).⁶
35. **kegg_id**: KEGG identifier.
36. **formula**: Molecular formula for the full compound.
37. **exact_mass**: Mass of the compound (from KEGG).
38. **mol_weight**: mass of a molecule of a substance, based on 12 as the atomic weight of carbon-12.⁸
39. atom: An ATOM entry represents KEGG Atom Type .¹⁰
40. **bond**: A BOND entry is defined as a pair of ATOM entries that form a chemical bond in a molecule, corresponding to many named bonds in organic chemistry and biochemistry. ¹⁰
41. **chebi_id**: ChEBI identifier.
42. **definition**: A simple definition of this compound.
43. **mass**: Returns the average mass. The relative masses are calculated from tables of relative atomic masses (atomic weights) published by IUPAC. (from CheBI).⁷
44. **mol**: ChEBI stores the two-dimensional or three-dimensional structural diagrams as connection tables in MDL molfile format.⁷
45. **smiles**: The simplified molecular-input line-entry system (SMILES) is a specification in the form of a line notation for describing the structure of chemical species using short ASCII strings.
46. **inchi**: The International Chemical Identifier (InChI) is a textual identifier for chemical substances, designed to provide a standard way to encode molecular information and to facilitate the search for such information in databases and on the web.
47. **inchi_key**: The InChIKey, sometimes referred to as a hashed InChI, is a fixed length (27 character) condensed digital representation of the InChI that is not human-understandable.
48. **cas_id**: CAS Registry Number. A CAS Registry Number is a unique and unambiguous identifier for a specific substance that allows clear communication and, with the help of CAS scientists, links together all available data and research about that substance.
49. **substance**: Full substance name as recognized by CFSAN (FDA). ⁹
50. **regs**: Code of Federal Regulations associated numbers of this compound (FDA). ⁹
51. **syns**: Synonyms of the compound (FDA).
52. **used_for**: The physical or technical effect(s) the substance has in or on food; see 21 CFR 170.3(o) for definitions. (FDA). ⁹



¹ http://chemgps.bmc.uu.se/help/dragonx/GhoseCrippenViswanadhanAlogP.html

² http://www.talete.mi.it/help/dproperties_help/index.html?molecular_properties.htm

³ http://chembl.blogspot.com/2020/03/chembl-26-released.html

⁴ https://micha-protocol.org/glossary/index

⁵ https://www.ebi.ac.uk/chembl/api/data/drug/schema

⁶ https://www.ebi.ac.uk/chembl/api/data/molecule/schema

⁷ http://libchebi.github.io/libChEBI%20API.pdf

⁸ https://www.britannica.com/science/molecular-weight

⁹ https://www.cfsanappsexternal.fda.gov/scripts/fdcc/?set=FoodSubstances&sort=Used_for_Technical_Effect

¹⁰ https://bmcsystbiol.biomedcentral.com/articles/10.1186/1752-0509-7-S6-S2
