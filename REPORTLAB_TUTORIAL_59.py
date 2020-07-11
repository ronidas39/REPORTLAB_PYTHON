from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import colors

pdf=canvas.Canvas("tutorial59.pdf")
pdf.translate(cm,cm)
pdf.setPageSize((1024,700))
pdf.setStrokeColor(colors.green)
pdf.setFillColor(colors.green)
pdf.rect(40,560,900,100,stroke=1,fill=1)
pdf.setStrokeColor(colors.red)
pdf.setFillColor(colors.red)
pdf.rect(40,30,900,500,stroke=1,fill=1)


pdf.setFillColor(colors.white)
pdf.rect(60,50,300,20,stroke=1,fill=1)
pdf.rect(370,50,300,20,stroke=1,fill=1)
pdf.rect(680,50,240,20,stroke=1,fill=1)

pdf.rect(60,80,300,20,stroke=1,fill=1)
pdf.rect(370,80,300,20,stroke=1,fill=1)
pdf.rect(680,80,240,20,stroke=1,fill=1)

pdf.rect(60,110,300,20,stroke=1,fill=1)
pdf.rect(370,110,300,20,stroke=1,fill=1)
pdf.rect(680,110,240,20,stroke=1,fill=1)

pdf.rect(60,140,300,20,stroke=1,fill=1)
pdf.rect(370,140,300,20,stroke=1,fill=1)
pdf.rect(680,140,240,20,stroke=1,fill=1)

pdf.rect(60,170,300,20,stroke=1,fill=1)
pdf.rect(370,170,300,20,stroke=1,fill=1)
pdf.rect(680,170,240,20,stroke=1,fill=1)

pdf.rect(60,200,300,20,stroke=1,fill=1)
pdf.rect(370,200,300,20,stroke=1,fill=1)
pdf.rect(680,200,240,20,stroke=1,fill=1)

pdf.rect(60,230,300,20,stroke=1,fill=1)
pdf.rect(370,230,300,20,stroke=1,fill=1)
pdf.rect(680,230,240,20,stroke=1,fill=1)

pdf.rect(60,260,300,20,stroke=1,fill=1)
pdf.rect(370,260,300,20,stroke=1,fill=1)
pdf.rect(680,260,240,20,stroke=1,fill=1)

pdf.rect(60,290,300,20,stroke=1,fill=1)
pdf.rect(370,290,300,20,stroke=1,fill=1)
pdf.rect(680,290,240,20,stroke=1,fill=1)

pdf.rect(60,320,300,20,stroke=1,fill=1)
pdf.rect(370,320,300,20,stroke=1,fill=1)
pdf.rect(680,320,240,20,stroke=1,fill=1)

pdf.rect(60,320,300,20,stroke=1,fill=1)
pdf.rect(370,320,300,20,stroke=1,fill=1)
pdf.rect(680,320,240,20,stroke=1,fill=1)

pdf.rect(60,350,300,20,stroke=1,fill=1)
pdf.rect(370,350,300,20,stroke=1,fill=1)
pdf.rect(680,350,240,20,stroke=1,fill=1)

pdf.rect(60,380,300,20,stroke=1,fill=1)
pdf.rect(370,380,300,20,stroke=1,fill=1)
pdf.rect(680,380,240,20,stroke=1,fill=1)

pdf.rect(60,410,300,20,stroke=1,fill=1)
pdf.rect(370,410,300,20,stroke=1,fill=1)
pdf.rect(680,410,240,20,stroke=1,fill=1)

pdf.rect(60,440,300,20,stroke=1,fill=1)
pdf.rect(370,440,300,20,stroke=1,fill=1)
pdf.rect(680,440,240,20,stroke=1,fill=1)

pdf.rect(60,470,300,20,stroke=1,fill=1)
pdf.rect(370,470,300,20,stroke=1,fill=1)
pdf.rect(680,470,240,20,stroke=1,fill=1)





pdf.save()


pdf1=canvas.Canvas("tutorial59_loop.pdf")
pdf1.translate(cm,cm)
pdf1.setPageSize((1024,700))
pdf1.setStrokeColor(colors.green)
pdf1.setFillColor(colors.green)
pdf1.rect(40,560,900,100,stroke=1,fill=1)
pdf1.setStrokeColor(colors.red)
pdf1.setFillColor(colors.red)
pdf1.rect(40,30,900,500,stroke=1,fill=1)

k=440/30
k=int(k)+1
l=470
pdf1.setFillColor(colors.yellow)
for i in range(k):
      w=60
      pdf1.rect(w,l,300,20,stroke=1,fill=1)
      pdf1.rect(w+310,l,300,20,stroke=1,fill=1)
      pdf1.rect(w+620,l,240,20,stroke=1,fill=1)

      l=l-30


pdf1.save()