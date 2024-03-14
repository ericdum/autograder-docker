import pytest
from ..out.base.util import runfile

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


@pytest.mark.parametrize("input, expected, args", [
    ["ABC", "ABC", ["mode2"]], # 接收 stdin 并输出到 stdout, and work with args
    ["hell world", "hell world", ["mode2"]], # same as above
    ["ABC", "PyCharm", None], # not accept stdin in the target code, but send some in.
    ["", "PyCharm", None] # nothing send to stdin
])
def test_runfile(setup_file, input, expected, args):
    if args == None:
        runfile(input, expected)
    else:
        runfile(input, expected, args=args)


