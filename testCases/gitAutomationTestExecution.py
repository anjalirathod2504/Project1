import os.path
from utilities.gitAutomationUtils import *

git_auto =TestExecutionAutomation()
non_testing_files = ["__init__.py", "gitAutomationTestExecution.py", "updatedsort.py"]


class GitAutomationTestExecutionTest:
    @staticmethod
    def __init__():
        git_auto.setup()
        GitAutomationTestExecutionTest.git_automation_test()
        git_auto.teardown()

    @staticmethod
    def git_automation_test():
        res = []
        git_auto.git_command("git pull")
        print("-I- Repository Updated successfully")
        tests = git_auto.files_update()
        if len(tests) > 0:
            for test in tests:
                test_name = os.path.splitext(test)
                if test_name[1] == ".py" and not(test in non_testing_files):
                    try:
                        git_auto.test_case_execution(test)
                        res.append((test, "PASSED"))
                        print("Testcase PASSED for : {}".format(test))
                    except:
                        res.append((test, "FAILED"))
                        print("Testcase Failed for : {}".format(test))
        else:
            print("-I- Currently there are no tests are available")
        git_auto.generate_result_files(res)


if __name__ == "__main__":
    GitAutomationTestExecutionTest()
