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
    END as transaction_type
FROM {{ source('raw', 'raw_transactions') }}
