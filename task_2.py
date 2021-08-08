"""
XKCD ZIP File Reader - Edition and Image Counter

This script is to be used with a Zip file created by task_1.py
"""

# Import Modules
import os
import shutil
import glob
from zipfile import ZipFile
import pandas as pd
import datetime
from collections import Counter

# Define constant directories and files
COMICS_CSV = 'comics/comics.csv'
COMICS_DIR = 'comics'
COMICS_ZIP = 'comics.zip'

# Expand Zip File
with ZipFile(COMICS_ZIP, 'r') as zip:
    zip.extractall()

# Read CSV using Pandas module
read_csv = pd.read_csv(COMICS_CSV)

# Filter date column and convert the column to a list
date = read_csv['date'].tolist()

weekday = []
# Convert the date list into a weekday list
for i in range(len(date)):
    date_string = date[i]
    date_format = "%Y-%m-%d"

    # Convert the string from the CSV into datetime and transform this to a weekday
    weekday.append(datetime.datetime.strptime(date_string, date_format).strftime('%A'))

# Count the number of instances of each weekday
counter = Counter(weekday)

# Print the results
print('The numbers of comics published on the day of the week are:')
for key, value in counter.items():
    print(key, ': ', value)

# Count image files and print to terminal
image_counter = len(glob.glob1('', "*.png"))
print(f'\nThere are {image_counter} images in the ZIP file.')

# Clean up working folder
shutil.rmtree(COMICS_DIR)
