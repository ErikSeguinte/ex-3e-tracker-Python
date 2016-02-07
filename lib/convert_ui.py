from PyQt5 import uic
import sys, re, subprocess, datetime
import os

path = os.getcwd()


# uic.compileUiDir(path)
# print(path)


def get_datetime(filename: str):
    timestamp = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(timestamp)


file_list = os.listdir(path)

ui_files = [string for string in file_list if re.match(r'.*\.ui', string)]
py_files = [string for string in file_list if
            re.match(r'.*\.py', string) and not (string == '__init__.py' or string == 'convert_ui.py')]

ui_files.sort()

py_files.sort()

conversion = False
for file in ui_files:
    name = file.split('.')[0]
    match = name + '.py'
    if match not in py_files:
        with open(match, 'w', encoding='utf-8') as new_file:
            uic.compileUi(file, new_file)

        subprocess.run(['hg', 'add', match, '-y'])
        conversion = True
        print('Converting ' + str(file))
        continue

    ui_time = get_datetime(file)
    py_time = get_datetime(match)

    if py_time < ui_time:
        with open(match, 'w', encoding='utf-8') as new_file:
            uic.compileUi(file, new_file)

        conversion = True
        print('Converting ' + str(file))

print(conversion)
