# XKCD Comics Processing Scripts

Two scripts are provided to interact with XKCD comics, these are titled:

- `script_1.py`, and 
- `script_2.py`

## Script 1

`script_1.py` accesses the API of https://xkcd.com/ and extracts and formats metadata and downloads images.

The formatted metadata is stored as `comics.csv`.
The images are stored as PNG files with their respective ID numbers.

The CSV file and images are zipped up and working files are deleted.

If the ZIP file already exists, the script will open and analyse the contents of the file, and if the file is out of date, it will add 
new editions of the comic and update the metadata CSV.

## Script 2

`script_2.py` extracts and reads the contents of comics.zip.
The script summarises how many editions of XKCD comics were published on each day of the week, and how many image files exist in the zip file.

There is some basic error checking which will stop the script if the ZIP file does not exist, or if the CSV file does not exist.

# Requirements
Requirements to run the scripts can be found in `requirements.txt`