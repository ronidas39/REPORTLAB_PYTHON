#tutorial 49
#CREATE PORTRAIT ORIENTATIONS IN PDF
 from reportlab.pdfgen import canvas
 from reportlab.lib.pagesizes import letter,landscape
 from reportlab.lib.units import cm
 pdf=canvas.Canvas("tutorial49.pdf")
 pdf.setPageSize([100,900])
 pdf.translate(cm, cm)
 pdf.drawCentredString(30,50,"portrait orientation")
 pdf.save()
#CREATE LANDSCAPE ORIENTATION IN PDF
 from reportlab.pdfgen import canvas
 from reportlab.lib.pagesizes import letter,landscape
 from reportlab.lib.units import cm
 pdf=canvas.Canvas("tutorial49.pdf",pagesize=letter)
 pdf.translate(cm, cm)
 pdf.setPageSize(landscape(letter))
 pdf.drawCentredString(30,50,"landscape")
 pdf.save()

#HOW TO  CREATE LANDSCAPE ORIENTATION WITH CUSTOM SIZE
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,landscape
from reportlab.lib.units import cm
pdf=canvas.Canvas("tutorial49.pdf")
pdf.translate(cm, cm)
pdf.setPageSize([950,550])
pdf.drawCentredString(30,50,"landscape")
pdf.save()



