#tutorial 14
#textobject word spacing
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

pdf=canvas.Canvas("tutorial14.pdf",bottomup=0)
pdf.translate(cm, cm)

textobject=pdf.beginText()
textobject.setTextOrigin(10, 10)
text="please subscribe to our channel total technology"

for i in range(15):
    textobject.textLine(text)
    textobject.setWordSpace(i+1)
    
pdf.drawText(textobject)
pdf.save()
