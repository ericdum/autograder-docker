import argparse
from grader import grade_for_file

def main():
    parser = argparse.ArgumentParser(description='A program that provides programming assignment grading based on Docker.')

    parser.add_argument('code', help='Code file path')
    parser.add_argument('cases', help='Cases file path')
    parser.add_argument('-d', '--debug', action='store_true', help='Output debugging information')

    args = parser.parse_args()

    with open(args.code, 'r') as code:
        with open(args.cases, 'r') as cases:
            print(grade_for_file(code.read(), cases.read(), args.debug))


if __name__ == '__main__':
    main()