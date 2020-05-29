#tutorial 26
#table

#using table class
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
pdf=SimpleDocTemplate("tutorial26.pdf")
flow_obj=[]
styles=getSampleStyleSheet()
data=[[str(x) for x in range (1,7)],[str(x) for x in range (1,7)],[str(x) for x in range (1,7)]]
#print(help(Table))
#tstyle=TableStyle([("GRID",(0,0),(-5,-2),.1,colors.red),
                   #("GRID",(4,1),(-1,-1),.1,colors.green)])

tstyle=TableStyle([("BOX",(0,0),(-1,-1),2,colors.red),
                   ("FONT",(0,0),(-1,-1),"Times-Italic",50),
                   ("TEXTCOLOR",(0,0),(-1,-1),colors.red),
                   ("BACKGROUND",(0,0),(-1,-1),colors.blue),
                   ("BACKGROUND",(4,1),(-1,-1),colors.green)])
t=Table(data)
t.setStyle(tstyle)
flow_obj.append(t)
pdf.build(flow_obj)




