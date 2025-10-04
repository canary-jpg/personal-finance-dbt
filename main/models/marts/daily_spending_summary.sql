{{
    config(
        materialized='incremental',
        unique_key='summary_date',
        incremental_strategy='delete+insert'
    )
}}

SELECT
    transaction_date as summary_date,
    COUNT(*) as transaction_count,
    SUM(CASE WHEN transaction_type = 'expense' THEN ABS(amount) ELSE 0 END) as total_expenses,
    SUM(CASE WHEN transaction_type = 'income' THEN amount ELSE 0 END) as total_income,
    COUNT(DISTINCT category) as categories_used
FROM {{ ref('stg_transactions') }}

WHERE 1=1
{{ get_incremental_filter(date_column='transaction_date', lookback_days=14) }}

GROUP BY 1
ORDER BY 1 DESC