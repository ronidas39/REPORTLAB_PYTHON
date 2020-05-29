#tutorial 45
#CREATE EDITABLE CHEKBOX IN PDF
from reportlab.pdfgen import canvas
from reportlab.lib import colors
pdf=canvas.Canvas("TUTORIAL45.pdf")
pdf.drawCentredString(30,50,"checkbox1")
x=pdf.acroForm
x.checkbox(buttonStyle="check", shape="square", fillColor=colors.yellow, borderColor=colors.black, textColor=colors.red, borderWidth=1, borderStyle="solid", size=30, x=150, y=30, tooltip="checkbox1", name="checkbox1")
pdf.drawCentredString(30,200,"checkbox2")
x.checkbox(checked=True,buttonStyle="cross", shape="square", fillColor=colors.yellow, borderColor=colors.black, textColor=colors.red, borderWidth=1, borderStyle="solid", size=30, x=150, y=180, tooltip="checkbox2", name="checkbox2")
pdf.save()
