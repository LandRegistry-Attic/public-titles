from factory.alchemy import SQLAlchemyModelFactory

from publictitles.models import Title
from publictitles import db

class TitleFactory(SQLAlchemyModelFactory):

    class Meta:
        model = Title
        sqlalchemy_session = db.session

    title_number = "TN1234567"
    house_number = "1"
    road  = "High Street"
    town = "Croydon"
    postcode = "ABC 123"
