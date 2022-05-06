import pytest, re, os, numpy

@pytest.mark.it("You have to use the unravel_index() function.")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.unravel_index\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it('The output should be the index of the 100th position.')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == '(1, 5, 3)\n'