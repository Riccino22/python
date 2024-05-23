from fpdf import FPDF
import random

def generate_ticket(name, email, quantity):
    for index in range(int(quantity)):
        ticket_id = str(random.randint(1000000, 9999999))
        pdf = FPDF(orientation="P", unit="mm", format="A4")

        pdf.add_page()
        pdf.set_font(family="Helvetica", style="B", size=12)
        pdf.cell(w=0.1, h=10, txt="Ticket for the event", border=1, ln=1, align="L")

        pdf.set_font(family="Helvetica", style="B", size=20)

        def info_item(title, height=12):
            pdf.cell(w=60, h=height, border=0, ln=0, align="C")
            pdf.cell(w=0, h=height, txt=title, border=0, ln=1, align="L")


        info_item(height=20, title="Information")

        pdf.set_font(family="Helvetica", style="B", size=15)


        data = [
            "ID: " + ticket_id, 
            "Name: " + name, 
            "Email: " + email
        ]

        for item in data: info_item(title=item)

        pdf.output(ticket_id + ".pdf")