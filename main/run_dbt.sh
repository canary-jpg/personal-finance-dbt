#!/bin/bash

cd ~/personal_finance_analytics

dbt run

dbt test

echo "dbt run completed at $(date)"
