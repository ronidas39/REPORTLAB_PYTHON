#TUTORIAL 53
#MULTIPLE FRAME WITHIN SAME PAGE

#create two frames side by side  with same height & width 

from reportlab.pdfgen import canvas
from reportlab.platypus import Frame
pdf=canvas.Canvas("tutorial53.pdf")
flow_obj=[]
frame=Frame(50,150,200,300,showBoundary=1)
frame.addFromList(flow_obj, pdf)
frame=Frame(270,150,200,300,showBoundary=1)
frame.addFromList(flow_obj, pdf)
pdf.save()
