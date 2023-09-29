import cv2
import pytesseract
import re
import os

def prepareImages(phrase: str, file: str, offset: int):
    image = cv2.imread("./images/" + file)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    data = pytesseract.image_to_data(gray_image, output_type='dict')

    target_words = phrase.split(" ")

    text_without_special_chars = [re.sub(r'[^\w\s]', '', text) for text in data['text']]

    combined_x_min = float('inf')
    combined_x_max = 0
    combined_y_min = float('inf')
    combined_y_max = 0

    found = 0

    for i, word in enumerate(text_without_special_chars):
        if target_words[0] in word:
            if text_without_special_chars[i:i+len(target_words)] == target_words:
                x_min = data['left'][i]
                x_max = x_min + data['width'][i]
                y_min = data['top'][i]
                y_max = y_min + data['height'][i]

                combined_x_min = min(combined_x_min, x_min)
                combined_x_max = max(combined_x_max, x_max)
                combined_y_min = min(combined_y_min, y_min)
                combined_y_max = max(combined_y_max, y_max)
                
                if found == 0:
                    found = i
        elif found != 0 and (found + len(target_words)) > i:
            x_min = data['left'][i]
            x_max = x_min + data['width'][i]
            y_min = data['top'][i]
            y_max = y_min + data['height'][i]

            combined_x_min = min(combined_x_min, x_min)
            combined_x_max = max(combined_x_max, x_max)
            combined_y_min = min(combined_y_min, y_min)
            combined_y_max = max(combined_y_max, y_max)
        elif found != 0:
            break

    crop_x_min = max(0, combined_x_min - offset)
    crop_x_max = min(image.shape[1], combined_x_max + offset)
    crop_y_min = max(0, combined_y_min - offset)
    crop_y_max = min(image.shape[0], combined_y_max + offset)

    cropped_image = image[crop_y_min:crop_y_max, crop_x_min:crop_x_max]

    resized_image = cv2.resize(cropped_image, (1920, 1080))
    cv2.imwrite(f'./cache/cropped/{file}', resized_image)