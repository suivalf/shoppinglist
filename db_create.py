from app import db
from models import Item

db.create_all()
db.session.commit()