import json
from publictitles import app, db
from publictitles.models import Title
from flask import jsonify, request

@app.route('/titles/<title_number>')
def title_number(title_number):
    app.logger.info('Title number %s requested' % title_number)
    title = Title.query.filter_by(title_number=title_number).first()
    if title:
        return jsonify({'title_number':  title.title_number,
                                'address': title.address,
                                'postcode': title.postcode})
    else:
        return jsonify({})

@app.route('/titles',methods=['POST'])
def add_title():
    req_body = request.json

    title_number = req_body['title_number']
    address = req_body['address']
    postcode = req_body['postcode']

    new_title = Title(title_number, address, postcode)

    db.session.add(new_title)
    db.session.commit()

    return "", 200
