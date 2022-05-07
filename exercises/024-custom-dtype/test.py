import pytest, re, os, numpy, app

@pytest.mark.it('You should create a variable named color')
def test_variable_exists():
    try:
        app.color
    except AttributeError:
        raise AttributeError("The variable 'color' should exist on app.py")

@pytest.mark.it('The variable color itemsize should be 4')
def test_color_itemsize():
    try:
        assert app.color.itemsize == 4
    except AttributeError:
        raise AttributeError("The variable 'color' should exist on app.py")

@pytest.mark.it("You have to use the mean() function.")
def test_dtype_use():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.dtype\s*\(")
        assert bool(regex.search(content)) == True
