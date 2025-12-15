#app.py

def add(a, b):
    return a + b

#This will be use to make the addition
def test_add():
    assert add(1, 4) == 5
    assert add(1, -1) == 0
