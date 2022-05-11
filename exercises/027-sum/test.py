import pytest, re, os, numpy

@pytest.mark.it('The output should be the sum of the elements of the vector (10).')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == "10\n"

@pytest.mark.it('You should create a variable named vector')
def test_vector_exists():
    try:
        import app
        app.vector
    except AttributeError:
        raise AttributeError("The variable 'vector' should exist on app.py")

@pytest.mark.it("You have to use the sum() function.")
def test_dtype_use():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.sum\s*\(")
        assert bool(regex.search(content)) == True