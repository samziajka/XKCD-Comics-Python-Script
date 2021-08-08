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

There 