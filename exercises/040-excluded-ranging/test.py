import pytest, re, os, numpy

@pytest.mark.it('The output should be a vector of size ten with values between 0 and 1.')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == "[0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9]\n"

@pytest.mark.it("You have to use the linspace() function.")
def test_dtype_use():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.linspace\s*\(")
        assert bool(regex.search(content)) == True