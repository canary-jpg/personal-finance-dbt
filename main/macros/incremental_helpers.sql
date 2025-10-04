{% macro get_incremental_filter(
    date_column='transaction_date',
    lookback_days=7
) %}

{% if is_incremental() %}
    -- Snowflake-compatible approach: reference in WHERE with simple logic
    AND {{ date_column }} >= DATEADD(day, -{{ lookback_days }}, CURRENT_DATE())
{% endif %}

{% endmacro %}
