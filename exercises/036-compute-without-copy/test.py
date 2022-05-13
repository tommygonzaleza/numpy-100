import pytest, re, os, numpy

@pytest.mark.it('The output should be a vector with the operation result.')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == "[-1.5 -1.5 -1.5]\n"

@pytest.mark.it("You have to use the add() function.")
def test_add_use():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.add\s*\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it("You have to use the divide() function.")
def test_divide_use():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.divide\s*\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it("You have to use the negative() function.")
def test_negative_use():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.negative\s*\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it("You have to use the multiply() function.")
def test_multiply_use():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.multiply\s*\(")
        assert bool(regex.search(content)) == True