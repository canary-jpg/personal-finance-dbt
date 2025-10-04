WITH date_spine AS (
    {{ dbt_utils.date_spine(
        datepart="day",
        start_date="cast('2024-04-01' as date)",
        end_date="cast(current_date() as date)"
    ) }}
),

daily_spending AS (
    SELECT 
        transaction_date,
        SUM(CASE WHEN transaction_type = 'expense' THEN ABS(amount) ELSE 0 END) as daily_total
    FROM {{ ref('stg_transactions') }}
    WHERE transaction_type = 'expense'
    GROUP BY 1
)

SELECT 
    date_spine.date_day,
    COALESCE(daily_spending.daily_total, 0) as total_spent
FROM date_spine
LEFT JOIN daily_spending
    ON date_spine.date_day = daily_spending.transaction_date
ORDER BY date_spine.date_day DESC 