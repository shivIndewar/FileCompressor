File Compressor

This Python project allows you to select multiple files and a destination folder, then compress those files into a specified location using a simple graphical user interface (GUI) created with the FreeSimpleGUI package.

Requirements

Python 3.6 or higher

FreeSimpleGUI Python package

zipfile (standard Python library for file compression)

You can install the necessary dependencies with the following command:

pip install FreeSimpleGUI

Project Structure
FileCompressor/
│
├── .venv/               # Virtual environment (optional)
├── FileCompressor.py    # Main script for the GUI and file compression logic
├── zip_creator.py       # Contains file compression logic
└── README.md            # This file

How to Use

Clone the repository:

git clone https://github.com/your-username/FileCompressor.git
cd FileCompressor


Run the program:

python FileCompressor.py


GUI Instructions:

Select files to compress: Click the "Choose" button to browse and select multiple files you want to compress.

Select the destination folder: Click the "Choose" button to specify the folder where you want the compressed file to be saved.

Compress: Once you've selected the files and destination folder, click the "Compress" button to start the compression process.

App out put
<img width="959" height="502" alt="image" src="https://github.com/user-attachments/assets/901e0a9f-260f-4962-8f89-949acc523d5c" />

