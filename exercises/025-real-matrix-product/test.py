import pytest, re, os, numpy

@pytest.mark.it('The output should be the dot product of matrix1 and matrix2.')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == """[[3. 3.]
 [3. 3.]
 [3. 3.]
 [3. 3.]
 [3. 3.]]\n"""

@pytest.mark.it('You should create a variable named matrix1')
def test_matrix1_exists():
    try:
        import app
        app.matrix1
    except AttributeError:
        raise AttributeError("The variable 'matrix1' should exist on app.py")

@pytest.mark.it('You should create a variable named matrix2')
def test_matrix2_exists():
    try:
        import app
        app.matrix2
    except AttributeError:
        raise AttributeError("The variable 'matrix2' should exist on app.py")

@pytest.mark.it("You have to use the dot() function.")
def test_dtype_use():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.dot\s*\(")
        assert bool(regex.search(content)) == True
