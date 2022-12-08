from rps_game import create_app


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_new_game(client):
    response = client.get('/')
    assert b'New Game' in response.data

def test_score(client):
    response = client.get('/score')
    assert b'<tr><td>winner</td><td>winner</td><td>loser</td><td>1</td></tr>' in response.data
