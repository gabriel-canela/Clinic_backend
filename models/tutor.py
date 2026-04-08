from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base

class Tutor (Base):
    __tablename__ = "tutor"
    id_tutor = Column (Integer, primary_key=True)
    nome = Column(String, nullable=False)
    telefone = Column (String)
    email = Column (String)
    animais = relationship ("Animal", back_populates = "tutor", cascade = "all, delete")
    user = relationship("User", back_populates="emailUnico", cascade = "all, delete")