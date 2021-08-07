"""
XKCD Comics Downloader and Reader
"""

# Import Modules
import json
import requests
import csv
import datetime
import os
import shutil
from zipfile import ZipFile

# Read the current edition of XKCD comics and store as a dictionary
current_edition = json.loads(requests.get('http://xkcd.com/info.0.json').text)

# Define latest edition and set range to store in CSV
current_id = current_edition["num"]

# Check whether directory exists in script folder, and if not, creates a new working directory
if not os.path.exists('comics'):
    os.mkdir('comics')

# Set working_working directory as current folder
os.chdir('comics')

# Write and append to CSV file for the most recent 7 comics
with open('comics.csv', 'w', newline='') as csvfile:

    # Define and write column headers to CSV file
    csv_header = ["date", "id", "title", "url", "alt text"]
    writer = csv.writer(csvfile)
    writer.writerow(csv_header)

    # Write metadata to CSV file
    for id in range(current_id - 6, current_id + 1):

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

        # Append formatted metadata to CSV file
        writer = csv.writer(csvfile)
        writer.writerow(formatted_metadata)

        # Request, label and download image file
        img_file = requests.get(source_metadata['img'])
        img_filename = f'{id}.png'

        open(img_filename, 'wb').write(img_file.content)

# Create zip file and delete directory
os.chdir('..')

with ZipFile('comics.zip', 'w') as zip:
   for path, directories, files in os.walk('comics'):
       for file in files:
           file_name = os.path.join(path, file)
           zip.write(file_name)

# Clean up working folder
shutil.rmtree('comics')

print("Zipping complete, the program will now end")