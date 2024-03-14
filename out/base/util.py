import subprocess
import os


wd = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../target")


def runfile(input="", output="", strict=False, file="main.py", args=[]):
    assert '..' not in file, "执行路径不合法"
    file = os.path.join(wd, file)
    # result = subprocess.run(['python', file], stdout=subprocess.PIPE)
    # assert result.returncode == 0  # 确保脚本成功执行
    # assert 'PyCharm' in result.stdout.decode('utf-8')  # 检查输出是否包含预期内容

    assert os.path.exists(file), f"文件 {file} 不存在"
    process = subprocess.Popen(['python', file] + args,
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True)
    try:
        # 通过标准输入发送数据
        process.stdin.write(input)
        process.stdin.flush()  # 确保数据被立即发送，而不是缓存起来

        stdout, error = process.communicate()
        assert not error, error
        if output:
            assert stdout, "无输出"

            if strict:
                assert output == stdout
            else:
                assert output in stdout  # 检查输出是否包含预期内容
    finally:
        # 关闭标准输入流
        process.stdin.close()

        # 等待进程完成
    process.wait()