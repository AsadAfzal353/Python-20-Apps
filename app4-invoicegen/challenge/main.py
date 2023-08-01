import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("app4-invoicegen/challenge/text_files/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_font(family="Times", size=24, style="B")

for filepath in filepaths:
    filename = Path(filepath).stem
    pdf.add_page()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=24, txt=filename.title(), ln=1)

    with open(filepath, "r") as file:
        content = file.read()

    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output(f"app4-invoicegen/challenge/output.pdf")