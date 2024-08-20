# resdetect.py
# Simple helper tool to output a list containing the resolution of all images in the current directory
# Kevin Anderson 8/20/24
#
# source ~/dev/resdetect/venv/bin/activate
# python ~/dev/resdetect/resdetect.py

from PIL import Image
from PIL import UnidentifiedImageError
from pathlib import Path
from tabulate import tabulate

currentdir = Path.cwd()
files = Path(currentdir).glob('*')
table = []

# Iterate through all the files in the current working directory
for file in files:
    if file.is_file():
        try:
            with Image.open(file) as image:
                width, height = image.size
                format = image.format
                filename = Path(file).name
                listItem = [filename, format, width, height]
                table.append(listItem)

        except UnidentifiedImageError:
            print(f"PIL unable to determine file type: {file}")

        except Exception as e:
            print(f"Error has occurred: {e}")

# Print this cleanly!            
print(tabulate(table, headers=["Filename", "Format", "Width", "Height"], tablefmt="github"))

with open('resolutions.txt', 'w') as f:
    print(tabulate(table, headers=["Filename", "Format", "Width", "Height"], tablefmt="github"), file=f)