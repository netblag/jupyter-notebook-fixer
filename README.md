# jupyter notebook fixer

---
<p align="center">
  <img src="https://i.imgur.com/lalSwBh.png" alt="Sample1" width="700" height="300"/>
</p>

---
## Introduction
In the world of data and computer science, Jupyter Notebook serves as one of the primary tools for data analysis and executing Python code. However, sometimes we encounter issues that result in corruption of notebook files, making it difficult to open or reuse them. This project is created to address this problem and update Jupyter Notebook files to a newer version.

Problem
Sometimes, you may have a set of .ipynb files that are corrupted due to various reasons or fail to open properly due to the use of older versions. This issue can lead to data loss, incomplete analyses, and wasted valuable time. In such situations, manually inspecting and correcting each notebook file is time-consuming and tiresome.

Solution
This project provides a simple and efficient script to update and fix all notebook files in a directory. The script automatically updates .ipynb files to version 4 and attempts to recover the file content and create a new notebook if an error occurs while reading the file. This approach ensures that all your notebook files are up-to-date and usable.

Requirements
To use this project, you need the following:

Python 3.x
nbformat library
You can install the required library using pip:

sh
Copy code
pip install nbformat
Installation
To use this script, follow these steps:

Clone this repository:
sh
Copy code
git clone https://github.com/netblag/jupyter-notebook-fixer.git
Navigate to the project directory:
sh
Copy code
cd jupyter-notebook-fixer
Usage
Replace the directory path containing your notebook files in the script.
Run the script:
sh
Copy code
python update_notebook_version.py
This script checks and updates all .ipynb files in the specified directory to version 4. It also fixes corrupted files if needed.

Advantages
Using this script offers several advantages, including:

Time-saving: Automatically updates all files instead of manually inspecting and correcting each one.
Compatibility assurance: By updating all files to version 4, it ensures compatibility with the latest Jupyter Notebook version.
Ease of use: Simply specify the directory path containing your files and run the script.
Contribution
If you'd like to contribute to this project, you can help by submitting pull requests or reporting issues to improve it. We welcome any feedback and suggestions.
