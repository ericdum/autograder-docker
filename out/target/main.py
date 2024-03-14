
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
    