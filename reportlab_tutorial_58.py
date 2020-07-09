#tutorial 57
import pyodbc
import io
import datetime
from reportlab.pdfgen import canvas
from reportlab.platypus import Table,TableStyle,Frame,Paragraph,Spacer
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
#read credentinal file

pdf=canvas.Canvas("tutorial58.pdf")
pdf.setPageSize((1024,700))
flow_obj=[]
pdf.translate(cm, cm)
#template 1
#===============================================================================
# pdf.setFillColor(colors.blue)
# pdf.setStrokeColor(colors.darkgreen)
# pdf.setFillColor(colors.darkgreen)
# pdf.rect(40, 560, 900, 100, stroke=1, fill=1)
# pdf.setStrokeColor(colors.red)
# pdf.setFillColor(colors.red)
# pdf.rect(40, 30, 900, 500, stroke=1, fill=1)
#===============================================================================

#template2
#===============================================================================
# pdf.setFillColor(colors.blue)
# pdf.setStrokeColor(colors.darkgreen)
# pdf.setFillColor(colors.darkgreen)
# pdf.rect(40, 560, 900, 100, stroke=1, fill=1)
# pdf.setStrokeColor(colors.blueviolet)
# pdf.setFillColor(colors.blueviolet)
# pdf.rect(40, 100, 900, 420, stroke=1, fill=1)
# 
# pdf.setStrokeColor(colors.orangered)
# pdf.setFillColor(colors.orangered)
# pdf.rect(40, 20, 900, 60, stroke=1, fill=1)
#===============================================================================

#template 3
#===============================================================================
# pdf.setFillColor(colors.blue)
# pdf.setStrokeColor(colors.darkgreen)
# pdf.setFillColor(colors.darkgreen)
# pdf.rect(40, 560, 900, 100, stroke=1, fill=1)
# pdf.setStrokeColor(colors.blueviolet)
# pdf.setFillColor(colors.blueviolet)
# pdf.rect(40, 100, 200, 420, stroke=1, fill=1)
# pdf.setStrokeColor(colors.blueviolet)
# pdf.setFillColor(colors.blueviolet)
# pdf.rect(260, 100, 680, 420, stroke=1, fill=1)
# 
# pdf.setStrokeColor(colors.orangered)
# pdf.setFillColor(colors.orangered)
# pdf.rect(40, 20, 900, 60, stroke=1, fill=1)
#===============================================================================


#template 4
pdf.setFillColor(colors.blue)
pdf.setStrokeColor(colors.darkgreen)
pdf.setFillColor(colors.darkgreen)
pdf.rect(40, 560, 900, 100, stroke=1, fill=1)
pdf.setStrokeColor(colors.blueviolet)
pdf.setFillColor(colors.blueviolet)
pdf.rect(40, 100, 200, 420, stroke=1, fill=1)
pdf.setStrokeColor(colors.blueviolet)
pdf.setFillColor(colors.blueviolet)
pdf.rect(260, 100, 680, 220, stroke=1, fill=1)
pdf.rect(260, 330, 680, 190, stroke=1, fill=1)

pdf.setStrokeColor(colors.orangered)
pdf.setFillColor(colors.orangered)
pdf.rect(40, 20, 900, 60, stroke=1, fill=1)
        
        
    
pdf.save()


  










