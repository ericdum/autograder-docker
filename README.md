
### Design ideas
1. Testing in Docker for easy environment isolation. In the early stage, statistics are performed using stdout, and later using a daemon method. 
2. The testing methods include:
    * Run the file, enter stdin, and detect stdout
    * Reference function, input parameters, and detection output 
    * Import the compressed package and execute the project file
3. Use `go_for_test.py` to communicate with Docker, copy the entire `out` directory to Docker, and then run the `test.py` file test case inside.
4. The test target file is placed in the `out/target/` directory, and the default single file is placed in the `out/target/main.py` file. If it is a compressed package, the run path and parameters need to be provided, but they are limited to relative paths to the `target`. Be aware of path security issues.
5. Expose the interface through `grader.py` and test the entire project through the `tests` directory
6. No need to write complex test cases, just define the input, output, and running parameters to test.

### Quick Start

```shell
pip install -r requirements.txt

docker build -t autograder .

# test from terminal
python cmd.py _code.py _case.json
```

```python
# in python file
from grader import grade_for_file

code = "print(input() or 'PyCharm')"
test_cases =  [
     ["ABC", "ABC", ["mode2"]],  # 接收 stdin 并输出到 stdout, and work with args
     ["hell world", "hell world", ["mode2"]],  # same as above
     ["ABC", "PyCharm", []],  # not accept stdin in the target code, but send some in.
     ["", "PyCharm", []]  # nothing send to stdin
 ] # input, output, args

# following code will run the code though sub proccess
result = grade_for_file(code, test_cases)
# result == {
#  total, passed, failed, failed_info
#}
# you can simply get a score by result["passed"] / result["total"]
```

### TODO
- [x] Support Docker-based testing using std IO
- [ ] Integrate into CTFd to support python grader
- [ ] Support function call
- [ ] Support task queue, by using database
- [ ] Support queue in CTFd
- [ ] Support task queue, by using message queue