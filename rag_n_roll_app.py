import streamlit as st
import requests
from snowflake.snowpark import Session

# Snowflake session configuration
SNOWFLAKE_CONFIG = {
    "account": "<your_account>",
    "user": "<your_username>",
    "password": "<your_password>",
    "role": "<your_role>",
    "warehouse": "<your_warehouse>",
    "database": "<your_database>",
    "schema": "<your_schema>",
}

# Cortex Search API configuration
CORTEX_SEARCH_ENDPOINT = "<your_cortex_search_endpoint>"
CORTEX_API_KEY = "<your_cortex_api_key>"

# Query Cortex Search
def query_cortex_search(user_query, top_k=5):
    headers = {"Authorization": f"Bearer {CORTEX_API_KEY}"}
    payload = {"query": user_query, "size": top_k}
    response = requests.post(CORTEX_SEARCH_ENDPOINT, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()["results"]
    else:
        st.error("Error querying Cortex Search!")
        return []

# Generate response with Mistral LLM
def generate_with_mistral(prompt):
    session = Session.builder.configs(SNOWFLAKE_CONFIG).create()
    query = f"""
        CALL MISTRAL_LARGE2_GENERATE(PROMPT => '{prompt}')
    """
    try:
        result = session.sql(query).collect()
        return result[0]["RESPONSE"]
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")
        return "Error generating response."

# Streamlit UI
st.title("RAG 'n' ROLL Assistant")
st.subheader("Smart Retrieval-Augmented Generation for Better Answers")

# User query input
user_query = st.text_input("Enter your query here:")
if user_query:
    st.write("**Retrieving relevant documents...**")
    retrieved_docs = query_cortex_search(user_query)
    
    if retrieved_docs:
        st.write("### Retrieved Documents:")
        for i, doc in enumerate(retrieved_docs, 1):
            st.write(f"**Document {i}:** {doc['content']}")
        
        # Prepare prompt for Mistral LLM
        st.write("**Generating response...**")
        context = "\n".join([doc["content"] for doc in retrieved_docs])
        prompt = f"Using the following documents:\n{context}\nAnswer the query: {user_query}"
        
        # Generate response
        response = generate_with_mistral(prompt)
        st.write("### Generated Response:")
        st.write(response)
    else:
        st.error("No relevant documents found.")

# Footer
st.markdown("---")
st.caption("Built with Cortex Search, Mistral LLM, and Streamlit.")
