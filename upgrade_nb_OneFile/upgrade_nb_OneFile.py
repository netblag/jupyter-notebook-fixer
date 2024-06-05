"""
# [🄽🄴🅃🄱🄻🄰🄶](https://github.com/netblag)
---
# Jupyter Notebook Fixer

---
### This code reads a Jupyter notebook file named File-Name.ipynb and converts it to version 4 
### (if it has an older version) and then saves it with a new name File-Name-Update.ipynb.
### This ensures the notebook file is converted to the latest compatible version, resolving
### potential issues caused by older versions.

---

## Steps:

- 1. Importing the `nbformat` library
- 2. Loading the notebook file
- 3. Saving the notebook file with the latest version
---

- ### ! This code only accepts one file (.ipynb)

---

## [GitHub](https://github.com/netblag/jupyter-notebook-fixer)
---
"""

import nbformat

# Load the notebook
with open('File-Name.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Save the notebook with the latest version
with open('File-Name-Updated.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)






