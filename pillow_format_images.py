# PILLOW/PIL to reformat images (open/rotate/resize/save) (from nano)
'''
#!/usr/bin/env python3
from PIL import Image
import os

source = "/opt/icons"          # folder with the original images
destination = "/opt/icons_new" # folder to save processed images

# Create destination folder if it doesn't exist
if not os.path.exists(destination):
    os.makedirs(destination)

for filename in os.listdir(source):
    if not filename.lower().endswith((".png", ".jpg", ".jpeg", ".tiff")):
        continue  # skip non-image files

    # Build full file path
    filepath = os.path.join(source, filename)

    # Open the image
    with Image.open(filepath) as im:
        # Process the image
        new_im = im.rotate(-90).resize((128, 128)).convert("RGB")

        # Build output filename (force .jpeg)
        new_filename = os.path.splitext(filename)[0] + ".jpeg"
        output_path = os.path.join(destination, new_filename)

        # Save the processed image
        new_im.save(output_path, "JPEG")

#fails due to lab issues with file names missing .extension
'''


#!/usr/bin/env python3

from PIL import Image
import os

source = "/opt/icons"
destination = "/opt/icons_new"

# Create destination folder if it doesn't exist
if not os.path.exists(destination):
    os.makedirs(destination)

for filename in os.listdir(source):
    filepath = os.path.join(source, filename)

    # Try to open the file as an image
    try:
        with Image.open(filepath) as im:
            new_im = im.rotate(-90).resize((128, 128)).convert("RGB")

            # Save as .jpeg
            new_filename = os.path.splitext(filename)[0] + ".jpeg"
            output_path = os.path.join(destination, new_filename)

            new_im.save(output_path, "JPEG")
    except:
        # Skip files Pillow cannot open
        continue
