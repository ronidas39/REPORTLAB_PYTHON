from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import colors

pdf=canvas.Canvas("tutorial58.pdf")
pdf.translate(cm,cm)
pdf.setPageSize((1024,700))
#template 1
pdf.setStrokeColor(colors.green)
pdf.setFillColor(colors.green)
pdf.rect(40,560,900,100,stroke=1,fill=1)
pdf.setStrokeColor(colors.red)
pdf.setFillColor(colors.red)
pdf.rect(40,30,900,500,stroke=1,fill=1)

pdf.setStrokeColor(colors.red)
pdf.setFillColor(colors.red)
pdf.rect(40,30,900,500,stroke=1,fill=1)

pdf.save()

#template 2
# pdf.setStrokeColor(colors.green)
# pdf.setFillColor(colors.green)
# pdf.rect(40,560,900,100,stroke=1,fill=1)

# pdf.setStrokeColor(colors.blueviolet)
# pdf.setFillColor(colors.blueviolet)
# pdf.rect(40,100,900,420,stroke=1,fill=1)

# pdf.setStrokeColor(colors.red)
# pdf.setFillColor(colors.red)
# pdf.rect(40,20,900,50,stroke=1,fill=1)
# pdf.save()
#tutorial 3
# pdf.setStrokeColor(colors.green)
# pdf.setFillColor(colors.green)
# pdf.rect(40,560,900,100,stroke=1,fill=1)

# pdf.setStrokeColor(colors.blueviolet)
# pdf.setFillColor(colors.blueviolet)
# pdf.rect(40,100,200,420,stroke=1,fill=1)

# pdf.setStrokeColor(colors.blueviolet)
# pdf.setFillColor(colors.blueviolet)
# pdf.rect(260,100,680,420,stroke=1,fill=1)

# pdf.setStrokeColor(colors.red)
# pdf.setFillColor(colors.red)
# pdf.rect(40,20,900,50,stroke=1,fill=1)
# pdf.save()

#tutorial 4
# pdf.setStrokeColor(colors.green)
# pdf.setFillColor(colors.green)
# pdf.rect(40,560,900,100,stroke=1,fill=1)

# pdf.setStrokeColor(colors.blueviolet)
# pdf.setFillColor(colors.blueviolet)
# pdf.rect(40,100,200,420,stroke=1,fill=1)

# pdf.setStrokeColor(colors.blueviolet)
# pdf.setFillColor(colors.blueviolet)
# pdf.rect(260,100,680,220,stroke=1,fill=1)

# pdf.setStrokeColor(colors.blueviolet)
# pdf.setFillColor(colors.blueviolet)
# pdf.rect(260,330,680,190,stroke=1,fill=1)


# pdf.setStrokeColor(colors.red)
# pdf.setFillColor(colors.red)
# pdf.rect(40,20,900,50,stroke=1,fill=1)
# pdf.save()



