"""
# [🄽🄴🅃🄱🄻🄰🄶](https://github.com/netblag)
---
# Jupyter Notebook Fixer
---
## Updating Notebook Version

---

### This Python script updates Jupyter notebook files to version 4. It walks through a given directory,
### finds all .ipynb files, and updates them to version 4.


## [GitHub](https://github.com/netblag/jupyter-notebook-fixer)
---
    
"""

import os
import nbformat
import shutil
from nbformat.v4 import new_notebook

def fix_and_update_notebook_version(folder_path):
    # List all files and directories in the given folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.ipynb'):
                file_path = os.path.join(root, file)
                print(f"Checking {file_path}")

                try:                   
                    # Opening and reading the notebook file
                    with open(file_path, 'r', encoding='utf-8') as f:
                        notebook = nbformat.read(f, as_version=4)

                    # Saving the notebook file with version 4
                    with open(file_path, 'w', encoding='utf-8') as f:
                        nbformat.write(notebook, f)

                    print(f"{file_path} is valid and has been updated to version 4.")
                except Exception as e:
                    print(f"{file_path} is invalid. Error: {e}")
                    print(f"Attempting to fix {file_path}")

                    # Creating a new notebook and replacing the content
                    fixed_notebook = new_notebook()

                    # Reading the content of the notebook file as text
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Adding the main content to the cells of the new notebook
                    fixed_notebook.cells.append(nbformat.v4.new_code_cell(content))

                    # Saving the modified notebook
                    with open(file_path, 'w', encoding='utf-8') as f:
                        nbformat.write(fixed_notebook, f)

                    print(f"{file_path} has been fixed and updated to version 4.")

# Replace your directory path

#*------------------------------------------------------------------------------------------------*#
# If you want all files within the current folder to be updated and saved, activate this code:

# folder_path = r'YOUR_FOLDER_PATH'
#*------------------------------------------------------------------------------------------------*#

#*-----*#

# To facilitate precise execution of the script, you can use this code to specify the path and save the file in another directory.

folder_path = input("Enter Your Folder path: ")

# new_folder_path = input("Enter the new folder to save path: ")

# fix_and_update_notebook_version(folder_path, new_folder_path)

#*-----*#

fix_and_update_notebook_version(folder_path)



