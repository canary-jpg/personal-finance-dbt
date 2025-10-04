SELECT
    month,
    total_expenses,
    total_income
FROM {{ ref('monthly_financial_summary') }}
WHERE total_expenses > (total_income * 5)
  AND month < DATE_TRUNC('month', CURRENT_DATE())
  AND total_income > 0
