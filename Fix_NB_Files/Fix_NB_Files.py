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

def update_notebook_version(folder_path, new_folder_path):
    # Create a new folder if it doesn't exist
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

    # List all files and folders in the given directory
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.ipynb'):
                file_path = os.path.join(root, file)
                print(f"Updating {file_path} to version 4")

                # Open and read the notebook file
                with open(file_path, 'r', encoding='utf-8') as f:
                    notebook = nbformat.read(f, as_version=4)

                # Save the notebook file with version 4
                with open(os.path.join(new_folder_path, file), 'w', encoding='utf-8') as f:
                    nbformat.write(notebook, f)

                print(f"{file_path} has been updated to version 4.")
    
    print("Updated notebooks have been saved in the new folder.")

# Replace your directory path

#*------------------------------------------------------------------------------------------------*#
# If you want all files within the current folder to be updated and saved, activate this code:

# folder_path = r'YOUR_FOLDER_PATH'
#*------------------------------------------------------------------------------------------------*#

#*-----*#

# To facilitate precise execution of the script, you can use this code to specify the path and save the file in another directory.

folder_path = input("Enter Your Folder path: ")

# new_folder_path = input("Enter the new folder to save path: ")

# update_notebook_version(folder_path, new_folder_path)
#*-----*#

update_notebook_version(folder_path)


