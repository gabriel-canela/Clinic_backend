from config.database import SessionLocal
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

class AuthService:

    @staticmethod
    def register(data):
        session = SessionLocal()
        user = User(
            email = data ["email"],
            password_hash = generate_password_hash(data["password"]),
            user_type = data ["user_type"]
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        session.close()
        return user
    
    @staticmethod
    def login (data):
        session = SessionLocal()
        user = session.query(User).filter(User.email == data["email"]).first()

        if not user:
            session.close()
            return None
        
        if not check_password_hash(user.password_hash, data["password"]):
            session.close()
            return None
        
        user.token = secrets.token_hex(32)
        session.commit()
        session.refresh(user)
        session.close()
        return user
    
    @staticmethod
    def get_user_by_token(token):
        session = SessionLocal()
        user = session.query(User).filter(User.token == token).first()
        session.close()
        return user