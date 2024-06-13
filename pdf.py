import fitz  


pdf_document = "policy-booklet-0923.pdf"
document = fitz.open(pdf_document)


text = ""
for page_num in range(document.page_count):
    page = document.load_page(page_num)
    text += page.get_text()


with open("extracted_text.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("Text extraction completed successfully.")
