from lists import db

class Lists(db.Model): # tabela bazy danych dla list np lidl
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(lenght=50), nullable=False)
    lista = db.relationship('list', backref='owned_suer', lazy=True)


class List(db.Model):
     id = db.Column(db.Integer(), primary_key=true)
    name = db.Column(db.String(lenght=50), nullable=False)
    amount = db.Column(db.Integer(), nullable=False)
    purchased =db.Column(db.Boolean(), default=False)
    owner = db.Column(db.Integer(), db.ForeginKey(lists.id))

    def __repr__(self):
        return f'List {self.name}'