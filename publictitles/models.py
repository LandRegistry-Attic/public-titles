from publictitles import db

class Title(db.Model):

    __tablename__ = 'title'

    id = db.Column(db.Integer, primary_key=True)
    title_number = db.Column('title_number', db.String(9), unique=True)
    house_number = db.Column('house_number', db.String(10))
    road  = db.Column('road', db.String(1000))
    town = db.Column('town', db.String(100))
    postcode = db.Column('post_code', db.String(25))
    price_paid = db.Column('price_paid', db.Float, nullable=True)

    def __init__(self, **kwargs):
        self.title_number = kwargs['title_number']
        self.house_number = kwargs['house_number']
        self.road = kwargs['road']
        self.town = kwargs['town']
        self.postcode = kwargs['postcode']

    def __repr__(self):
        return "Title number: %s | db id: %d | house_number : %s | road : %s | post code: %s" % (self.title_number, self.id, self.house_number, self.road, self.postcode)
