from go_for_docker import Go4Docker
import json

case_grade_for_file = """
import pytest
from .base.util import runfile

@pytest.mark.parametrize("input, expected, args", <<<replace_case>>>)
def test_runfile(input, expected, args):
    if args == None:
        runfile(input or "", expected or "")
    else:
        runfile(input or "", expected or "", args=args)
"""

def grade_for_file(target, cases):
    with open('./out/target/main.py', 'w') as f:
        f.write(target)

    with open('./out/test.py', 'w') as f:
        f.write(case_grade_for_file.replace("<<<replace_case>>>",
                                            json.dumps(cases)))

    g4t = Go4Docker(dir="./out", target=target)

    return g4t.test()
