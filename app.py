from flask import Flask, render_template
import pyodbc
import os

app = Flask(__name__)

# Get connection string from environment variable
conn_str = os.environ.get("AZURE_SQL_CONN")

@app.route('/')
def home():
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT TOP 1 message FROM welcome")
        row = cursor.fetchone()
        message = row[0] if row else "Welcome!"
        conn.close()
    except Exception as e:
        message = f"DB Error: {e}"

    return render_template("index.html", message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
