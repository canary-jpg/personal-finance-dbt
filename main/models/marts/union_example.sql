{{ dbt_utils.union_relations(
    relations=[
        ref('stg_transactions')
    ]
) }}