{% macro last_n_days(n_days) %}
    transaction_date >= DATEADD(day, -{{ n_days }}, CURRENT_DATE())
{% endmacro %}

{% macro current_month() %}
    DATE_TRUNC('month', transaction_date) = DATE_TRUNC('month', CURRENT_DATE())
{% endmacro %}