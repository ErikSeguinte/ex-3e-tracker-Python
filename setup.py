import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    'compressed': True,
    'includes':   [
        'LICENSE.txt'
    ],}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name="Exalted 3e Initiative Tracker",
      version="0.1",
      description="Tracker for Exalted",
      options={"build_exe": build_exe_options},
      executables=[Executable("start.py", base=base)])
