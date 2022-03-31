import os
import configparser
import xlsxwriter
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

import pytest
ini_file = os.path.abspath(os.path.dirname(".\\..\configurations\."))
config = configparser.RawConfigParser()
config.read(ini_file + "\\config.ini")
updated_repo_path = config.get('common info', 'updated_repo_path')
testCases_path = config.get('common info', 'testCases_path')
testData_path = config.get('common info', 'testData_path')
git_branch = config.get('common info', 'git_branch')


class TestExecutionAutomation:
    @staticmethod
    def setup():
        print("******************** TEST EXECUTION STARTED ********************")

    @staticmethod
    def teardown():
        print("******************** TEST EXECUTION COMPLETED ********************")

    @staticmethod
    def git_command(git_repo_command):
        print("******************** GIT COMMAND EXECUTION STARTED ********************")
        os.chdir(updated_repo_path)
        repo_path = os.getcwd()
        print(repo_path)
        os.system(command=git_repo_command)
        print("******************** GIT COMMAND EXECUTION COMPLETED ********************")

    @staticmethod
    def files_update():
        files = []
        os.chdir(updated_repo_path)
        folders = os.listdir()
        if "testCases" in folders:
            os.chdir(testCases_path)
            print("-I- Current Directory Selected is :{}".format(os.getcwd()))
            files = os.listdir()
            if len(files) != 0:
                print("******************** ALL FILES LOADED SUCCESSFULLY ********************")
        else:
            print("-I- Couldn't find any directory called 'TestCases'")
        return files

    @staticmethod
    def test_case_execution(file_name):
        os.chdir(updated_repo_path)
        folders = os.listdir()
        if "testCases" in folders:
            os.chdir(testCases_path)
            if file_name in os.listdir():
             os.system(command=file_name)

            else:
                print("The file is not available in this directory")
        else:
            print("-I- Couldn't find any directory called 'TestCases'")

    @staticmethod
    def generate_result_files(res):
        os.chdir(testData_path)
        # results_list = os.listdir()
        curr_date = str(datetime.date.today())
        workbook = xlsxwriter.Workbook("Test_case_result" + ".xlsx")
        worksheet = workbook.add_worksheet("Test_case_results")
        worksheet.set_column(0, 0, 50)
        bold = workbook.add_format({'bold': True})
        worksheet.write(0, 0, "Test case Name", bold)
        worksheet.write(0, 2, "Result", bold)
        worksheet.write(0, 1, "Date", bold)
        row = 1
        col = 0
        for i, j in res:
            worksheet.write(row, col, i)
            worksheet.write(row, col + 1, curr_date)
            worksheet.write(row, col + 2, j)
            row += 1
        workbook.close()

    @staticmethod
    def Send_mail():
        print("Mail Sending Started")
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login('arathod250498@gmail.com', '8897258397') # Login with your email and password

        def message(subject="Python Notification",
                    text="", attachments=None):
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg.attach(MIMEText(text))

            if attachments is not None:

                if type(attachments) is not list:
                    attachments = [attachments]
                for attachment in attachments:
                    with open(attachment, 'rb') as f:
                        file = MIMEApplication(
                            f.read(),
                            name=os.path.basename(attachment)
                        )
                    file['Content-Disposition'] = f'attachment;\
                    filename="{os.path.basename(attachment)}"'

                    msg.attach(file)
            return msg
        # Call the message function
        msg = message("Good!", "Hi there!", r"C:\repo2\automation-project\testData\Test_case_result.xlsx")

        # Make a list of emails.
        to = ["venkatv19be1d3@gmail.com", "anjalirathod2504@gmail.com"]

        # Provide some data to the sendmail function!
        smtp.sendmail(from_addr="arathod250498@gmail.com",
                      to_addrs=to, msg=msg.as_string())

        # Finally, don't forget to close the connection
        smtp.quit()

        print("Mail Sending Completed...")

