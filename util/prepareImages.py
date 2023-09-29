import cv2
import pytesseract
import re
import os

def prepareImages(phrase: str, file: str, offset: int):
    image = cv2.imread("./images/" + file)

    # Convert the image to grayscale (optional but can help improve OCR)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    data = pytesseract.image_to_data(gray_image, output_type='dict')

    # Split the target phrase into words
    target_words = phrase.split(" ")

    text_without_special_chars = [re.sub(r'[^\w\s]', '', text) for text in data['text']]

    combined_x_min = float('inf')
    combined_x_max = 0
    combined_y_min = float('inf')
    combined_y_max = 0

    found = 0

    # Iterate through the lines (individual words) of OCR text
    for i, word in enumerate(text_without_special_chars):
        # Check if the current word matches the first word of the target phrase
        if target_words[0] in word:
            # Check if the following words also match the target phrase
            if text_without_special_chars[i:i+len(target_words)] == target_words:
                # Calculate the bounding box for the matched words in the line
                x_min = data['left'][i]
                x_max = x_min + data['width'][i]
                y_min = data['top'][i]
                y_max = y_min + data['height'][i]

                # Update the combined bounding box
                combined_x_min = min(combined_x_min, x_min)
                combined_x_max = max(combined_x_max, x_max)
                combined_y_min = min(combined_y_min, y_min)
                combined_y_max = max(combined_y_max, y_max)
                
                if found == 0:
                    found = i
        elif found != 0 and (found + len(target_words)) > i:
            # Calculate the bounding box for the matched words in the line
            x_min = data['left'][i]
            x_max = x_min + data['width'][i]
            y_min = data['top'][i]
            y_max = y_min + data['height'][i]

            # Update the combined bounding box
            combined_x_min = min(combined_x_min, x_min)
            combined_x_max = max(combined_x_max, x_max)
            combined_y_min = min(combined_y_min, y_min)
            combined_y_max = max(combined_y_max, y_max)
        elif found != 0:
            break

    # Calculate the new coordinates for cropping
    crop_x_min = max(0, combined_x_min - offset)
    crop_x_max = min(image.shape[1], combined_x_max + offset)
    crop_y_min = max(0, combined_y_min - offset)
    crop_y_max = min(image.shape[0], combined_y_max + offset)

    # Crop the image
    cropped_image = image[crop_y_min:crop_y_max, crop_x_min:crop_x_max]

    # Resize the cropped image to 1920x1080
    resized_image = cv2.resize(cropped_image, (1920, 1080))
    cv2.imwrite(f'./cache/cropped/{file}', resized_image)