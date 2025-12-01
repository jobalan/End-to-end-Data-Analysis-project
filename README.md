**E-commerce Sales Performance & Profitability Dashboard: A Star Schema Analysis**

**Project Summary**
This project demonstrates an end-to-end data engineering and analytics pipeline, transforming raw e-commerce sales data into a structured Star Schema Data Warehouse using Python and SQL Server. The final model is used to generate critical business insights and visualizations in Power BI, providing a complete view of sales performance, profitability, and customer segmentation.

**Role	Technology	Key Techniques Demonstrated**
ETL & Transformation	Python (Pandas, NumPy)	Data merging, cleaning, feature engineering (calculating Profit, Net Sales).
Data Warehousing	Microsoft SQL Server	Star Schema design, robust data typing (INT, NVARCHAR(100)), Data Population Logic.
Advanced Analytics	SQL Window Functions (CTE, RANK())	Top N per Group Analysis, Aggregation Filtering (HAVING).
Business Intelligence	Power BI (DAX)

**Phase 1: Python ETL Pipeline (01_main_etl_script.py)**
The Python script is the backbone of the project, responsible for integrating and enriching the source data from four separate CSV files (users, products, orders, order_items).

Key Technical Aspects:
Data Integration: Merged all four source files into a single, comprehensive transactional table.

Feature Engineering: Calculated three essential business metrics required for the data warehouse:

Net Sales: Gross Sales * (1 - Discount)

COGS (Cost of Goods Sold): Quantity * Cost

Profit: Net Sales - COGS

Output: Generates the final, clean cleaned_sales_data.csv file, ready for loading into SQL Server.

**Phase 2: SQL Data Warehouse (Star Schema)**
The 02_sql_data_warehouse.sql script defines and populates the analytical environment, creating a highly efficient Star Schema.

1. Robust Schema Design
Created Fact_Sales (the central transactional table) linked to two dimension tables, Dim_Customer and Dim_Product.

Error Handling (Critical Fixes): Used the CREATE TABLE script to manually define robust data types, specifically:

INT for all ID columns (order_id, product_id) to prevent tinyint conversion errors.

NVARCHAR(100) for text columns (country, category) to prevent truncation errors (e.g., handling long country names like 'British Indian Ocean Territory').

**Phase 3: Power BI Dashboard**
The final dashboard visualizes the SQL insights, prioritizing clarity and interactivity.

1. Key Metrics & DAX
Core KPIs: Prominently displays Total Net Sales, Total Profit, and Average Order Value (AOV) using custom DAX measures.

Time Intelligence: Utilizes DAX functions (e.g., DATEADD) to create measures like Sales Last Month and Month-over-Month (MoM) Growth.

2. Data Storytelling (Visuals)
Clear Trend Analysis: The primary visual is a Line Chart showing Monthly Sales Trend, which is the professional standard for time-series analysis.

Segmentation Insight: The Donut Chart breaks down sales by Customer Segment (addressing the LTV analysis).

Geographic & Category Focus: Bar Charts are used to clearly compare Sales by Country and Category, replacing less effective Pie Charts to ensure accurate data comparison.

Interactivity: Strategic Slicers (Date Range, Category, Segment) allow end-users to dynamically filter the entire report for quick, ad-hoc analysis.
