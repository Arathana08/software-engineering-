from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "change-this-secret-key"

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS resources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        location TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        resource_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        location TEXT NOT NULL,
        priority TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'Pending',
        FOREIGN KEY(user_id) REFERENCES users(id)
    );
    """)
    existing = conn.execute("SELECT id FROM users WHERE email=?", ("admin@example.com",)).fetchone()
    if not existing:
        conn.execute(
            "INSERT INTO users (name,email,password) VALUES (?,?,?)",
            ("Admin", "admin@example.com", generate_password_hash("admin123"))
        )
    conn.commit()
    conn.close()

@app.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return render_template("index.html")

@app.post("/login")
def login():
    email = request.form["email"].strip()
    password = request.form["password"]
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
    conn.close()

    if user and check_password_hash(user["password"], password):
        session["user_id"] = user["id"]
        session["user_name"] = user["name"]
        return redirect(url_for("dashboard"))

    flash("Invalid email or password.", "error")
    return redirect(url_for("index"))

@app.get("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("index"))

    conn = get_db()
    requests = conn.execute("""
        SELECT requests.*, users.name AS user_name
        FROM requests JOIN users ON requests.user_id = users.id
        ORDER BY requests.id DESC
    """).fetchall()
    resources = conn.execute("SELECT * FROM resources ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("dashboard.html", requests=requests, resources=resources)

@app.post("/request-resource")
def request_resource():
    if "user_id" not in session:
        return redirect(url_for("index"))

    resource_name = request.form["resource_name"].strip()
    quantity = int(request.form["quantity"])
    location = request.form["location"].strip()
    priority = request.form["priority"]

    conn = get_db()
    conn.execute("""
        INSERT INTO requests (user_id, resource_name, quantity, location, priority)
        VALUES (?, ?, ?, ?, ?)
    """, (session["user_id"], resource_name, quantity, location, priority))
    conn.commit()
    conn.close()
    flash("Resource request submitted successfully.", "success")
    return redirect(url_for("dashboard"))

@app.post("/add-resource")
def add_resource():
    if "user_id" not in session:
        return redirect(url_for("index"))

    name = request.form["name"].strip()
    quantity = int(request.form["quantity"])
    location = request.form["location"].strip()

    conn = get_db()
    conn.execute(
        "INSERT INTO resources (name, quantity, location) VALUES (?, ?, ?)",
        (name, quantity, location)
    )
    conn.commit()
    conn.close()
    flash("Resource added successfully.", "success")
    return redirect(url_for("dashboard"))

@app.post("/request/<int:request_id>/status")
def update_status(request_id):
    if "user_id" not in session:
        return redirect(url_for("index"))

    status = request.form["status"]
    allowed = {"Pending", "Approved", "Completed"}
    if status not in allowed:
        return jsonify({"error": "Invalid status"}), 400

    conn = get_db()
    conn.execute("UPDATE requests SET status=? WHERE id=?", (status, request_id))
    conn.commit()
    conn.close()
    return redirect(url_for("dashboard"))

@app.get("/api/requests")
def api_requests():
    if "user_id" not in session:
        return jsonify({"error": "Unauthorized"}), 401

    conn = get_db()
    rows = conn.execute("SELECT * FROM requests ORDER BY id DESC").fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
