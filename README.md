
Setup virtual env with

```bash
python -m venv ./env               
source env/bin/activate # use virtual environment
```

Install libraries (will pip freeze later)

```bash

```

Create sqlite3 tables with ./setup/1-create-tables.sql, with the folllowing command:

```bash
rm -rf ecommerce.db
sqlite3 ecommerce.db < ./setup/1-create-tables.sql
sqlite3 ecommerce.db < ./setup/2-populate-raw-tables.sql
```


