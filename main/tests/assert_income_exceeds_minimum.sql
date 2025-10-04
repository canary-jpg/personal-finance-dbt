SELECT
    month,
    total_income
FROM {{ ref('monthly_financial_summary') }}
WHERE total_income < 500
  AND month < DATE_TRUNC('month', CURRENT_DATE())

