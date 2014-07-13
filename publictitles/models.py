from publictitles import db

class Title(db.Model):

    __tablename__ = 'title'

    id = db.Column(db.Integer, primary_key=True)
    title_number = db.Column('title_number', db.String(9), unique=True)
    address  = db.Column('address', db.String(1000))
    postcode = db.Column('post_code', db.String(25))

    def __init__(self, id, title_number, address, postcode):
        self.id = id
        self.title_number = title_number
        self.address = address
        self.postcode = postcode

    def __repr__(self):
        return "Title number: %s | db id: %d | address : %s | post code: %s" % (self.title_number, self.id, self.address, self.postcode)
