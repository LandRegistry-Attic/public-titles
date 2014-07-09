from publictitles import app
from flask import jsonify

@app.route('/titles/<title_number>')
def title_number(title_number):
    app.logger.info('Title number %s requested' % title_number)
    return jsonify({'title_number':  title_number})
