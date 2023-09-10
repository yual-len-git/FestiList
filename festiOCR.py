import pytesseract
from PIL import Image
import sys

if len(sys.argv) != 2:
    print("Usage: python festival_lineup_reader.py <image_path>")
    sys.exit(1)

# Get the image file path from the command line argument
image_path = sys.argv[1]

try:
    # Load the festival poster image
    poster_image = Image.open(image_path)

    # Perform OCR on the image
    text = pytesseract.image_to_string(poster_image)

    # Define a function to extract the lineup from the OCR result
    def extract_lineup(text):
        # Split the text into lines
        lines = text.split('\n')

        # Iterate through the lines to find the lineup section
        lineup_found = False
        lineup = []

        for line in lines:
            # You may need to adapt the logic to match the festival poster's specific format
            if "Lineup" in line:
                lineup_found = True
                continue

            if lineup_found:
                if line.strip():  # Check if the line is not empty
                    lineup.append(line)

        return lineup

    # Extract the lineup from the OCR result
    lineup = extract_lineup(text)

    # Print the lineup
    for artist in lineup:
        print(artist)

except FileNotFoundError:
    print("Image not found. Please provide a valid file path.")
except Exception as e:
    print(f"An error occurred: {e}")
