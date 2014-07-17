from publictitles import app, db
from publictitles.models import Title
from flask import jsonify, request, abort

@app.route('/title/<title_number>')
def title_number(title_number):
    app.logger.info('Title number %s requested' % title_number)
    title = Title.query.filter_by(title_number=title_number).first()
    if title:
        return jsonify({'title_number':  title.title_number,
                                     'house_number': title.house_number,
                                     'road': title.road,
                                     'town': title.town,
                                     'postcode': title.postcode,
                                     'pricepaid': title.price_paid})
    else:
        abort(400)

# do we ever update in this db?
# not sure it matters as we can move to elastic search soon
@app.route('/title/<title_number>', methods=['POST'])
def add_title(title_number):
    app.logger.info("Received %s from the-feeder" % request.json)
    title = Title.query.filter_by(title_number=title_number).first()
    if title:
        app.logger.info("Title number %s already" % title_number)
    else:
        app.logger.info("Create entry for title number %s" % title_number)
        house_number = request.json['house_number']
        road = request.json['road']
        town = request.json['town']
        postcode = request.json['postcode']
        title = Title(title_number, house_number, road, town, postcode)
        title.price_paid = request.json['price_paid']
        db.session.add(title)
        db.session.commit()
    return "", 200
