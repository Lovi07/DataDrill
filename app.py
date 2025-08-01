import streamlit as st
import pandas as pd
import plotly.express as px
import requests

st.set_page_config(page_title="DataDrill", layout="wide")
st.title("📊 DataDrill: Ask Your Data with Natural Language")

# Input box for the natural language query
query = st.text_input("Type your question (e.g. 'Total sales by product')")

if st.button("Run Query") and query:
    with st.spinner("Querying your data..."):
        try:
            # Call the Flask API
            response = requests.post(
                "http://localhost:5000/query",
                headers={"Content-Type": "application/json"},
                json={"text": query}
            )

            if response.status_code != 200:
                st.error(f"API Error {response.status_code}: {response.text}")
            else:
                data = response.json()

                # Show SQL query generated
                st.subheader("🔍 SQL Generated:")
                st.code(data["sql"], language="sql")

                # Show result in table
                df = pd.DataFrame(data["rows"], columns=data["columns"])
                st.dataframe(df)

                # Show chart if applicable
                if "total" in query.lower() and df.shape[1] >= 2:
                    try:
                        x = df.columns[0]
                        y = df.columns[1]
                        fig = px.bar(df, x=x, y=y, title=f"{y} by {x}")
                        st.plotly_chart(fig, use_container_width=True)
                    except Exception as e:
                        st.warning("⚠️ Chart could not be rendered: " + str(e))

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Failed to connect to API: {e}")
