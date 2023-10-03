import argparse
import openai
import json

from query import select_from_table
from schema import get_schema
from db import create_connection

DATABASE = "./pythonsqlite.db"

def main(conn, question):
    # Load your API key from an environment variable or secret management service
    # openai.api_key = os.getenv(auth['api_key'])
    openai.api_key = ""
    print(f"Question: {question}")

    prompt = f"""
    
    Given the following SQL Schema:{get_schema()}
    Write a SQL query to answer this question: {question}
    Keep in mind that our SQL version is SQL Lite.
    Queries may only use columns and tables within the database unless they are being created.
    Instead of drop or delete statements, replace it with a select all statement.
    An ok solution to complex queries is creating a new and needed table or column. 
    """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=200
    )


    q = response["choices"][0]["text"]

    print(f"AI-generated SQL query: \n{q}")
    print("Answer: \n")
    select_from_table(conn, q)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, default="natural language query")
    args = parser.parse_args()
    conn = create_connection(DATABASE)

    main(conn, question=args.query)

