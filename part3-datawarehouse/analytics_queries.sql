------------ Query 1: Monthly Sales Drill-Down-----------
-- Business Scenario: [Copy scenario]
-- Demonstrates: Drill-down from Year to Quarter to Month

SELECT
    d.year AS year,
    d.quarter AS quarter,
    d.month_name AS month_name,
    SUM(f.total_amount) AS total_sales,
    SUM(f.quantity_sold) AS total_quantity
FROM fact_sales f
JOIN dim_date d
    ON f.date_key = d.date_key
WHERE d.year = 2024
GROUP BY
    d.year,
    d.quarter,
    d.month,
    d.month_name
ORDER BY
    d.year,
    d.quarter,
    d.month;


------------ Query 2: Top 10 Products by Revenue-----------
-- Business Scenario: [Copy scenario]
-- Includes: Revenue percentage calculation

SELECT
    p.product_name,
    p.category,
    SUM(f.quantity_sold) AS units_sold,
    SUM(f.total_amount) AS revenue,
    ROUND(
        (SUM(f.total_amount) / SUM(SUM(f.total_amount)) OVER ()) * 100,
        2
    ) AS revenue_percentage
FROM fact_sales f
JOIN dim_product p
    ON f.product_key = p.product_key
GROUP BY
    p.product_key,
    p.product_name,
    p.category
ORDER BY
    revenue DESC
LIMIT 10;


------------ Query 3: Customer Segmentation Analysis----------------
-- Business Scenario: [Copy scenario]
-- Segments: High/Medium/Low value customers

WITH customer_spend AS (
    SELECT
        c.customer_key,
        c.customer_name,
        SUM(f.total_amount) AS total_spent
    FROM fact_sales f
    JOIN dim_customer c
        ON f.customer_key = c.customer_key
    GROUP BY
        c.customer_key,
        c.customer_name
),
segmented AS (
    SELECT
        customer_key,
        total_spent,
        CASE
            WHEN total_spent > 50000 THEN 'High Value'
            WHEN total_spent BETWEEN 20000 AND 50000 THEN 'Medium Value'
            ELSE 'Low Value'
        END AS customer_segment
    FROM customer_spend
)
SELECT
    customer_segment,
    COUNT(*) AS customer_count,
    SUM(total_spent) AS total_revenue,
    ROUND(AVG(total_spent), 2) AS avg_revenue_per_customer
FROM segmented
GROUP BY customer_segment
ORDER BY
    CASE customer_segment
        WHEN 'High Value' THEN 1
        WHEN 'Medium Value' THEN 2
        ELSE 3
    END;


