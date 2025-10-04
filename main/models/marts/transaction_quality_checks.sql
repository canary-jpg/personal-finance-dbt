SELECT
    transaction_id,
    transaction_date,
    description,
    amount,
    category,
    {{ dbt_utils.generate_surrogate_key(['transaction_id', 'transaction_date']) }} as surrogate_key,
    date_trunc('week', transaction_date) as week_start,
    
FROM {{ ref('stg_transactions') }}