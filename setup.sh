#!/bin/bash

rm -rf ecommerce.db
sqlite3 ecommerce.db < ./setup/1-create-tables.sql
sqlite3 ecommerce.db < ./setup/2-populate-raw-tables.sql

