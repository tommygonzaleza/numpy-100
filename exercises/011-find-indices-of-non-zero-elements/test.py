import pytest, re, os

@pytest.mark.it("You have to use the nonzero() function")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.nonzero\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The output should be a tuple of arrays with the indices of non zero values')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == '(array([0, 1, 4]),)\n'