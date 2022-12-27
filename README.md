# Convert VTT to SRT
Python script for converting WebVTT (.vtt) files to SubRip Text (.srt) files.
The script can be run on a directory and its subdirectories, converting all VTT files found within.

## Requirements
To use this script, you will need to have the following libraries installed:
- webvtt

You can install these libraries using pip:

```python
pip install webvtt
```

## Usage

To use the script, simply run the following command:
```python
python convert_vtt_to_srt.py
```
This will convert all .vtt files in the current directory and its subdirectories to .srt files.

## You can create a batch file to run the Python script quickly.
To create a batch file to run the Python script, follow these steps:

1. Open a text editor (such as Notepad) and type the following commands:
```commandline
@echo off
python convert_vtt_to_srt.py
```
2. Save the file with the `.bat` extension (e.g., `convert.bat`).

3. To run the script, double-click the batch file. This will open a command prompt window, execute the Python script.
