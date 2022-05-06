import pytest, re, os, numpy

@pytest.mark.it("You have to use the ones() function")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.ones\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The output should be a the expected matrix')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == '[[1. 1. 1. 1. 1.]\n [1. 0. 0. 0. 1.]\n [1. 0. 0. 0. 1.]\n [1. 0. 0. 0. 1.]\n [1. 1. 1. 1. 1.]]\n'