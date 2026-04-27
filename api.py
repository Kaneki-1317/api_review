from flask import Flask, Response, request, jsonify
import json

app = Flask(__name__)

users = []

@app.route("/")
def get_user():
    users = [
        {"nombre": "Cristian", "apellido": "Mayorga", "telefono": 3150606018},
        {"nombre": "Diego", "apellido": "Diaz", "telefono": 3150606018},
        {"nombre": "Dayana", "apellido": "Barbosa", "telefono": 3150606018},
        {"nombre": "Sara", "apellido": "Nuñez", "telefono": 3150606018}
    ]

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
    
    nombre = data["nombre"]
    apellido = data["apellido"]
    telefono = data["telefono"]
    
    users.append({
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono
    })
    
    return jsonify({
        "message": "Usuario Agregado correctamente",
        "User": users
    })
    