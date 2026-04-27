from flask import Flask, Response, request, jsonify
import sqlite3
import json

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXITS users(
            id int PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            apellido TEXT,
            telefono TEXT
        )               
    """)

    conn.commit()
    conn.close()
    
    
@app.route("/")
def get_user():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    
    conn.close()
    
    users = []

    for row in rows:
        users.append({
            "id": row[0],
            "nombre": row[1],
            "apellido": row[2],
            "telefono": row[3]
        })
    
    data = {
        "status": "success",
        "total": len(users),
        "data": {
            "users": users
        }
    }

    return Response(
        json.dumps(data, indent=2),
        mimetype='application/json'
    )
    
@app.route("/api/user", methods=["POST"])
def add_user():
    data = request.get_json()
    
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO users (nombre, apellido, telefono) VALUES (?, ?, ?)
    """,(
        data["nombre"],
        data["apellido"],
        data["telefono"]
    ))
    
    conn.commit()
    conn.close()
    
    return jsonify({
        "message": "Usuario Agregado correctamente"
    })
    