import pytest, os, re

@pytest.mark.it("You have to use the zeros() function")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"np\.zeros\(\s*10\s*\)")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The output should be a null vector of size 10 and the fifth value should be 1')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == '[0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]\n'