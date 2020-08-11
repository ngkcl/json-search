from flask import Flask, jsonify, Response, request
from flask_session import Session

from flask_cors import CORS, cross_origin

# Import own scripts correctly 
if __name__ == "__main__":
    import config
    import search
else:
    import json_search.config as config
    import json_search.search as search

import os

SERVER_HOST = os.getenv('SERVER_HOST', config.SERVER_HOST)
SERVER_PORT = os.getenv('SERVER_PORT', config.SERVER_PORT)

app = Flask(__name__)
app.config.from_object(__name__)

# Setup CORS
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Setup sessions
Session(app)

# Searcher object
_searcher = search.Searcher()
_searcher.generate_index()

@app.route("/", methods = ['GET'])
def index() -> str:
    return jsonify({"message": "It Works"})


@app.route("/search", methods = ['POST'])
@cross_origin()
def search() -> Response:
    try:
        req = request.json

        # Raise error if data not supplied
        if not req['data']:
            raise

    except Exception as e:
        return jsonify({
            'error': True, 
            'message': "Please supply a json with search data"
        }), 500

    try:
        search_res = _searcher.search(req['data'])
        return jsonify({
            'search_results': search_res
        }), 200
    except Exception as e:
        return jsonify({
            'error': True, 
            'message': str(e)
        }), 500

@app.route("/search_page", methods = ['POST'])
@cross_origin()
def search_page() -> Response:
    try:
        req = request.json

        # Raise error if data not supplied
        if not req['data'] or not req['page']:
            raise

    except Exception as e:
        return jsonify({
            'error': True, 
            'message': "Please supply a json with search data, page number, and page length"
        }), 500

    try:
        search_res = _searcher.search_page(req['data'],req['page'])
        return jsonify({
            'search_results': search_res
        }), 200
    except Exception as e:
        return jsonify({
            'error': True, 
            'message': str(e)
        }), 500

@app.route('/suggest', methods=['POST'])
@cross_origin()
def suggest() -> list:
    try:
        req = request.json

        # Raise error if data not supplied
        if not req['data']:
            raise

    except Exception as e:
        return jsonify({
            'error': True, 
            'message': "Please supply a json with search data"
        }), 500

    try:
        suggestions = _searcher.suggest(req['data'])
        return jsonify({
            'suggestions': suggestions
        }), 200
    except Exception as e:
        return jsonify({
            'error': True, 
            'message': str(e)
        }), 500
        
if __name__ == '__main__':
    app.run(host=SERVER_HOST, port=SERVER_PORT)        