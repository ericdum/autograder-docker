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
print(result)