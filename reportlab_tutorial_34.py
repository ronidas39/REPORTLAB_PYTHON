#tutorial 34
#page number

#how to add page number for platypus flowable
from reportlab.platypus import Paragraph,SimpleDocTemplate,PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.pdfgen import canvas
pdf=canvas.Canvas("tutorial34.pdf")
pdf.drawCentredString(300,10,str(pdf.getPageNumber()))
pdf.showPage()
pdf.drawCentredString(300,10,str(pdf.getPageNumber()))
pdf.showPage()
pdf.drawCentredString(300,10,str(pdf.getPageNumber()))
pdf.showPage()
pdf.save()


