from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("files/*.txt")

pdf = FPDF()

for filepath in filepaths:
    pdf.set_font("Times", size=24, style="B")
    pdf.add_page()
    filename = Path(filepath).stem
    print(filename)
    pdf.cell(txt=filename.title(), w=297, h=13, ln=1)
    with open(filepath, 'r') as file:
        data = file.read()

    pdf.set_font("Times", size=12)
    pdf.multi_cell(w=0, h=8, txt=data)

pdf.output("output.pdf")