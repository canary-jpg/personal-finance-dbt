SELECT
    month,
    total_expenses,
    total_income
FROM {{ ref('monthly_financial_summary') }}
WHERE total_expenses > (total_income * 3)