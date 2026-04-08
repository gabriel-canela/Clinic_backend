from flask import Blueprint, request
from services.tutor_service import TutorService


tutor_bp = Blueprint("tutor_bp", __name__)

@tutor_bp.route("/tutor", methods=["POST"])

def criar():
    data = request.json
    tutor = TutorService.create_tutor(data)
    return {"id":tutor.id_tutor, "nome":tutor.nome}, 201

@tutor_bp.route("/tutor", methods=["GET"])
def listar():
    tutor = TutorService.list_tutores()
    return [
        {"id": t.id, "nome": t.nome, "telefone": t.telefone, "email":t.email}
        for t in tutor
    ]

@tutor_bp.route("/tutor/<int:tutor_id>", methods=["GET"])
def obter(tutor_id):
    tutor = TutorService.get_tutor(tutor_id)
    if not tutor:
        return {"erro":"Tutor não encontrado"}, 404
    
    return {"id":tutor.id, "nome": tutor.nome, "telefone":tutor.telefone, "email": tutor.email}


@tutor_bp.route("/tutor/<int:tutor_id>", methods=["PUT"])
def atualizar(tutor_id):
    data = request.json
    tutor = TutorService.update_tutor(tutor_id, data)
    if not tutor:
        return {"erro": "Tutor não encontrado"},404
    
    return {"id": tutor.id, "nome": tutor.nome, "telefone": tutor.telefone, "email": tutor.email}
    

@tutor_bp.route("/tutor/<int:tutor_id>", methods=["DELETE"])
def deletar(tutor_id):
    ok = TutorService.delete_tutor(tutor_id)
    if not ok:
        return {"Erro": "Tutor não encontrado"}, 404
    return {"mensagem": "Tutor removido com sucesso"}
