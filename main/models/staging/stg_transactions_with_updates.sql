{{
    config(
        materialized='incremental',
        unique_key='transaction_id',
        merge_update_columns=['amount', 'description', 'category']
    )
}}

SELECT
    transaction_id,
    date::DATE as transaction_date,
    TRIM(description) as description,
    amount,
    TRIM(category) as category,
    TRIM(account_type) as account_type,
    CASE
        WHEN amount > 0 THEN 'income'
        ELSE 'expense'
    END as transaction_type,
    CURRENT_TIMESTAMP() AS dbt_updated_at
FROM {{ source('raw', 'raw_transactions') }}

{% if is_incremental() %}
    WHERE date::DATE >= (SELECT DATEADD(day, -7, MAX(transaction_date)) FROM {{ this }})
{% endif %}
