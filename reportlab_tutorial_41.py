#TUTORIAL 41
#how to generate qr code
 from reportlab.graphics.barcode import qr
 from reportlab.pdfgen import canvas
 from reportlab.graphics import shapes,renderPDF,renderPM
 pdf=canvas.Canvas("tutorial41.pdf")
 text="www.totaltechnologyabcd.com"
 qrcode=qr.QrCodeWidget(text)
 drawing_obj=shapes.Drawing()
 drawing_obj.add(qrcode)
 renderPDF.draw(drawing_obj,pdf,200,200)
 pdf.save()
 
#how to generate qr code in png
from reportlab.graphics.barcode import qr
from reportlab.graphics import shapes,renderPM
drawing_obj=shapes.Drawing(500,500)
code="www.totaltechnoogy.com"
qrcode=qr.QrCodeWidget(code)
qrcode.barWidth=200
drawing_obj.add(qrcode)
renderPM.drawToFile(drawing_obj, fn="roni.png" )

#generate qrcode using qrcode package

import qrcode
from reportlab.platypus import SimpleDocTemplate,Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
pdf=canvas.Canvas("tutorial41_1.pdf")
pdf.translate(cm,cm)
flow_obj=[]
code="www.totaltechnoogy123456.com"
qrcode=qrcode.make(code)
qrcode.save("roni1.png")
pdf.drawImage("roni.png",10,50,800,800)
pdf.save()















