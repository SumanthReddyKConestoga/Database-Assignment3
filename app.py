import os
from flask import Flask, render_template, request, redirect
import mysql.connector
from dotenv import load_dotenv

# ————— Load environment variables —————
load_dotenv()

app = Flask(__name__)


def get_db_conn():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASS", ""),
        database=os.getenv("DB_NAME", "usersdb")
    )


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (username, password) VALUES (%s,%s)",
            (u, p)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect("/success")
    return render_template("login.html")


@app.route("/success")
def success():
    return "✅ User recorded – database updated."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
