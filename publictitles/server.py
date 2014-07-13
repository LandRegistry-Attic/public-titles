from publictitles import app
from publictitles.models import Title
from flask import jsonify

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
