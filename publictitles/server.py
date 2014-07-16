from publictitles import app, db
from publictitles.models import Title
from flask import jsonify, request, abort

@app.route('/title/<title_number>')
def title_number(title_number):
    app.logger.info('Title number %s requested' % title_number)
    title = Title.query.filter_by(title_number=title_number).first()
    if title:
        return jsonify({'title_number':  title.title_number,
                                     'address': title.address,
                                     'postcode': title.postcode})
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
        address = request.json['address']
        postcode = request.json['postcode']
        title = Title(title_number, address, postcode)
        db.session.add(title)
        db.session.commit()
    return "", 200
