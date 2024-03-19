# coderhouse-de-entregable02

This repo contains the notebooks for the second homework of the course of data engineering at CoderHouse.

### 1-create-table-in-database.ipynb

This Jupyter Notebook contains code for creating the target table in the database (this code was part of the homework 1).

### 2-load-data-to-rds.ipynb

This Jupyter Notebook uses functions defined in utils to get exchange rates from many currencies from Frankfuter API, transform the daily rates to monthly rates by taking the mean, validates format and data, and finally uploads data to DB.

### utils/

- `extraction.py`: contains functions to get data from Frankfuter API (this code was part of the homework 1).
- `load_to_db.py`: contains the function used to load data to DB using psycopg2
- `validation.py`: contains functions to validate format and data previous to load it to DB.

#### Execution Steps

1. **Create table in DB:** Executes notebook ` 1-create-table-in-database.ipynb` to create the target table in DB.
2. **ETL:** Executes notebook `2-load-data-to-rds.ipynb` to get exchange rates from Frankfuter API, transform the date, validates format, and finally upload it to DB.


## Environment Configuration

### environment.yml

The `environment.yml` file contains the configuration necessary to recreate the project environment. You can use this file with conda to create a virtual environment with the required dependencies. There is also a `requirements.txt` file to recreate the project environment not using conda.

#### Recreate Environment (using conda)

```bash
conda env create -f environment.yml
conda activate  coderhouse-de-02
```