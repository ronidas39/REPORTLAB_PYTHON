#tutorial 27
#table

#CREATE TABLE WITH image & paragraph
from reportlab.platypus import Paragraph,SimpleDocTemplate,Table,TableStyle,Image
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

pdf=SimpleDocTemplate("tutorial27.pdf")
flow_obj=[]
styles=getSampleStyleSheet()
im_data1=Image("logo.jpg",50,50)
im_data2=Image("roni.jpg",50,50)
text='<font name="Times-Italic" color=red size="12">this is paragraph text</font>'
p_text=Paragraph(text,style=styles["Normal"])
t=Table([[im_data1 for i in range(1,7)],
         [im_data2 for i in range(1,7)],
         [x for x in range(1,7)],
         [p_text for i in range(1,7)]])
t_style=TableStyle([("BOX",(0,0),(-1,-1),2,colors.red),
                    ("GRID",(0,0),(-1,-1),2,colors.blue),
                    ("BACKGROUND",(0,0),(-1,-1),colors.yellow)])
t.setStyle(t_style)
flow_obj.append(t)
pdf.build(flow_obj)