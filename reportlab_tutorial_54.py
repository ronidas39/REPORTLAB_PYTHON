#tutorial 54
#how to generate nested frames in pdf
from reportlab.pdfgen import canvas
from reportlab.platypus import Frame,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
pdf=canvas.Canvas("tutorial54.pdf")
flow_obj=[]
styles=getSampleStyleSheet()
text1=Paragraph("inner-frame",style=styles["Normal"])
flow_obj.append(text1)
frame=Frame(50,250,300,200,showBoundary=1)
frame.addFromList(flow_obj, pdf)

text3=Paragraph("inner_most-frame",style=styles["Normal"])
flow_obj.append(text3)
frame=Frame(150,290,80,80,showBoundary=1)
frame.addFromList(flow_obj, pdf)

text2=Paragraph("outer-frame",style=styles["Normal"])
flow_obj.append(text2)
frame=Frame(10,150,400,400,showBoundary=1)
frame.addFromList(flow_obj, pdf)
pdf.save()
