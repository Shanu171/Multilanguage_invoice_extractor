# Multi-Language Invoice Extractor
This is a multi-language invoice extractor app built using Streamlit and Google Gemini-1.5-Flash-Latest. The app allows users to upload an invoice image in any language and ask questions about the invoice (such as amount, GST number, address, etc.). The AI-powered model processes the invoice and provides answers based on the content of the uploaded invoice.

Features
Multi-Language Support: Extracts and understands invoice data in various languages.
Key Data Extraction: Extracts details such as:
Total Amount
Address
GST Number
Date
Invoice Number
Interactive Q&A: Ask specific questions about the uploaded invoice and get relevant answers.
Requirements
Python 3.x
Streamlit
Google Cloud API (for Google Gemini Model)
Tesseract OCR (if you plan to use OCR for text extraction, though this app leverages Google's model for extraction)
Other necessary Python libraries like Pillow, python-dotenv, etc.
Installation
Step 1: Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/invoice-extractor.git
cd invoice-extractor
Step 2: Install Dependencies
Use the following command to install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Step 3: Set Up Google Cloud API Key
Go to the Google Cloud Console, create a new project, and enable the Gemini API for the project.

Create an API key and store it securely.

Set the environment variable GOOGLE_API_KEY to your API key:

On Linux/macOS:

bash
Copy code
export GOOGLE_API_KEY="your-api-key"
On Windows (Command Prompt):

bash
Copy code
set GOOGLE_API_KEY="your-api-key"
Ensure you have a .env file in the root directory with the following content:

text
Copy code
GOOGLE_API_KEY=your-api-key
Step 4: Run the Application
Run the Streamlit app locally with the following command:

bash
Copy code
streamlit run app.py
This will start the app at http://localhost:8501/.

How to Use
Upload Invoice Image: On the homepage, upload an image of the invoice (in JPG, JPEG, or PNG format).
Enter a Question: Type your question in the provided input field (e.g., "What is the total amount?").
Get the Answer: Click on the "Tell me about the invoice" button to get a response based on the invoice details.
The app uses Google Gemini-1.5-Flash-Latest to generate a response based on the invoice content.

Example Queries
Here are some example questions you can ask after uploading an invoice:

"How much is the total amount?"
"What is the invoice number?"
"What is the GST number?"
"Where is the supplier's address?"
"What is the date of the invoice?"
Code Explanation
get_gemmini_response()
This function communicates with the Google Gemini-1.5-Flash-Latest model to generate a response based on the uploaded invoice image and a provided prompt.

input_image_details()
This function handles the file upload and converts the image into a format suitable for interaction with the Gemini API. The uploaded file is processed into a byte array.

Streamlit Interface
st.file_uploader(): Allows users to upload the invoice image.
st.text_input(): Takes the user's question as input.
st.button(): Triggers the process of sending the query to the model after the user uploads an invoice and enters a question.
st.subheader() and st.write(): Displays the generated response from the model.
API Documentation
If you'd like to integrate the invoice extractor functionality into your own system, here’s the API structure:

Endpoint: /extract_invoice
Method: POST
Parameters:
image: (multipart/form-data) The invoice image to be uploaded.
Endpoint: /ask_question
Method: POST
Parameters:
question: (string) The question you want to ask about the uploaded invoice.
Contributing
Feel free to fork the repository, submit issues, or create pull requests. If you are contributing, please ensure your code follows the existing style and includes tests where applicable.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Google Gemini API: For providing the language model that powers the Q&A functionality.
Streamlit: For providing an interactive framework to build the web app.
python-dotenv: For securely loading environment variables like the API key.
