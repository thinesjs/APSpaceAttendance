from APSpaceAttendance import *
import requests

print("# APSpace Attendance Automation v1 #")
print("Press ENTER to start the program")
check = input("Press C and Enter to terminate")

if check == "c":
    print("Stopping...")
    exit()

casUrl = f'https://cas.apiit.edu.my/cas/v1/tickets?username={apkey}&password={apkey_password}'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

x = requests.post(casUrl, headers=headers)

if x.status_code == 401:
    print("Log in to APSpace failed! Check config.ini or network connection!")
    exit()

run = APSpaceAttendance()
