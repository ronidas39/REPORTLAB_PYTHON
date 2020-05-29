#tutorial 15
#textobject setrise
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
pdf=canvas.Canvas("tutorial15.pdf",bottomup=0)
pdf.translate(cm, cm)
textobject=pdf.beginText()
textobject.setTextOrigin(10, 10)
text="demo"
textobject.textOut(text)
textobject.setRise(5)
textobject.textOut("superscript")
textobject.setRise(0)
textobject.textOut("and")
textobject.setRise(-5)
textobject.textOut("subscript")
pdf.drawText(textobject)
pdf.save()


