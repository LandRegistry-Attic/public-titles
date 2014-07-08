from publictitles import app

@app.route('/')
def hello():
  return "hello"

@app.route('/titles/<titleno>')
def title(titleno):
  return "Hello %s" % titleno
