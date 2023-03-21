import os
import sys
from PIL import Image

# check for correct number of arguments
if len(sys.argv) != 2:
    print("usage: python webp2jpg.py <input_file_path>")
    sys.exit(1)

# declare given path
input_path = sys.argv[1]

# check if its a webp file
if not input_path.lower().endswith(".webp"):
    print("error: input file is not a webp image.")
    sys.exit(1)

# create output file path
input_dir, input_file = os.path.split(input_path)
output_file = os.path.splitext(input_file)[0] + "(converted).jpg"
output_path = os.path.join(input_dir, output_file)

# open webp file, convert it into jpeg and save it to the same directory
with Image.open(input_path) as img:
    img = img.convert("RGB")
    img.save(output_path, "JPEG")
