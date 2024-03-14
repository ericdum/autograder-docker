import pytest
from ..go_for_docker import Go4Docker

target = """
import sys
def print_hi(name):
    print(f'Hi, {name}') 

if __name__ == '__main__':
    if len(sys.argv) == 2:
        name = sys.argv[1]
        if name == "mode2":
            name = input("something i told you")
    else:
        name = 'PyCharm'
    print_hi(name)
    """

@pytest.fixture
def setup_file():
    with open('./out/target/main.py', 'w') as f:
        f.write(target)
    yield

def test_runfile(setup_file):
    g4t = Go4Docker(dir="out", target=target)
    result = g4t.test()
    assert "total" in result
    assert "passed" in result
    assert "failed" in result
    assert "failed_info" in result
    assert isinstance(result["total"], int)
    assert isinstance(result["passed"], int)
    assert isinstance(result["failed"], int)
    assert isinstance(result["failed_info"], str)


