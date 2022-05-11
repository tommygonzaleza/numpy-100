import pytest, re, os, numpy

@pytest.mark.it('The vector elements should be rounded.')
def test_print(capsys):
    import app
    assert app.vector[0] == numpy.ceil(app.vector[0])

@pytest.mark.it('You should create a variable named vector')
def test_vector_exists():
    try:
        import app
        app.vector
    except AttributeError:
        raise AttributeError("The variable 'vector' should exist on app.py")