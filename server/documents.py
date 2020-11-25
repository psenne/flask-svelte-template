from app import db

class Documents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    userId = db.Column(db.String(255))

    def serialize(self):
        return {
            'uuid': self.uuid,
            'text': self.text
        }