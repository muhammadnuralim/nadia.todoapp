from flask import Blueprint
from flask_cors import CORS

homeBp = Blueprint('home', __name__)
CORS(homeBp)

from app.home import routes 