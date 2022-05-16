import pytest, re, os, numpy

@pytest.mark.it('The output should be a 5 x 5 matrix with the row values from 0 to 4.')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == """[[0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]]\n"""

@pytest.mark.it("You have to use the arange() function.")
def test_dtype_use():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.arange\s*\(")
        assert bool(regex.search(content)) == True