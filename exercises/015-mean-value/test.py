import pytest, re, os, numpy

@pytest.mark.it("You have to use the mean() function")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.mean\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The output should be a the mean value of the array')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == f'{app.vector.mean()}\n'

@pytest.mark.it('You should create a variable named vector')
def test_arr_exists():
    try:
        from app import vector
    except AttributeError:
        raise AttributeError("The variable 'vector' should exist on app.py")

@pytest.mark.it('The array should have ten random values')
def test_arr_value(capsys):
    from app import vector
    size = numpy.size(vector)
    assert size == 10