### **Motivation**

Get more hands-on experience & intuition about some lightweight _(no separate dedicated server)_ storage options for the purposes of storing and querying medium-size datasets.

* * *

### Suggested experiment

1.  Dataset  
    create some representative datasets:
    1.  2 datasets
    2.  how many tables:
        1.  one dataset – 1 table
        2.  second dataset – 2/3 tables
    3.  table size:
        1.  setting 1: ~2 mln rows per table
        2.  _(optional)_ setting 2: ~5-10 mln rows per table
    4.  ~300 attributes/columns per table
    5.  domain: smth close to POC could be great (but not mandatory). I.e. some person/organization-related records with some personal + insurance (or generally some products) info
    6.  let’s store each table as a separate .csv file as a proxy for some external database (as a starting point for ingestion)
2.  Engines to try out  
    Smth like:
    1.  DuckDB
    2.  maybe SQLite (maybe more for comparison reasons)
    3.  pure Pandas?
    4.  anything else interesting?  
        No need for more than 2-3 options
3.  What to check
    1.  Ingestion process
        1.  time
        2.  complexity (any constraints, prerequisites)
        3.  resource usage, approximate (RAM, CPU, machine type)
    2.  Queries
        1.  simple iteration through 1 big table
            1.  time, resource usage
        2.  analytical column-wise query (e.g. calculate the average of some numerical attribute)
            1.  time, resource usage
        3.  some simple join (just to understand how bad it performs for such queries)
            1.  time, resource usage
        4.  _(optional)_ some “insight” on the data: some simplified socio-economic index per Mary’s suggestion (take a few attributes, calculate their statistics and plug it in some formula, use this formula to assign some value to each record in table)
            1.  time, resource usage

* * *

### Expected results

One report that includes:

1.  Description of the data used
2.  Benchmarks results
3.  Some most important pros/cons of the selected engines
4.  _(Optional)_ the most interesting links (suggest having no more than ~5)

Total size of report: suggested not more than 2-3 pages in Google doc.

### How to run the experiment

In order to run the experiment, you need to have Python 3.7+ installed.
1.  Install dependencies
```bash
pip3 install -r requirements.txt
```

2.  Generate datasets 
```bash
python3 generate_datasets.py
```

It generates daatasets in `data` folder.

3.  Run benchmarks
Need to specify test scenario name and path to the dataset file (for example from the previous step):
```bash
python3 benchmark_cli.py --test_scenario <test_scenario_name> --path <data_file>
```

### How to run all tests

```bash
chmod +x run_all.sh
./run_all.sh
```
