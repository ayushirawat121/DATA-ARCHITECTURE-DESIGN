---------------Star Schema Design – FlexiMart Data Warehouse----------------------

---------------Section 1: Schema Overview------------------------

FlexiMart requires a star schema to analyze historical sales patterns efficiently. The design uses a central fact table that stores measurable sales metrics.
--------------
#FACT TABLE: fact_sales

Grain: One row per product per order line item
Business Process: Sales transactions.

Measures (Numeric Facts): 
-quantity_sold: Number of units sold for a product in an order line
-unit_price: Price per unit at the time of sale
-discount_amount: Discount applied on that line item (default 0 if not applicable)
- total_amount: Final amount after discount (quantity_sold × unit_price − discount_amount)

Foreign Keys in fact_sales:
- date_key → dim_date
- product_key → dim_product
- customer_key → dim_customer

--------------

#DIMENSION TABLE: dim_date

Purpose: Date dimension for time-based analysis as trends by month, quarter, year, and weekday  
Type: Conformed dimension

Attributes:**
- date_key (PK): Surrogate key
- full_date: Actual calendar date
- day_of_week: Monday, Tuesday, etc.
- day_of_month: Numeric day (1–31)
- month: Numeric month (1–12)
- month_name: January, February, etc.
- quarter: Q1, Q2, Q3, Q4
- year: Year value (e.g., 2023, 2024)
- is_weekend: Boolean (TRUE if satuday/sunday, otherwise FALSE)

--------------

#DIMENSION TABLE: dim_product

Purpose: Stores descriptive information about products by category, brand, and pricing.  
Type: Descriptive dimension.

Attributes:**
- **product_key (PK):** Surrogate key (auto-increment integer)
- **product_id:** Business/natural key from source system (e.g., P001)
- **product_name:** Name of the product
- **category:** High-level category (e.g., Electronics, Fashion, Groceries)
- **subcategory:** More detailed classification (e.g., Smartphones, Laptops, Footwear)
- **unit_price:** Standard/base unit price for reference in analysis

--------------

#DIMENSION TABLE: dim_customer

Purpose: Stores customer-related information for segmentation and geographic reporting.  
Type: Descriptive dimension.

Attributes:
- customer_key (PK): Surrogate key
- customer_id: Business/natural key from source system (e.g., C001)
- customer_name: Full name of the customer (first_name + last_name)
- city: City where the customer resides
- state: State/region (if not available in source, can be stored as NULL)
- customer_segment: Segment classification (e.g., Regular, Premium, Corporate)

--------------

The design improves query performance and simplifies BI reporting compared to normalized transactional schemas.

---------------------------------Section 2: Design Decision-----------------------

The fact table is designed at the transaction line-item level, meaning each row represents a single product purchased in an order. This granularity was chosen because it provides the highest level of detail, allowing accurate analysis of product-level sales, quantities, discounts, and revenue. From this detailed level, data can always be aggregated to higher levels such as order, daily, monthly, or yearly sales, but the reverse is not possible if lower granularity is lost.

Surrogate keys are used instead of natural keys to improve performance and maintain data consistency. Natural keys such as product IDs or customer IDs may change in source systems or may be reused, whereas surrogate keys are system-generated, stable, and efficient for joins in a data warehouse environment.

This star schema design supports drill-down and roll-up operations effectively. Analysts can roll up data from day to month or year using the date dimension and drill down from category to subcategory or individual products using the product dimension, enabling flexible and efficient analytical reporting.

-----------------------Section 3: Sample Data Flow----------------------------------------

In the source system, the transaction is stored across multiple normalized tables such as orders, order_items, customers, and products.

Transformation and Key Lookup : 
        During the ETL process:-
          a. The order date is mapped to the date dimension and assigned a surrogate key.
          b. The product and customer business keys are looked up in their respective dimension tables to retrieve surrogate keys.
          c. Measures such as quantity and total amount are calculated.

Data Warehouse representation:
    fact_sales table:            
                {
                    "date_key": 20240115,
                    "product_key": 5,
                    "customer_key": 12,
                    "quantity_sold": 2,
                    "unit_price": 50000,
                    "discount_amount": 0,
                    "total_amount": 100000
                }

    dim_date table:
                {
                    "date_key": 20240115,
                    "full_date": "2024-01-15",
                    "day_of_week": "Monday",
                    "month": 1,
                    "month_name": "January",
                    "quarter": "Q1",
                    "year": 2024,
                    "is_weekend": false
                }

    dim_product table:
                {
                `    "product_key": 5,
                    "product_name": "Laptop",
                    "category": "Electronics",
                    "subcategory": "Laptops",
                    "unit_price": 50000`
                }

    dim_customer table: 
                {
                    "customer_key": 12,
                    "customer_name": "John Doe",
                    "city": "Mumbai",
                    "customer_segment": "Regular"
                }

#Summary - This example shows how detailed transactional data is transformed into a structured analytical format. The fact table captures measurable sales data, while dimension tables provide descriptive context, enabling efficient reporting and analysis.


