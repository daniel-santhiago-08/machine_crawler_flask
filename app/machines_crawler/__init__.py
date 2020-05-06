from flask import Blueprint

machines_crawler = Blueprint('machines_crawler', __name__)

from app.machines_crawler import views
