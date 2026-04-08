from flask import request, g
from functools import wraps
from services.auth_service import AuthService
from services.tutor_service import TutorService
from services.animal_service import AnimalService

def auth_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Token "):
            return {"erro": "Token ausente ou invalido"}, 401
        
        token = auth_header.split (" ") [1]
        user = AuthService.get_user_by_token(token)

        if not user:
            return {"erro": "Token invalido"}, 401
        
        g.current_user = user
        return f(*args, **kwargs)
    
    return wrapper
""" 
def adm_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Token "):
            return {"erro": "Token ausente ou inválido"}, 401
        
        token = auth_header.split (" ") [1]
        user = AuthService.get_user_by_token(token)

        if not user:
            return {"erro": "Token invalido"}, 401
        

        if user.user_type != 1:
            return {"erro":"Permissão de usuário insuficiente"}, 403
        
        g.current_user = user
        return f(*args, **kwargs)
    
    return wrapper

def vet_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Token "):
            return {"erro":"Token ausente ou invalido"}, 401
        
        token = auth_header.split (" ") [1]
        user = AuthService.get_user_by_token(token)

        if not user:
            return {"erro": "Token invalido"}, 401
        
        if user.user_type != 3:
            return {"erro": "Permissão de usuário insuficiente"}, 403
        
        g.current_user = user
        return f(*args, **kwargs)
    return wrapper
        
 """

def verify_permissions(*allowed_roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            auth_header = request.headers.get("Authorization")
            
            if not auth_header or not auth_header.startswith("Token "):
                return {"erro": "Token ausente ou invalido"}, 401
            
            
            token = auth_header.split (" ")[1]
            
            user = AuthService.get_user_by_token(token)

            if not user:
                return {"erro": "Token invalido"}, 401
            
            if user.user_type not in allowed_roles:
                return {"erro":"Usuário não autorizado"}
            
            if user.user_type == 2: #Validação do usuário cuja conta tutor está relacionada ao pet em questão
                tutor = TutorService.get_tutor_by_email(user.email)
                id_pet = request.args.get('id', type=int)
                pet = AnimalService.get_animal(id_pet)
                if pet:
                    if int(tutor.id_tutor) == (pet.id_tutor):
                        
                        print ("ID TUTOR SERVICE", tutor.id_tutor," DEU BOA ENTROU AQUI")
                        return {"erro":"Tutores podem editar apenas os próprios pets"}
               # return {"erro":"Pet não encontrado"}

            g.current_user = user
            return f(*args, **kwargs)
        return wrapper
    return decorator

  