# RAG 'n' ROLL Assistant

A smart Retrieval-Augmented Generation (RAG) application using:
- **Cortex Search** for document retrieval
- **Mistral LLM** on Snowflake Cortex for response generation
- **Streamlit Community Cloud** for the front-end interface

## Features
- Retrieve relevant documents using Cortex Search
- Generate context-aware answers with Mistral LLM
- Interactive and user-friendly web app built with Streamlit

## How It Works
1. Enter a query in the Streamlit interface.
2. Cortex Search retrieves the top relevant documents.
3. Mistral LLM processes the retrieved documents and generates a response.
4. The app displays both the retrieved documents and the generated response.

## Prerequisites
- Python 3.x installed
- API access for Cortex Search and Mistral LLM on Snowflake Cortex
- A dataset indexed in Cortex Search
- Required Python packages: `streamlit`, `requests`, `snowflake-snowpark-python`

## Installation
Clone this repository:
   
  - git clone https://github.com/sahasraa/RAG-n-ROLL-Assistant.git
  - cd rag-n-roll-assistant
