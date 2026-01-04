----------------------------Overview--------------------------------
This part of the project focuses on building a data warehouse for FlexiMart to analyze historical sales patterns. A star schema design is used to support fast analytical queries and reporting for business decision-making. 

---------------------------Star Schema Design-------------------------
The data warehouse follows a star schema with:

Fact Table -> fact_sales - which Stores measurable sales data (quantity, revenue, discounts)

Dimension Tables -> 
        a. dim_date – Time-based analysis (day, month, quarter, year)
        b. dim_product – Product details (category, subcategory, price)
        c. dim_customer – Customer attributes (city, state, segment)

The schema design is documented in detail in: star_schema_design.md

---------------------------Analytical Queries--------------------------

Query 1: Monthly Sales Drill-Down
            a.Shows sales broken down by Year → Quarter → Month
            b.Demonstrates drill-down capability using the date dimension

Query 2: Product Performance Analysis
            a. Identifies top 10 products by revenue
            b. Calculates revenue contribution percentage
            c. Helps product managers understand top-performing products

Query 3: Customer Segmentation Analysis
            a. Segments customers into High, Medium, and Low Value
            b. Shows customer count and revenue per segment
            c. Supports targeted marketing strategies

All queries are stored in file: analytics_queries.sql

-----------------------------How to Run--------------------------------

Step 1: Open MySQL Workbench
Step 2: Create Database -> 
            Create Database fleximart_dw;
            Use fleximart_dw;
Step 3: Run ->
            warehouse_schema.sql
            warehouse_data.sql
Step 4: Execute queries from -> analytics_queries.sql