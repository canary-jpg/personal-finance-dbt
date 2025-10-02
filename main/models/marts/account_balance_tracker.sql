WITH daily_transactions AS (
    SELECT
        transaction_date,
        account_type,
        transaction_id,
        description,
        amount,
        transaction_type
    FROM {{ ref('stg_transactions') }}
),
running_balances AS (
    SELECT
        transaction_date,
        account_type,
        transaction_id,
        description,
        amount,
        transaction_type,
        SUM(amount) OVER (
            PARTITION BY account_type
            ORDER BY transaction_date, transaction_id
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) as balance,
        SUM(amount) OVER (
            PARTITION BY account_type, DATE_TRUNC('month', transaction_date)
        ) as monthly_net_change
    FROM daily_transactions
)

SELECT
    transaction_date,
    account_type,
    transaction_id,
    description,
    amount,
    transaction_type,
    balance,
    monthly_net_change,
    balance - amount as previous_balance
FROM running_balances
ORDER BY account_type, transaction_date, transaction_id