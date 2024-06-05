import PyPDF2
import os

def merge_pdfs(output_path, *input_paths):
    merger = PyPDF2.PdfMerger()
    
    for path in input_paths:
        merger.append(path)
    
    with open(output_path, 'wb') as f:
        merger.write(f)

# Example usage:
input_folder = r'C:\Users\Harish Paramathma\git\General_Scripts\merger'  # Change this to the folder containing your PDF files
output_path = 'merged_pdf.pdf'

pdf_files = [file for file in os.listdir(input_folder) if file.endswith('.pdf')]
input_paths = [os.path.join(input_folder, file) for file in pdf_files]

merge_pdfs(output_path, *input_paths)
