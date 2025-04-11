# Student Database Dashboard

This project is a **Streamlit** app integrated with **Google Gemini AI** that allows users to ask natural language questions about a student database, and automatically generates and executes the corresponding **SQL queries** on a SQLite database.

## Features

- **Natural Language to SQL**: Converts user questions in natural language to valid SQL queries.
- **SQLite Database**: Executes the generated SQL queries on an SQLite database and displays the results.
- **Google Gemini AI**: Uses Google's Gemini AI to generate SQL queries based on a given schema.
- **Interactive UI**: Built with Streamlit for easy interaction and displaying results.

## Prerequisites

Before running this app, make sure you have the following:

- Python 3.7+ installed.
- A **Google API Key** for **Gemini AI** (to be saved in a `.env` file).
- An **SQLite database** (`student.db`) with a `STUDENT` table containing the following columns:
  - `NAME` (TEXT)
  - `CLASS` (TEXT)
  - `SECTION` (TEXT)
  - `MARKS` (INTEGER)

## Installation

1. Clone this repository or download the source code to your local machine.
   
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
