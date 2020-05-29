#tutorial 44
#CREATE EDITABLE TEXTBOX IN PDF
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import colors
pdf=canvas.Canvas("tutorial44.pdf")
pdf.drawCentredString(10,50,"test")
x=pdf.acroForm
x.textfield(fillColor=colors.yellow, borderColor=colors.black, textColor=colors.red, borderWidth=2, borderStyle="solid", width=500, height=50, x=50, y=40, tooltip="tutorial44 example", name="tutorial44 textbox",fontSize=20)
pdf.save()
