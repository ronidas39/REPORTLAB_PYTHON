#tutorial 46
#CREATE EDITABLE COMBOBOX IN PDF
from reportlab.pdfgen import canvas
from reportlab.lib import colors
pdf=canvas.Canvas("tutorial46.pdf")
pdf.drawCentredString(20,50,"select from combobox")
x=pdf.acroForm
x.choice(value="blue", fillColor=colors.yellow, borderColor=colors.black, textColor=colors.red, borderWidth=2, borderStyle="solid", width=50, height=100, x=50, y=40, tooltip="combix1", name="combox1", options=["red","blue","black","green","yellow"])
pdf.save()