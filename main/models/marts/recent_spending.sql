SELECT
    transaction_date,
    category,
    SUM(ABS(amount)) as total_spent
FROM {{ ref('stg_transactions') }}
WHERE {{ last_n_days(30) }}
    AND transaction_type = 'expense'
GROUP BY 1, 2
ORDER BY 1 DESC