import pytest, re, os

@pytest.mark.it("You have to use the eye() function")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.eye\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The output should be a matrix which values should be from 0 to 9')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == '[[1. 0. 0.]\n [0. 1. 0.]\n [0. 0. 1.]]\n'