from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
  return render_template('index.html', name=name)

if __name__ == 'main':
  app.run(debug=True)