
## Codespaces

Start codespaces with this link. Wait a few minutes for `requirements.txt` to be installed.

## Local setup
Setup virtual env with

```bash
python -m venv ./env               
source env/bin/activate # use virtual environment
pip install -r requirements.txt
```

## Setup tables

Setup tables and data with the following command:

```bash
./setup.sh
```

## Run ETL

```bash
python ecommerce/ecommerce/dim_customer_etl.py
```

## Test ETL run 

```bash
sqlite3 ecommerce.db < ./setup/3-check-count.sql 
```

The above query should return

110
110
27


