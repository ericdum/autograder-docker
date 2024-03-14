
import pytest
from .base.util import runfile

@pytest.mark.parametrize("input, expected, args", [["ABC", "ABC", ["mode2"]], ["hell world", "hell world", ["mode2"]], ["ABC", "PyCharm", []], ["", "PyCharm", []]])
def test_runfile(input, expected, args):
    if args == None:
        runfile(input or "", expected or "")
    else:
        runfile(input or "", expected or "", args=args)
