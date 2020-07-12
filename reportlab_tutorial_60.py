from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib import colors

pdf=canvas.Canvas("tutorial60.pdf")
pdf.translate(cm,cm)
pdf.setPageSize((1024,700))

pdf.setStrokeColor(colors.green)
pdf.setFillColor(colors.green)
pdf.rect(40,560,900,100,stroke=1,fill=1)

pdf.setStrokeColor(colors.blueviolet)
pdf.setFillColor(colors.blueviolet)
pdf.rect(40,100,200,420,stroke=1,fill=1)
pdf.setStrokeColor(colors.white)
pdf.setLineWidth(3)
pdf.line(62,105,220,105)
pdf.line(62,135,220,135)
pdf.line(62,165,220,165)
pdf.line(62,195,220,195)
pdf.line(62,225,220,225)
pdf.line(62,255,220,255)
pdf.line(62,285,220,285)
pdf.line(62,315,220,315)
pdf.line(62,345,220,345)
pdf.line(62,375,220,375)
pdf.line(62,405,220,405)
pdf.line(62,435,220,435)
pdf.line(62,465,220,465)


pdf.setStrokeColor(colors.blueviolet)
pdf.setFillColor(colors.blueviolet)
pdf.rect(260,100,680,420,stroke=1,fill=1)

pdf.setStrokeColor(colors.white)
pdf.setLineWidth(3)
pdf.line(282,105,900,105)
pdf.line(282,135,900,135)
pdf.line(282,165,900,165)
pdf.line(282,195,900,195)
pdf.line(282,225,900,225)
pdf.line(282,255,900,255)
pdf.line(282,285,900,285)
pdf.line(282,315,900,315)
pdf.line(282,345,900,345)
pdf.line(282,375,900,375)
pdf.line(282,405,900,405)
pdf.line(282,435,900,435)
pdf.line(282,465,900,465)

pdf.setStrokeColor(colors.red)
pdf.setFillColor(colors.red)
pdf.rect(40,20,900,50,stroke=1,fill=1)
pdf.save()


