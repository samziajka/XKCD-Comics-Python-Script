"""
ZIP File Reader - Edition and Image Counter
"""

# Import Modules
import os
import shutil
import glob
from zipfile import ZipFile
import pandas as pd
import datetime
from collections import Counter

# Expand Zip File
with ZipFile('comics.zip', 'r') as zip:
    zip.extractall()

# Navigate to Comics folder
os.chdir('comics')

# Read CSV using Pandas module and filter date column
read_csv = pd.read_csv('comics.csv')

# Convert the column to a list
date = read_csv['date'].tolist()

# Define a counter for a while loop to transform the datetime into a day of the week
i = 1
weekday = []

# Convert the date list into a weekday list
while i < len(date):
    date_string = date[i]
    date_format = "%Y-%m-%d"

    # Convert the string from the CSV into datetime and transform this to a weekday
    weekday.append(datetime.datetime.strptime(date_string, date_format).strftime('%A'))
    i += 1

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
os.chdir('..')
shutil.rmtree('comics')