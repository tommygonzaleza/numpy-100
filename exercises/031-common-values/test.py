import pytest, re, os, numpy

@pytest.mark.it('The output should be a vector with the common values.')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == "[5 6 7 8 9]\n"

@pytest.mark.it('You should create a variable named vector1')
def test_vector_exists():
    try:
        import app
        app.vector1
    except AttributeError:
        raise AttributeError("The variable 'vector1' should exist on app.py")

@pytest.mark.it('You should create a variable named vector2')
def test_vector_exists():
    try:
        import app
        app.vector2
    except AttributeError:
        raise AttributeError("The variable 'vector2' should exist on app.py")

@pytest.mark.it("You have to use the intersect1d() function.")
def test_dtype_use():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.intersect1d\s*\(")
        assert bool(regex.search(content)) == True