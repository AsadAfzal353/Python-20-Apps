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
    pdf.cell(w=50, h=24, txt=filename.title())

pdf.output(f"app4-invoicegen/challenge/output.pdf")