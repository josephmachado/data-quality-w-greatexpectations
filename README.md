
* [Setup](#setup)
    * [Github Codespaces](#github-codespaces)
    * [Locally with virtual environment](#locally-with-virtual-environment)
    * [Create the tables necessary for the ETL](#create-the-tables-necessary-for-the-etl)
* [Run ETL](#run-etl)
* [Test ETL output](#test-etl-output)
* [Validation results](#validation-results)

Code for the blog: **[How to implement data quality checks with greatexpectations](https://www.startdataengineering.com/post/implement_data_quality_with_great_expectations/)**

## Setup

You can run this via 

### Github Codespaces

Simply click on this **[link]** and you will be able to run your own code space with this repository. Wait for a few minutes for codespaces to install all the packages in **[requirements.txt](./requirements.txt)**.

:heavy_exclamation_mark: **Caution**: Codespaces only have limited free availability

### Locally with virtual environment

You can clone this repo and setup a virtual environment to run the code. You will need [Python >= 3.10](https://www.python.org/downloads/) and [git](https://git-scm.com/downloads) installed.

```bash
git clone https://github.com/josephmachado/data-quality-w-greatexpectations.git
cd data-quality-w-greatexpectations
python -m venv ./env               
source env/bin/activate # use virtual environment
pip install -r requirements.txt
```

### Create the tables necessary for the ETL

Once you have the environment ready (either via codespaces or locally), run the setup script that **[creates tables](./setup/1-create-tables.sql)**, and **[inserts data](./setup/2-populate-raw-tables.sql)** into them.

```bash
# in the data-quality-w-greatexpectations folder
./setup.sh
```

## Run ETL

With the tables setup, you can run the ETL with the following command:

```bash
# in the data-quality-w-greatexpectations folder
python ecommerce/ecommerce/dim_customer_etl.py
```

This will run the ETL along with the **[greatexpectations validations](./ecommerce/ecommerce/gx/expectations/)**.

## Test ETL output

You can check that the ETL output is present with the following command.

```bash
sqlite3 ecommerce.db < ./setup/3-check-count.sql 
```

The above query should return

```text
110
110
27
```

## Validation results

The results of the validations will be stored in the `./ecommerce/ecommerce/gx/uncommitted/validations/dim_customer_dt_created_count/__none__`.

Since the `uncommitted` folder is not included in the git repo, you will need to run the ETL atleast once for this folder to appear.

