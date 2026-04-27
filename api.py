from flask import Flask, Response
import json

app = Flask(__name__)

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
