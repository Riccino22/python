from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.output("ticket.pdf")