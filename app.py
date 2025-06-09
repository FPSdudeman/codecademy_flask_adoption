from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return '''
  <h1>Adopt a Pet!</h1>
  <p>
  Browse through the links below to find your new furry friend:
  </p>
  <ul>
  <li><a href="/animal/dogs">Dogs</a></li>
  <li><a href="/animal/cats">Cats</a></li>
  <li><a href="/animal/rabbits">Rabbits</a></li>
  </ul>
  '''

@app.route('/animal/<pet_type>')
def animals(pet_type):
  html = f'<h1>List of {pet_type}</h1>'
  html += '<ul>'
  count = 0
  for pet in pets[pet_type]:
    html += f'<li><a href="/animal/{pet_type}/{count}">{pet["name"]}</a></li>'
    count += 1
  html += '</ul>'
  return html

@app.route('/animal/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  return f'<h1>{pet["name"]}</h1>'
