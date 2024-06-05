from fpdf import FPDF
import os

class PDFManager:
    def __init__(self, filename):
        self.filename = filename
        self.downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        self.file_path = os.path.join(self.downloads_folder, self.filename)
        self.text_list = []

    def add_text(self, new_text):
        self.text_list.append(new_text)
        self.generate_pdf()

    def generate_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 12)
        for text in self.text_list:
            pdf.multi_cell(0, 10, text)
        pdf.output(self.file_path)
        print(f"PDF updated and saved to {self.file_path}")
