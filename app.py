
import streamlit as st
import os
import sqlite3
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure your Gemini API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("API key not found. Please check your .env file.")
    st.stop()  # Stop execution if the API key is missing

genai.configure(api_key=api_key)

# Set up the Gemini model
try:
    model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Updated model name
except Exception as e:
    st.error(f"❌ Error setting up Gemini model: {e}")
    st.stop()

# Function to get Gemini-generated SQL response
def get_gemini_sql_response(question, prompt):
    full_prompt = prompt + "\nUser question: " + question
    try:
        response = model.generate_content(full_prompt)
        sql_query = response.text.strip()
        
        # Clean up the SQL query to remove markdown formatting
        sql_query = sql_query.replace("```sql", "").replace("```", "").strip()
        
        return sql_query
    except Exception as e:
        st.error(f"❌ Error while generating content: {e}")
        return ""

# Function to retrieve data from SQLite
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        return rows
    except Exception as e:
        st.error(f"❌ Error executing SQL query: {e}")
        return []

# Prompt for Gemini
prompt = """
You are a helpful assistant that converts user questions into valid SQL queries.
Use the following database schema to generate the SQL:

Table: STUDENT
Columns: NAME (TEXT), CLASS (TEXT), SECTION (TEXT), MARKS (INTEGER)

Examples:
- List names of students who scored above 80.
- Show average marks of all students.
- Get names from Data Science class.
"""

# Streamlit app
st.set_page_config(page_title="Gemini SQL Chatbot")
st.header("Ask Questions About Student Database")

# User input
question = st.text_input("Ask your question:", key="input")
submit = st.button("Get SQL Answer")

if submit and question:
    sql_query = get_gemini_sql_response(question, prompt)
    
    if sql_query:  # Only proceed if a valid SQL query was generated
        st.write("🧠 Gemini-generated SQL:")
        st.code(sql_query, language="sql")

        # Execute the SQL query
        data = read_sql_query(sql_query, "student.db")

        # Display results
        st.subheader("📊 Result:")
        if data:
            for row in data:
                st.write(row)
        else:
            st.write("No data found or error executing SQL.")
    else:
        st.error("Failed to generate a valid SQL query.")
