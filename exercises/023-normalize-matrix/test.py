import pytest, re, os, numpy

@pytest.mark.it("You have to use the mean() function.")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.mean\s*\(")
        assert bool(regex.search(content)) == True

@pytest.mark.it("You have to use the std() function.")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"\.std\s*\(")
        assert bool(regex.search(content)) == True