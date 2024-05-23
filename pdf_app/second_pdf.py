from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()

pdf.set_font(family="Helvetica", style="B", size=0)
pdf.cell(w=20, h=12, txt="1", border=1, ln=0, align="C")
pdf.cell(w=0, h=12, txt="2", border=1, ln=1, align="C")

pdf.cell(w=0, h=12, txt="3", border=1, ln=1, align="C")

pdf.cell(w=20, h=24, txt="4", border=1, ln=0, align="C")
pdf.cell(w=0, h=12, txt="5", border=1, ln=1, align="C")
pdf.cell(w=20, h=12, txt="6", border=1, ln=1, align="C")


pdf.output("second_file.pdf")