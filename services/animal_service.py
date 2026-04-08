from config.database import SessionLocal
from models.animal import Animal

class AnimalService:
    @staticmethod
    def create_animal(data):
        session = SessionLocal()
        animal = Animal(**data)
        session.add(animal)
        session.commit()
        session.refresh(animal)
        session.close()
        return animal
        
    @staticmethod
    def list_animais():
        session = SessionLocal()
        animals = session.query(Animal).all()
        session.close()
        return animals

    @staticmethod
    def get_animal(id_animal):
        session = SessionLocal()
        animal = session.query(Animal).filter(Animal.id_animal == id_animal).first()
        
        session.close()
        return animal


    @staticmethod
    def update_animal (animal_id, data):
        pass

    @staticmethod
    def delete_animal (animal_id):
        session = SessionLocal()
        animal = session.query(Animal).filter(Animal.id_animal == animal_id).first()

        if not animal:
            session.close()
            return False  # ou None, dependendo da sua regra

        session.delete(animal)
        session.commit()
        session.close()
        return True