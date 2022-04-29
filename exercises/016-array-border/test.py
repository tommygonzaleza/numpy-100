import pytest
import os
import numpy

@pytest.mark.it("You have to use the ones() method")
def test_random():
    f = open(os.path.dirname(os.path.abspath(__file__)) + '/app.py')
    content = f.read()
    assert "ones(" in content

@pytest.mark.it('The output should be a the expected matrix')
def test_print(capsys):
    import app
    captured = capsys.readouterr()
    assert captured.out == '[[1. 1. 1. 1. 1.]\n [1. 0. 0. 0. 1.]\n [1. 0. 0. 0. 1.]\n [1. 0. 0. 0. 1.]\n [1. 1. 1. 1. 1.]]\n'