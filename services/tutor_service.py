from config.database import SessionLocal
from models.tutor import Tutor

class TutorService:

    @staticmethod
    def create_tutor(data):
         
        session = SessionLocal()
        tutor = Tutor(**data)
        session.add(tutor)
        session.commit()
        session.refresh(tutor)
        session.close()
        return tutor


    @staticmethod
    def list_tutores():
        pass

    @staticmethod
    def get_tutor_by_email(email):
        session = SessionLocal()
        tutor = session.query(Tutor).filter(Tutor.email == email).first()
        session.close()
        return tutor

    @staticmethod
    def update_tutor(tutor_id, data):
        pass
    
    @staticmethod
    def delete_tutor(tutor_id):
        pass