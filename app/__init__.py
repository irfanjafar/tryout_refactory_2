from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db) 
jwt = JWTManager(app)


# # model
from app.model import absen, user, kelas

# #Memanggil file routes 
# # (akan segera dibuat)
from app.route import routeUser, routeKelas, routeAbsen

