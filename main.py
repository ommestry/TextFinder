import PyPDF2

def find_text_in_pdf(file_path, search_text):
    with open('D:\\intership\\Down To Earth 16-30 June 2023.pdf', 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        num_pages = len(pdf.pages)

        for page_number in range(num_pages):
            page = pdf.pages[page_number]
            text = page.extract_text()

            sentences = text.split('. ')

            for sentence in sentences:
                if search_text in sentence:
                    print(sentence.strip())



pdf_file_path = 'path/to/your/pdf/file.pdf'
search_term = 'example text'

find_text_in_pdf("", "Earth")
