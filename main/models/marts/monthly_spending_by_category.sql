SELECT
    DATE_TRUNC('month', transaction_date) as month,
    category,
    account_type,
    COUNT(*) as transaction_count,
    SUM(CASE WHEN transaction_type = 'expense' THEN ABS(amount) ELSE 0 END) as total_spent,
    AVG(CASE WHEN transaction_type = 'expense' THEN ABS(amount) ELSE 0 END) as avg_transaction_amount
FROM {{ ref('stg_transactions') }}
WHERE transaction_type = 'expense'
GROUP BY 1, 2, 3
ORDER BY 1 DESC, 5 DESC