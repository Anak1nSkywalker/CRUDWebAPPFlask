"""
class Note(db.Model):
    id = db.Column(db.Integer, prymary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)

    def __int__(self, title, body):
        self.title = title
        self.body = body
"""