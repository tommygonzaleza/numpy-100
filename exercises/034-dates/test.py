import pytest, re, os, numpy

@pytest.mark.it("The output should be yesterday's date.")
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    yesterday = numpy.datetime64('today') - numpy.timedelta64(1)
    assert captured.out == f"{yesterday}\n"

@pytest.mark.it("You have to use the datetime64() function.")
def test_dtype_use():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.datetime64\s*\(")
        assert bool(regex.search(content)) == True