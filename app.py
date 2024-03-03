import streamlit as st
import os
import fitz  # PyMuPDF
from datetime import datetime asd;flasj

# Ensure uploads folder exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

def save_uploaded_file(uploaded_file):
    try:
        with open(os.path.join('uploads', uploaded_file.name), "wb") as f:
            f.write(uploaded_file.getbuffer())
        return True
    except Exception as e:
        return False

def extract_text_from_pdfs(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            doc = fitz.open(pdf_path)
            print(f"Text from {filename}:")
            for page in doc:
                print(page.get_text())
            print("\n--- End of Document ---\n")
            doc.close()

def main():
    st.title("PDF Upload and Text Extraction App")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        if save_uploaded_file(uploaded_file):
            st.success("File saved successfully.")
        else:
            st.error("Failed to save file.")

    if st.button("Train"):
        st.write("Extracting text from PDFs...")
        extract_text_from_pdfs('uploads')

    st.write("## Ask a Question")
    user_question = st.text_input("Enter your question here:")
    if user_question:
        # Implement your logic to generate a HTML response based on the question
        # For demonstration, we're just echoing the question in a simple HTML
        html_response = f"<h1> lala bhai</h1>"
        st.markdown(html_response, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
