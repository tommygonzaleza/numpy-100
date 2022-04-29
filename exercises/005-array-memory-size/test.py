import pytest, os, re

@pytest.mark.it("You have to use the itemsize property.")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.itemsize")
        assert bool(regex.search(content)) == True

@pytest.mark.it("You have to use the size property.")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.size")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The output should be the memory size of a null vector of size 10')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == '80\n'