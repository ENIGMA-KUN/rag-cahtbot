import fitz  # PyMuPDF

# Open the PDF file
pdf_document = "policy-booklet-0923.pdf"
document = fitz.open(pdf_document)

# Extract text from each page
text = ""
for page_num in range(document.page_count):
    page = document.load_page(page_num)
    text += page.get_text()

# Save the text to a file for further processing
with open("extracted_text.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("Text extraction completed successfully.")
