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

def update_notebook_version(folder_path):
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
                with open(file_path, 'w', encoding='utf-8') as f:
                    nbformat.write(notebook, f)

                print(f"{file_path} has been updated to version 4.")

# Replace your directory path
folder_path = r'YOUR_FOLDER_PATH'
update_notebook_version(folder_path)


