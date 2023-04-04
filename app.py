
import os

from flask import Flask, request, Response, render_template
import requests

# define flask app and home route
# define json graphql query with only info we care about
# post the query to the graphql endpoint and serve the data in the template

# i care about pokemon color
"""query samplePokeAPIquery {
  pokemon_v2_pokemoncolor {
    pokemon_v2_pokemonspecies {
      name
      pokemon_v2_pokemoncolor {
        name
      }
    }
    name
  }
}
"""

"""query MyQuery {
  pokemon_v2_pokemoncolor {
    pokemon_v2_pokemoncolornames(where: {pokemon_v2_language: {id: {_eq: 9}}}) {
      name
    }
    pokemon_v2_pokemonspecies {
      name
    }
  }
}
"""

# AW YEAH pokemon and color
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


app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    # send POST
    # FIXME: uncomment below to reenable API
    # response = requests.post('https://beta.pokeapi.co/graphql/v1beta', json={'query': color_query})
    # if not response.ok:
    # return render_template('oops.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))