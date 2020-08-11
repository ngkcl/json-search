from json_search import server

import pytest


import json

# Server client to be used in tests
@pytest.fixture
def client():
    """
        Yield a testing client
    """
    server.app.config['TESTING'] = True
    with server.app.test_client() as client:
        yield client

# Tests --------------------
def test_search_newhaven(client):
    """
        description: Tests if Newhaven is found
        when searching for hav
    """
    res = client.post('/search', json={"data": "hav"})
    
    data = json.loads(res.data)
    search_results = data['search_results']
    
    assert 'Newhaven' in [item['name'] for item in search_results]

def test_search_postcode_first(client):
    """
        description: Tests if search follows criteria that postcode
        is searched first before name
    """
    res = client.post('/search', json={"data": "br"})
    
    data = json.loads(res.data)
    search_results = data['search_results']

    assert 'Orpington' in search_results[0]['name']
    assert 'Bracknell' in search_results[1]['name']
# ==========================