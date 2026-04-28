from flask import Flask, Response, request, jsonify
import mysql.connector
import json

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="switchback.proxy.rlwy.net",
        port=30358,
        user="root",
        password="GPVmHkVFvXjLgialsdTEBJjNQHhywMCG",
        database="railway"
    )
    
    
@app.route("/")
def get_user():
    conn = get_connection()
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
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO users (nombre, apellido, telefono) VALUES (%s, %s, %s)
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

