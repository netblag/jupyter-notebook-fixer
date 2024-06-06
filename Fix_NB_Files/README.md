<p align="center">
  
<a href="https://github.com/netblag/jupyter-notebook-fixer/tree/main" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/jupyter/jupyter-original.svg" alt="jupyter" width="100" height="100"/>

---
# Updating Notebook Version

### Sometimes, you might have a bunch of corrupted .ipynb files that seem to be time-consuming to fix manually. Instead of going through each file one by one, you can place all `.ipynb files in a folder` and use this script to fix them all at once.
***

## How it works

- #### 1. List Files: The script lists all files and folders in the provided directory.

- #### 2. Find Notebooks: For each file found, it checks if it ends with '.ipynb'.

- #### 3. Open and Read: If it's a notebook file, it opens and reads the file using nbformat.

- #### 4. Update Version: It updates the notebook to version 4.

- #### 5. Save Changes: The updated notebook is then saved with version 4.
***

## Requirements

- ### Python: Ensure `Python` is installed on your system.

- ### Jupyter Notebook: The script relies on nbformat module, which is part of the Jupyter ecosystem. Make sure Jupyter is installed (`pip install jupyter`).

- #### Folder Path: Replace `YOUR_FOLDER_PATH` in the script with the path of the directory containing the notebooks you want to update.
- #### You can directly enter the folder path in the cmd and then use the following code to choose a new path for saving files:

```sh

new_folder_path = input("Please enter the new path for saving files: ")
fix_and_update_notebook_version(folder_path, new_folder_path)

```


***

## Usage

- #### 1. Replace `YOUR_FOLDER_PATH` with the actual path of the directory containing your notebooks. Additionally, you can directly enter the folder path in `CMD`.
- #### 2. Run the script.
- #### 3. That's it! Your notebook files should now be updated to version 4.
---

<p align="center">
  <a href="https://github.com/netblag">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/github/ccc?viewbox=auto" />
      <source media="(prefers-color-scheme: light)" srcset="https://cdn.simpleicons.org/github?viewbox=auto" />
      <img alt="GitHub" height="90" src="https://cdn.simpleicons.org/github?viewbox=auto" />
    </picture>
  </a>
  
