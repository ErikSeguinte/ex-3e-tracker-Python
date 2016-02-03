from PyQt5 import uic
import sys, re
import os

path = os.getcwd()

# uic.compileUiDir(path)

file_list = os.listdir(path)

print(file_list)

ui_files = [string for string in file_list if re.match(r'.*\.ui', string)]
py_files = [string for string in file_list if
            re.match(r'.*\.py', string) and not (string == '__init__.py' or string == 'convert_ui.py')]

print(ui_files)
print(py_files)
