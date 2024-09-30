<h1>Hindi-English Translator using OCR</h1>

<p>This project is a web-based application that allows users to upload images containing text in Hindi and English. The application performs Optical Character Recognition (OCR) to extract the text from the image and provides a translation of the recognized Hindi text into English. Additionally, it offers a search functionality to highlight specific words within the extracted text.</p>

<h2>Key Features</h2>
<ul>
    <li>Supports both Hindi and English OCR using <code>EasyOCR</code>.</li>
    <li>Allows users to upload images in <code>jpg</code>, <code>jpeg</code>, and <code>png</code> formats.</li>
    <li>Displays extracted text in a text area for easy reading.</li>
    <li>Provides a search feature that highlights specific words in the extracted text.</li>
    <li>Enables users to download the extracted text as a <code>JSON</code> file.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li><strong>Streamlit</strong> - Web application framework for Python.</li>
    <li><strong>EasyOCR</strong> - Optical Character Recognition library.</li>
    <li><strong>PIL</strong> - Python Imaging Library for image processing.</li>
    <li><strong>Regex</strong> - For search and highlight functionality.</li>
</ul>

<h2>Project Structure</h2>
<pre>
project-root/
│
├── ocr_model.py          # Contains the OCRModel class for text extraction
├── app.py                # Main application file for Streamlit
├── README.html           # This README file
└── requirements.txt      # Python dependencies
</pre>

<h2>How to Run the Project</h2>
<p>Follow the steps below to run the Hindi-English OCR project locally:</p>

<ol>
    <li><strong>Clone the repository:</strong>
        <pre><code>git clone https://github.com/your-repo/hindi-english-ocr.git</code></pre>
    </li>
    <li><strong>Navigate to the project folder:</strong>
        <pre><code>cd hindi-english-ocr</code></pre>
    </li>
    <li><strong>Install the required dependencies:</strong>
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li><strong>Run the Streamlit app:</strong>
        <pre><code>streamlit run app.py</code></pre>
    </li>
    <li><strong>Upload an image</strong> in the provided uploader section and click "Perform OCR".</li>
    <li><strong>Search for keywords</strong> and download the extracted text as JSON if needed.</li>
</ol>

<h2>OCR Model</h2>
<p>The OCR model is built using <strong>EasyOCR</strong>, which supports multiple languages including Hindi and English. The model automatically detects and extracts text from images, handling mixed-language text scenarios.</p>

<h2>Search and Highlight</h2>
<p>The application provides a search box where users can enter keywords to search within the extracted text. Matches are highlighted with a <span class="highlight">yellow background</span> and the number of matches is displayed.</p>

<h2>Download Extracted Text</h2>
<p>After performing OCR, the user can download the extracted text as a <code>JSON</code> file by clicking on the "Download JSON" button.</p>

<h2>Requirements</h2>
<ul>
    <li><code>Python 3.7+</code></li>
    <li><code>Streamlit</code></li>
    <li><code>EasyOCR</code></li>
    <li><code>Pillow</code> (PIL)</li>
</ul>

<h2>Usage Example</h2>
<p>Once the application is running, follow these steps:</p>
<ol>
    <li>Click "Choose an image file" to upload an image.</li>
    <li>Click "Perform OCR" to extract the text from the image.</li>
    <li>The extracted text will be displayed in the text area below.</li>
    <li>To search for a word in the text, enter the keyword in the search box and press Enter. The occurrences will be highlighted.</li>
    <li>Click the "Download JSON" button to save the extracted text.</li>
</ol>

<h2>Contributing</h2>
<p>If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please make sure your code follows best practices and is well documented.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for more details.</p>
