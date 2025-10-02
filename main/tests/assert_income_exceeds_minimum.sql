SELECT
    month,
    total_income
FROM {{ ref('monthly_financial_summary') }}
WHERE total_income < 1000