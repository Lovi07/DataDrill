import os
import sqlite3
from nlp_rules import parse_to_sql

def run_query(nl_query: str):
    try:
        sql = parse_to_sql(nl_query)

        # Build absolute path to the DB
        base_dir = os.path.dirname(os.path.abspath(__file__))  # root of project
        db_path = os.path.join(base_dir, "data", "sample_sales.db")

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(sql)
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        conn.close()
        return {"sql": sql, "columns": columns, "rows": rows}
    except Exception as e:
        return {"error": str(e)}
