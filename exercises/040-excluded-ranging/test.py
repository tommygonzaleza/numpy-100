import pytest, re, os, numpy

@pytest.mark.it('The output should be a vector with all the dates of july.')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == "\n"

@pytest.mark.it("You have to use the arange() function.")
def test_dtype_use():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.arange\s*\(")
        assert bool(regex.search(content)) == True