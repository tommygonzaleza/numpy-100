import pytest, re, os, numpy

@pytest.mark.it('The output should be a vector with the elements from 3 to 8 negated.')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == "[ 0  1  2  3 -4 -5 -6 -7  8  9 10]\n"

@pytest.mark.it('You should create a variable named vector')
def test_vector_exists():
    try:
        import app
        app.vector
    except AttributeError:
        raise AttributeError("The variable 'vector' should exist on app.py")