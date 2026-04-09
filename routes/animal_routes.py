from flask import Blueprint, request
from auth.decorators import auth_required, verify_permissions
from services.animal_service import AnimalService

animal_bp = Blueprint ("animal_bp", __name__)

@animal_bp.route ("/animal", methods=["POST"])
@auth_required

def criar():
    data = request.json
    animal = AnimalService.create_animal(data)
    return {"id":animal.id_animal, "nome":animal.nome}, 201

@animal_bp.route ("/animal", methods=["GET"])


def listar():
    animal = AnimalService.list_animais()
    return [
        {"id":a.id_animal, "nome":a.nome,"especie": a.especie, "raça": a.raca, "sexo": a.sexo, "Nascimento":a.data_nascimento}
        for a in animal
    ]

@animal_bp.route("/animal/<int:animal_id>", methods=["GET"])
def obter(animal_id):
    animal = AnimalService.get_animal(animal_id)
    if not animal:
        return {"erro": "Animal não encontrado"}, 404
    return {"id":animal.id_animal, "nome":animal.nome, "especie":animal.especie, "raça":animal.raca, "sexo":animal.sexo, "Nascimento":animal.data_nascimento}


@animal_bp.route("/animal/<int:animal_id>", methods=["PUT"])
def atualizar (animal_id):
    data = request.json
    animal = AnimalService.update_animal(animal_id, data)
    if not animal:
        return {"erro": "Animal não encontrado"}, 404
    
    return {"id": animal.id_animal, "nome": animal.nome, "especie":animal.especie, "raça":animal.raca, "sexo":animal.sexo, "Nascimento":animal.data_nascimento}

@animal_bp.route("/animal/<int:animal_id>", methods=["DELETE"])
@verify_permissions(2)
#@auth_required
def deletar(animal_id):
    ok =AnimalService.delete_animal(animal_id)
    if not ok:
        return {"erro":"Animal não encontrado"}, 404
    return {"mensagem": "Animal removido com sucesso"}
