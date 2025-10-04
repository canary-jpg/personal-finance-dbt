{% macro calculate_z_score(value_column, partition_by=none) %}
    ({{ value_column }} - AVG({{ value_column }}) OVER (
        {% if partition_by %}
        PARTITION BY {{ partition_by }}
        {% endif %}
    )) / NULLIF(STDDEV({{ value_column }}) OVER (
        {% if partition_by %}
        PARTITION BY {{ partition_by }}
        {% endif %}
    ), 0)
{% endmacro %}

{% macro flag_anomaly(z_score_column) %}
    CASE
        WHEN ABS({{ z_score_column }}) > 2 THEN 'HIGH ANOMALY'
        WHEN ABS({{ z_score_column }}) > 1.5 THEN 'MODERATE ANOMALY'
        WHEN {{ z_score_column }} > 1 THEN 'SLIGHTLY HIGH'
        WHEN {{ z_score_column }} < -1 THEN 'SLIGHTLY LOW'
        ELSE 'NORMAL'
    END
{% endmacro %}