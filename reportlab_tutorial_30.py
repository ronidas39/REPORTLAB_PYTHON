#tutorial 30
#table

#create table with rowbackgrounds & colbackgrounds
from reportlab.platypus import Paragraph,SimpleDocTemplate,Table,TableStyle
from reportlab.lib import colors
pdf=SimpleDocTemplate("tutorial30.pdf")
flow_obj=[] 
data=[[1,2,3,4,5,6,7,8],
      [1,2,3,4,5,6,7,8],
      [1,2,3,4,5,6,7,8],
      [1,2,3,4,5,6,7,8],
      [1,2,3,4,5,6,7,8],
      [1,2,3,4,5,6,7,8],
      [1,2,3,4,5,6,7,8],
      [1,2,3,4,5,6,7,8]]  

t=Table(data,colWidths=[50 for i in range(1,9)],rowHeights=[50 for i in range(1,9)]) 
tstyle=TableStyle([("GRID",(0,0),(-1,-1),2,colors.red),
                   ("COLBACKGROUNDS",(0,0),(-1,-8),[colors.black,colors.white]),
                   ("COLBACKGROUNDS",(0,1),(-1,-7),[colors.white,colors.black]),
                   ("COLBACKGROUNDS",(0,2),(-1,-6),[colors.black,colors.white]),
                   ("COLBACKGROUNDS",(0,3),(-1,-5),[colors.white,colors.black]),
                   ("COLBACKGROUNDS",(0,4),(-1,-4),[colors.black,colors.white]),
                   ("COLBACKGROUNDS",(0,5),(-1,-3),[colors.white,colors.black]),
                   ("COLBACKGROUNDS",(0,6),(-1,-2),[colors.black,colors.white]),
                   ("COLBACKGROUNDS",(0,7),(-1,-1),[colors.white,colors.black])])
t.setStyle(tstyle)   
flow_obj.append(t) 
pdf.build(flow_obj)         
                  
                  



 
