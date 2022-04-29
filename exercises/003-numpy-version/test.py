import os, pytest, re

@pytest.mark.it("Import Numpy as np on the app.py file")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"import\s+numpy\s+as\s+np")
        assert bool(regex.search(content)) == True

@pytest.mark.it("You have to access to the __version__ property.")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"np\.__version__")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The output should be a null vector of size 10')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == '1.17.4\n'