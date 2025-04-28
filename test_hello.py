from hello import more_hello

def test_more_hello():
    assert "HI" == more_hello(), "Error"

def test_more_hello2():
    assert "bye" == more_hello(), "Error"
