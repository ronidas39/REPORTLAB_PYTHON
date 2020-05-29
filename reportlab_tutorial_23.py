#tutorial 23
#frames 
from reportlab.platypus  import  Paragraph,Frame ,SimpleDocTemplate
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
pdf=canvas.Canvas("tutorial23.pdf")
pdf.drawImage("logo.jpg", 20,50, 80, 50)
pdf.setStrokeColor("RED")
flow_obj=[]
styles=getSampleStyleSheet()
text='''
     this is frame
     '''
p_text=Paragraph(text,style=styles["Normal"]) 
flow_obj.append(p_text)   
frame=Frame(20,50,80,50,showBoundary=1)
frame.addFromList(flow_obj,pdf)
pdf.drawImage("logo.jpg", 110,50, 80, 50)
flow_obj1=[]
flow_obj1.append(p_text)
frame=Frame(110,50,80,50,showBoundary=1)
frame.addFromList(flow_obj1,pdf)
pdf.save()
