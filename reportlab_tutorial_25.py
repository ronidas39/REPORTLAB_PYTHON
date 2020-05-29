#tutorial 25
#bullets

#using <bullet> tag
from reportlab.platypus import SimpleDocTemplate,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
pdf=SimpleDocTemplate("tutorial25.pdf")
flow_obj=[]
styles=getSampleStyleSheet()
text='''<font name="Helvetica" color=red size=15><bullet>&bull</bullet>this is with bullet</font>'''
for i in range(4):
 p_text=Paragraph(text,style=styles["Normal"])
 flow_obj.append(p_text)
pdf.build(flow_obj)

#using bulletText argument
from reportlab.platypus import SimpleDocTemplate,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
pdf=SimpleDocTemplate("tutorial25.pdf")
flow_obj=[]
styles=getSampleStyleSheet()
text='''this is with bullet'''
for i in range(4):
 p_text=Paragraph(text,style=styles["Normal"],bulletText="**")
 flow_obj.append(p_text)
pdf.build(flow_obj)

