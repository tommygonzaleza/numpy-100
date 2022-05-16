import pytest, re, os, numpy

@pytest.mark.it('The output should be a vector with the numbers from 0 to 9.')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == "[0 1 2 3 4 5 6 7 8 9]\n"

@pytest.mark.it('You should create a function named generator')
def test_variable_exists(app):
    try:
        assert app.generator != None
    except AttributeError:
        raise AttributeError("The function 'generator' should exists")

@pytest.mark.it("You have to use the fromiter() function.")
def test_dtype_use():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.fromiter\s*\(")
        assert bool(regex.search(content)) == True