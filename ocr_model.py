import easyocr
from PIL import Image
import numpy as np
import re

class OCRModel:
    def __init__(self):
        # Initialize the reader for English and Hindi, using GPU if available
        self.reader = easyocr.Reader(['en', 'hi'], gpu=True)

    def process_image(self, image: Image.Image) -> str:
        # Convert PIL Image to numpy array
        image_np = np.array(image)
        
        # Perform OCR and get the structured output
        result = self.reader.readtext(image_np, detail=1, paragraph=False)
        
        # Separate English and Hindi text
        english_text = []
        hindi_text = []

        for item in result:
            text = item[1]
            if self._is_language(text, 'en'):
                english_text.append(text)
            elif self._is_language(text, 'hi'):
                hindi_text.append(text)

        # Format output by joining the separated texts with new lines
        english_output = "\n".join(english_text)
        hindi_output = "\n".join(hindi_text)

        # Returning both English and Hindi output, with line breaks for each
        return f"English:\n{english_output}\n\nHindi:\n{hindi_output}"

    def _is_language(self, text: str, lang: str) -> bool:
        if lang == 'en':
            # Check if the text contains only English characters (basic ASCII range)
            return bool(re.match(r'^[a-zA-Z0-9\s,.\'!?"-]+$', text))
        elif lang == 'hi':
            # Check if the text contains Devanagari script (Hindi)
            return all('\u0900' <= char <= '\u097F' or char.isspace() for char in text)
        return False
