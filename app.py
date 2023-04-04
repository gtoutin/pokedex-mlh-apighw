
import os

from flask import Flask, render_template
import requests


# define json graphql query with only info we care about
# pokemon and color query
color_query = """
query ColorQuery {
  pokemon_v2_pokemonspecies {
    name
    pokemon_v2_pokemoncolor {
      name
    }
  }
}
"""

# all pokemon that belong to a color
"""
# TODO
"""


# define flask app and home route
app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    """post the query to the graphql endpoint and serve the data in the template"""
    response = requests.post('https://beta.pokeapi.co/graphql/v1beta', json={'query': color_query})
    if not response.ok:
        return render_template('oops.html')
    data=response.json().get("data", {}).get("pokemon_v2_pokemonspecies", {})
    if data == {}:
        return render_template('oops.html')

    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))