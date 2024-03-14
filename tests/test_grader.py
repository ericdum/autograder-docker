from ..grader import grade_for_file

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

def test_grader():
    grade_for_file(target, [
        ["ABC", "ABC", ["mode2"]],  # 接收 stdin 并输出到 stdout, and work with args
        ["hell world", "hell world", ["mode2"]],  # same as above
        ["ABC", "PyCharm", []],  # not accept stdin in the target code, but send some in.
        ["", "PyCharm", []]  # nothing send to stdin
    ])