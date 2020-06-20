from flask_app import hello_world

def test_hello_world():
    assert 'Hello and welcome to the homepage' == hello_world()
    