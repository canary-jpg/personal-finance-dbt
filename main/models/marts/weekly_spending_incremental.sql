{{
    config(
        materialized='incremental',
        unique_key='week_start_date',
        incremental_strategy='delete+insert'
    )
}}

SELECT
    DATE_TRUNC('week', transaction_date) as week_start_date,
    category,
    COUNT(*) as transaction_count,
    SUM(CASE WHEN transaction_type = 'expense' THEN ABS(amount) ELSE 0 END) as total_spent,
    AVG(CASE WHEN transaction_type = 'expense' THEN ABS(amount) ELSE 0 END) as avg_spent
FROM {{ ref('stg_transactions') }}
WHERE transaction_type = 'expense'

{% if is_incremental() %}
    AND transaction_date >= DATEADD(week, -2, CURRENT_DATE())
{% endif %}

GROUP BY 1, 2