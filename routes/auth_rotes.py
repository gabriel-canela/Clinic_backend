from flask import Blueprint, request
from services.auth_service import AuthService

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/register",methods=["POST"])
def register():
    data = request.json
    user = AuthService.register(data)
    return {"id": user.id, "email": user.email, "user_type": user.user_type}, 201

@auth_bp.route("/login", methods = ["POST"])
def login():
    data = request.json
    user = AuthService.login (data)

    if not user:
        return {"erro":"Credenciais inválidas"}, 401 
    
    return {"token": user.token}