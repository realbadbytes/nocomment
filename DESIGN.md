# Design

GUI interface

Interface will show all files in project. Each file will be color coded based on its documentation status. GUI will be divided into two windows, vertically separated.

GREEN : docstrings exist and are up-to-date

YELLOW : docstrings exist but are older than newest code edits

RED : docstrings don't exist / are incomplete

Selecting a file will present the source code in the right-hand window. Again, all functions will be color coded based on docstring status. Selecting a function will open a dialog.

Function dialog is the main purpose of this tool. All required information to create a docstring will be queried from the user. For example, if a function has no docstring and RST is desired, user will be prompted to enter descriptions for each function parameter (and more).

After dialog is completed, the docstring will be generated and written to a temporary .py file. User will be given opportunity to write changes to actual source file.

# Requirements

GUI - PySide2?

Filesystem interaction - os, PySide2.QtCore.QDir, PySide2.QtWidgets.QFileSystemModel

Target module loading/information extraction - importlib





