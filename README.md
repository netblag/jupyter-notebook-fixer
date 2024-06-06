# Jupyter Notebook Fixer

<p align="center">
  <img src="https://i.imgur.com/lalSwBh.png" alt="Sample1" width="700" height="300"/>
</p>

---
## Introduction
In the world of data and computer science, Jupyter Notebook serves as one of the primary tools for data analysis and executing Python code. However, sometimes we encounter issues that result in corruption of notebook files, making it difficult to open or reuse them. This project is created to address this problem and update Jupyter Notebook files to a newer version.

## Problem
Sometimes, you may have a set of .ipynb files that are corrupted due to various reasons or fail to open properly due to the use of older versions. This issue can lead to data loss, incomplete analyses, and wasted valuable time. In such situations, manually inspecting and correcting each notebook file is time-consuming and tiresome.

## Solution
This project provides a simple and efficient script to update and fix all notebook files in a directory. The script automatically updates .ipynb files to version 4 and attempts to recover the file content and create a new notebook if an error occurs while reading the file. This approach ensures that all your notebook files are up-to-date and usable.

---

## Requirements

### To use this project, you need the following:

- #### Python 3.x
- #### nbformat library

You can install the required library using pip:

```sh
 pip install nbformat
```
***
## Installation

### To use this script, follow these steps:

- #### 1. Clone this repository:

```sh
git clone https://github.com/netblag/jupyter-notebook-fixer.git
```

- #### 2. Navigate to the project directory:

```sh
cd jupyter-notebook-fixer
```
***
## Usage

- #### 1. Replace the directory path containing your notebook files in the script.
- #### 2. Run the script:

```sh
python update_notebook_version.py
```

#### This script checks and updates all .ipynb files in the specified directory to version 4. It also fixes corrupted files if needed.
***

## Advantages
### Using this script offers several advantages, including:

- #### Time-saving: Automatically updates all files instead of manually inspecting and correcting each one.

- #### Compatibility assurance: By updating all files to version 4, it ensures compatibility with the latest Jupyter Notebook version.

- #### Ease of use: Simply specify the directory path containing your files and run the script.

### Contribution

#### If you'd like to contribute to this project, you can help by submitting pull requests or reporting issues to improve it. We welcome any feedback and suggestions.

### License
#### Copyright (c) 2024 [netblag](https://github.com/netblag)
#### This project is licensed under the [MIT](https://github.com/netblag/jupyter-notebook-fixer/blob/main/License) License, so you can freely use and share it with others.

<p align="center">
  <a href="https://github.com/netblag">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/github/ccc?viewbox=auto" />
      <source media="(prefers-color-scheme: light)" srcset="https://cdn.simpleicons.org/github?viewbox=auto" />
      <img alt="GitHub" height="90" src="https://cdn.simpleicons.org/github?viewbox=auto" />
    </picture>
  </a>
  





