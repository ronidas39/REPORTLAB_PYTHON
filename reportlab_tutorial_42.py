#tutorial 42
#create annotations for pdf file

from reportlab.pdfgen import canvas
pdf=canvas.Canvas("tutorial42.pdf")
pdf.drawString(10,50,"tutorial 42")
pdf.setAuthor("RONI DAS")
pdf.setTitle("REPORTLAB ANNOTATIONS TUTORIAL")
pdf.setSubject("REPORTLAB TUTORIAL")
pdf.setCreator("total technology youtube tutorial")
pdf.save()