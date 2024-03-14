import docker
import os
import re
import tempfile
from docker.types import Mount

client = docker.from_env()

class Go4Docker:
    def __init__(self, dir, debug=False, target=""):
        self.path = os.path.join(os.path.dirname(os.path.abspath(__file__)), dir)
        self.debug = debug
        self.target = target

    def test(self):
        mount = Mount(type='bind', source=self.path, target="/tests")
        try:
            # 运行镜像，这里以nginx为例，你可以替换成你自己的镜像名
            container = client.containers.run(
                "autograder",
                detach=True,
                remove=True,
                mem_limit=512*1012*1025,
                command="pytest test.py",
                mounts=[mount]
            )
            output = ""
            failed_info = ""
            failed_count = 0
            passed_count = 0
            for line in container.logs(stream=True, stdout=True, stderr=False):
                # 输出容器的标准输出
                output += line.decode('utf-8')

            if self.debug:
                print(output)

            pass_pattern = re.compile(r'>>>>>>>>>>>>>>>Passed:\s+(\d+)', re.MULTILINE)
            fail_pattern = re.compile(r'>>>>>>>>>>>>>>>Failed:\s+(\d+)', re.MULTILINE)

            pass_match = pass_pattern.search(output)
            fail_match = fail_pattern.search(output)

            if pass_match and fail_match:
                # 提取匹配的部分中的数字
                failed_count = int(fail_match.group(1))
                passed_count = int(pass_match.group(1))
                if self.debug:
                    print(f"\nTest statistics:")
                    print(f"Failed: {failed_count}")
                    print(f"Passed: {passed_count}")
            else:
                print("Test statistics line not found.")


            if failed_count:
                pattern = re.compile(r'^={2,}\s+short test summary info\s+={2,}$', re.MULTILINE)
                match = pattern.search(output)
                if match:
                    # 获取匹配行的结束位置
                    end_pos = match.end()
                    # 从匹配行后面开始搜索，直到遇到另一个由'='组成的行
                    rest_of_output = output[end_pos:]
                    next_summary_line_pattern = re.compile(r'^={2,}.*$', re.MULTILINE)
                    next_match = next_summary_line_pattern.search(rest_of_output)
                    if next_match:
                        # 提取两个匹配行之间的内容（即具体的失败信息）
                        failed_info = rest_of_output[:next_match.start()].strip()
                        if self.debug:
                            print("\nFailed test info:")
                            print(failed_info)
                    else:
                        print("No additional summary info found.")
                else:
                    print("Cannot extract failed test info without finding the summary line first.")

            return {
                "total": failed_count+passed_count,
                "failed": failed_count,
                "passed": passed_count,
                "failed_info": failed_info
            }
            # print(container.id)  # 打印出容器的ID
        except Exception as e:
            print(f"An error occurred: {e}")
            # 确保容器被删除（如果之前没有被删除的话）
            if container.id is not None:
                container.remove()