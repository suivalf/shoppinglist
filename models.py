from app import db

class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.String(200), nullable=False)
    item_qty = db.Column(db.Integer, nullable=True)
    def __init__(self, item_name, item_qty):
        self.item_name = item_name
        self.item_qty = item_qty
    def __repr__(self):
        return '<Item: %r, Name: %r, Quantity: %r>' % self.id % self.item_name % self.item_qty