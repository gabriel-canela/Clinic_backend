from sqlalchemy import Column, Integer, String, ForeignKey
from config.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column (Integer, primary_key=True)
    email = Column (String, ForeignKey("tutor.email", ondelete="CASCADE"), unique=True, nullable = False,  )
    password_hash = Column(String, nullable=False)
    token = Column(String)
    user_type = Column(Integer, nullable=False)## Tipo do usuário. 1 = ADM, 2 = Tutor, 3 = vet.
    emailUnico = relationship("Tutor", back_populates="user")
    