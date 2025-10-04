WITH daily_totals AS (
    SELECT
        transaction_date,
        category,
        SUM(ABS(amount)) as daily_total
    FROM {{ ref('stg_transactions') }}
    WHERE transaction_type = 'expense'
    GROUP BY 1, 2
)

SELECT 
    transaction_date,
    category,
    daily_total,
    {{ calculate_z_score('daily_total', partition_by='category') }} as z_score,
    {{ flag_anomaly('z_score') }} as anomaly_flag
FROM daily_totals
ORDER BY ABS(z_score) DESC