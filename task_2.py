"""
ZIP File Reader - Edition and Image Counter
"""

# Import Modules
import os
import shutil
import glob
from zipfile import ZipFile
import pandas as pd
from collections import Counter

# Expand Zip File
with ZipFile('comics.zip', 'r') as zip:
    zip.extractall()

# Navigate to Comics folder
os.chdir('comics')

# Read CSV using Pandas module and filter date column
read_csv = pd.read_csv('comics.csv')

# Convert the column to a list
date_filter = read_csv['date'].tolist()

counter = Counter(date_filter)

print('The numbers of comics published on the day of the week are:')
for key, value in counter.items():
    print(key, ': ', value)

# Count image files and print to terminal
image_counter = len(glob.glob1('', "*.png"))
print(f'\nThere are {image_counter} images in the ZIP file.')

# Clean up working folder
os.chdir('..')
shutil.rmtree('comics')