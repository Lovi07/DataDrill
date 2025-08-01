def parse_to_sql(nl_query: str) -> str:
    q = nl_query.lower()

    if "total sales" in q and "by product" in q:
        return "SELECT product, SUM(revenue) as total_revenue FROM sales GROUP BY product"
    elif "total quantity" in q and "by region" in q:
        return "SELECT region, SUM(quantity) as total_quantity FROM sales GROUP BY region"
    elif "all sales" in q:
        return "SELECT * FROM sales"
    else:
        raise ValueError("I don't understand this query yet.")
