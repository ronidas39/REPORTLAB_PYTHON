#tutorial 55
#how to generate multiple table in same pdf page
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph,Table,TableStyle,Frame
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

pdf=canvas.Canvas("tutorial55.pdf")
flow_obj=[]
styles=getSampleStyleSheet()
t1=Paragraph("table1",style=styles["Normal"])
flow_obj.append(t1)
t=Table([[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]])
ts=TableStyle([("GRID",(0,0),(-1,-1),2,colors.red),
               ("BACKGROUND",(0,0),(-1,-1),colors.yellow)])
t.setStyle(ts)
flow_obj.append(t)
frame=Frame(20,150,100,200,showBoundary=1)
frame.addFromList(flow_obj, pdf)

t1=Paragraph("table2",style=styles["Normal"])
flow_obj.append(t1)
flow_obj.append(t)
frame=Frame(130,150,100,200,showBoundary=1)
frame.addFromList(flow_obj, pdf)

t1=Paragraph("table3",style=styles["Normal"])
flow_obj.append(t1)
flow_obj.append(t)
frame=Frame(240,150,100,200,showBoundary=1)
frame.addFromList(flow_obj, pdf)

pdf.save()