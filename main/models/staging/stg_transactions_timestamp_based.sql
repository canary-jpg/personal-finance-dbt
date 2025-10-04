{{
    config(
        materialized='incremental',
        unique_key='transaction_id'
    )
}}

WITH source_data AS (
    SELECT
        transaction_id,
        date::DATE as transaction_date,
        TRIM(description) as description,
        amount,
        TRIM(category) as category,
        TRIM(account_type) as account_type,
        CURRENT_TIMESTAMP() as loaded_at
    FROM {{ source('raw', 'raw_transactions') }}
)

SELECT
    transaction_id,
    transaction_date,
    description,
    amount,
    category,
    account_type,
    CASE
        WHEN amount > 0 THEN 'income'
        ELSE 'expense'
    END as transaction_type,
    loaded_at
FROM source_data

{% if is_incremental() %}
    WHERE loaded_at > (SELECT MAX(loaded_at) FROM {{ this }})
{% endif %}