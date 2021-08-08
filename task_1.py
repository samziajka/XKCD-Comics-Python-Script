"""
XKCD Comics Downloader and Reader
"""

# Import Modules
import json
import sys
import requests
import csv
import datetime
import os
import shutil
from zipfile import ZipFile
import pandas as pd

# Define constant directories and files
COMICS_CSV = 'comics/comics.csv'
COMICS_DIR = 'comics'
COMICS_ZIP = 'comics.zip'

# Read the current edition of XKCD comics and store as a dictionary
site_response = requests.get('http://xkcd.com/nfo.0.json')

if not site_response.ok:
    print(f'There is an issue with the connection, error {site_response.status_code}.')
    sys.exit()

current_edition = json.loads(site_response.text)

# Define latest edition and set lower bound to store in CSV
CURRENT_ID = current_edition["num"]
lower_bound = CURRENT_ID - 6

# Check whether zip file exists in script folder
if not os.path.exists(COMICS_ZIP):

    # Check whether directory exists in script folder, and if not, creates a new working directory
    if not os.path.exists(COMICS_DIR):
        os.mkdir(COMICS_DIR)

    if not os.path.exists(COMICS_CSV):
        # If csv doesn't exist, write and append to CSV file for the most recent 7 comics
        with open(COMICS_CSV, 'w', newline='') as csvfile:

            # Define and write column headers to CSV file
            csv_header = ["date", "id", "title", "url", "alt text"]
            writer = csv.writer(csvfile)
            writer.writerow(csv_header)

    # Create new, updated zip file
    with ZipFile(COMICS_ZIP, 'w') as zip:
        for path, directories, files in os.walk(COMICS_DIR):
            for file in files:
                file_name = os.path.join(path, file)
                zip.write(file_name)

    # Clean up working folder
    shutil.rmtree(COMICS_DIR)

# If comics.zip exists, expand the zip file
with ZipFile(COMICS_ZIP, 'r') as zip:
    zip.extractall()

# Check whether directory exists in script folder, and if not, creates a new working directory
if not os.path.exists(COMICS_DIR):
    os.mkdir(COMICS_DIR)

# Check whether comics.csv currently exists in comics directory
if not os.path.exists(COMICS_CSV):
    # Write and append to CSV file for the most recent 7 comics
    with open(COMICS_CSV, 'w', newline='') as csvfile:
        # Define and write column headers to CSV file
        csv_header = ["date", "id", "title", "url", "alt text"]
        writer = csv.writer(csvfile)
        writer.writerow(csv_header)

# Read CSV using Pandas module and filter id column
read_csv = pd.read_csv(COMICS_CSV)

# Convert the ID column to a list
id_list = read_csv['id'].tolist()

# Define the latest ID if there is nothing in the list
csv_latest_id = CURRENT_ID - 7

# Write to the latest ID if the list has values
if not len(id_list) < 1:
    csv_latest_id = max(id_list)

# Count how many new editions are added to the zip file
append_counter = 0

# Set the lower bound for the for loop if the current ID does not equal the highest ID in the list
if csv_latest_id == CURRENT_ID:
    # Clean up working folder
    shutil.rmtree(COMICS_DIR)
    print("You're up to date, no new editions were added!")

else:
    # Define the lower bound for the for loop
    lower_bound = csv_latest_id + 1

    # Write metadata to CSV file
    for id in range(lower_bound, CURRENT_ID + 1):

        append_counter += 1

        # Define json URL and store as dict
        json_url = f'http://xkcd.com/{id}/info.0.json'
        source_metadata = json.loads(requests.get(json_url).text)

        # Format date to YYYY-MM-DD
        date = datetime.date(int(source_metadata['year']),
                             int(source_metadata['month']),
                             int(source_metadata['day']))

        # Generate comic URL
        comic_url = f'https://xkcd.com/{id}/'

        # Format metadata to date, id, title, url, alt text
        formatted_metadata = [str(date),
                              source_metadata['num'],
                              source_metadata['title'],
                              comic_url,
                              source_metadata['alt']]
        # Write and append to CSV file for the most recent 7 comics
        with open(COMICS_CSV, 'a', newline='') as csvfile:

            # Write formatted metadata to CSV file
            writer = csv.writer(csvfile)
            writer.writerow(formatted_metadata)

        # Request, label and download image file
        img_file = requests.get(source_metadata['img'])
        img_filename = f'comics/{id}.png'

        open(img_filename, 'wb').write(img_file.content)

    # Remove existing zip file
    os.remove(COMICS_ZIP)

    # Create new, updated zip file
    with ZipFile(COMICS_ZIP, 'w') as zip:
        for path, directories, files in os.walk(COMICS_DIR):
            for file in files:
                file_name = os.path.join(path, file)
                zip.write(file_name)

    # Clean up working folder
    shutil.rmtree(COMICS_DIR)

    print(f'{append_counter} editions of the comics were added to the zip file')
