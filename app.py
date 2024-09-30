import streamlit as st
from PIL import Image
from ocr_model import OCRModel  # Assuming you have saved the OCRModel class in a file named `ocr_model.py`
import json
import re

# Function to search and highlight keywords in text
def search_and_highlight(text, keyword):
    if not text or not keyword:
        return text, []
    
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    # Highlight the search keyword with a yellow mark using inline CSS
    highlighted_text = pattern.sub(lambda m: f"<mark style='background-color: #fafa00;'>{m.group()}</mark>", text)
    
    matches = pattern.finditer(text)
    results = [m.start() for m in matches]
    
    return highlighted_text, results

# Caching the OCRModel object to avoid reloading on every action
@st.cache_resource
def get_ocr_model():
    return OCRModel()

# Streamlit App starts here
st.title("Hindi-English Translator using OCR")

# Initialize session state to store the OCR text and image
if 'ocr_text' not in st.session_state:
    st.session_state.ocr_text = ""
if 'image' not in st.session_state:
    st.session_state.image = None
if 'last_uploaded_file' not in st.session_state:
    st.session_state.last_uploaded_file = None

# Load the OCR model
ocr_model = get_ocr_model()

# Upload image through Streamlit
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

# Check if a new image is uploaded
if uploaded_file is not None and uploaded_file != st.session_state.last_uploaded_file:
    st.session_state.image = Image.open(uploaded_file)
    st.session_state.ocr_text = ""  # Reset OCR text when a new image is uploaded
    st.session_state.last_uploaded_file = uploaded_file

# Display uploaded image
if st.session_state.image is not None:
    st.image(st.session_state.image, caption="Uploaded Image", use_column_width=True)

    # Perform OCR when the button is pressed or when OCR text is already available
    if st.button("Perform OCR") or st.session_state.ocr_text:
        if not st.session_state.ocr_text:
            with st.spinner("Processing OCR..."):
                st.session_state.ocr_text = ocr_model.process_image(st.session_state.image)

        # Display the extracted OCR text
        st.subheader("Extracted Text:")
        text_area = st.empty()
        text_area.text_area("", st.session_state.ocr_text, height=200)
        
        # Save the extracted text as a JSON file
        json_output = json.dumps({"extracted_text": st.session_state.ocr_text}, ensure_ascii=False, indent=2)
        st.download_button(
            label="Download JSON",
            data=json_output,
            file_name="extracted_text.json",
            mime="application/json"
        )
        
        # Search functionality in the extracted text
        st.subheader("Search in Extracted Text")
        search_keyword = st.text_input("Enter a keyword to search")

        if search_keyword:
            # Highlight the found keywords
            highlighted_text, search_results = search_and_highlight(st.session_state.ocr_text, search_keyword)
            if search_results:
                st.markdown(f"Found {len(search_results)} matches.")
                text_area.markdown(highlighted_text, unsafe_allow_html=True)
                
                # Displaying search results with line numbers
                st.subheader("Search Results:")
                lines = st.session_state.ocr_text.split('\n')
                for i, pos in enumerate(search_results):
                    line_number = st.session_state.ocr_text.count('\n', 0, pos) + 1
                    line_content = lines[line_number - 1]
                    st.markdown(f"- Match {i+1} (Line {line_number}): ...{line_content}...")
            else:
                st.info("No matching results found.")

st.markdown("---")
