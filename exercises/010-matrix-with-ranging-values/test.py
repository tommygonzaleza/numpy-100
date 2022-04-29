import pytest, re, os

@pytest.mark.it("You have to use the reshape() function")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.reshape\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The output should be a matrix which values should be from 0 to 9')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == '[[0 1 2]\n [3 4 5]\n [6 7 8]]\n'