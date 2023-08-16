from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("app3-pdftemp/topics.csv")
for _, row in df.iterrows():
    for _ in range(row["Pages"]):
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(10, 10, 10)
        # width -> w; boolean -> border; boolean -> ln; height -> font
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        pdf.line(10, 21, 200, 21)
        for i in range(21, 291, 10):
            pdf.line(10, i, 200, i)

        # Set the footer
        pdf.ln(260)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("app3-pdftemp/output.pdf")