import pytest, os, re

@pytest.mark.it("You have to use the info() function")
def test_declare_variable():
    path = os.path.dirname(os.path.abspath(__file__)) + '/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = re.compile(r"np\.info\(\s*np\.add\s*\)")
        assert bool(regex.search(content)) == True
