#tutorial 29
#table

#create table with alignment
from reportlab.platypus import Paragraph,SimpleDocTemplate,Table,TableStyle
from reportlab.lib import colors
pdf=SimpleDocTemplate("tutorial29.pdf")
flow_obj=[]
data=[[1,2,3,4,5],
      [1,2,3,4,5],
      [1,2,3,4,5]]

t=Table(data,colWidths=[40 for i in range(1,6)],rowHeights=[40 for i in range(1,4)])
tstyle=TableStyle([("BOX",(0,0),(-1,-1),1,colors.red),
                  ("GRID",(0,0),(-1,-1),1,colors.blue),
                  ("VALIGN",(0,0),(-1,-1),"MIDDLE")])
t.setStyle(tstyle)
flow_obj.append(t)
pdf.build(flow_obj)
                  
                  
                  
                  



 
