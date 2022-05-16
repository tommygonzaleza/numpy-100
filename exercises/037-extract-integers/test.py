import pytest, re, os, numpy

@pytest.mark.it('The output should be a vector only with the integer numbers.')
def test_print(capsys):
    import app
    vector = numpy.floor(app.vector)
    captured = capsys.readouterr()
    assert captured.out == f"{vector}\n"