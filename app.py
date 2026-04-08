from flask import Flask
from config.database import Base, engine
from models.tutor import Tutor
from routes.tutor_routes import tutor_bp
from routes.animal_routes import animal_bp
from routes.auth_rotes import auth_bp
from models.user import User

app = Flask(__name__)

Base.metadata.create_all(engine) #Integrar isso aqui com o banco de dados para criar direto, sem ter que criar o banco manualmente

app.register_blueprint(tutor_bp)
app.register_blueprint(animal_bp)
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)

