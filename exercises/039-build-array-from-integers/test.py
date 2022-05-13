import pytest, re, os, numpy

@pytest.mark.it('The output should be a vector with all the dates of july.')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == """['2022-07-01' '2022-07-02' '2022-07-03' '2022-07-04' '2022-07-05'
 '2022-07-06' '2022-07-07' '2022-07-08' '2022-07-09' '2022-07-10'
 '2022-07-11' '2022-07-12' '2022-07-13' '2022-07-14' '2022-07-15'
 '2022-07-16' '2022-07-17' '2022-07-18' '2022-07-19' '2022-07-20'
 '2022-07-21' '2022-07-22' '2022-07-23' '2022-07-24' '2022-07-25'
 '2022-07-26' '2022-07-27' '2022-07-28' '2022-07-29' '2022-07-30'
 '2022-07-31']\n"""

@pytest.mark.it("You have to use the arange() function.")
def test_dtype_use():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.arange\s*\(")
        assert bool(regex.search(content)) == True