from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

pdf.set_font(family="Helvetica", style="B", size=12)
pdf.cell(w=0.1, h=12, txt="The guide", align="L", ln=1, border=1)
pdf.cell(w=0.1, h=12, txt="", align="L", ln=1, border=0)
pdf.set_font(family="Helvetica", style="B", size=18)
pdf.cell(w=0, h=12, txt="This is a PDF file.", align="C", ln=2, border=0)
pdf.output("first_file.pdf")


print(pdf)