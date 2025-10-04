{% macro get_incremental_filter(
    date_column='transaction_date',
    lookback_days=7
) %}

{% if is_incremental() %}
    AND {{ date_column }} >= (
        SELECT DATEADD(day, -{{ lookback_days }}, MAX({{ date_column }}))
        FROM {{ this }}
    )
{% endif %}

{% endmacro %}


{% macro get_merge_sql(unique_key, update_columns=[]) %}
    {{
        config(
            materialized='incremental',
            unique_key=unique_key,
            merge_update_columns=update_columns
        )
    }}
{% endmacro %}