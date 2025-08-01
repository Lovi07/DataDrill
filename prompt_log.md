Prompt: "Show total sales by product"
→ SQL: SELECT product, SUM(revenue) as total_revenue FROM sales GROUP BY product

Prompt: "Show total quantity by region"
→ SQL: SELECT region, SUM(quantity) as total_quantity FROM sales GROUP BY region