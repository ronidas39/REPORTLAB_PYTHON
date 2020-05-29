#tutorial 24
#sequence number for paragraph
from reportlab.platypus import Paragraph,SimpleDocTemplate,Spacer
from reportlab.lib.styles import getSampleStyleSheet
pdf=SimpleDocTemplate("tutorial24.pdf") 
flow_obj=[]
styles=getSampleStyleSheet()
for i in range(11,15):
 p_seq='<font name=Times-Italic size=20 color=red><seq id="section-id"/>.section</font>'
 p_seq_text=Paragraph(p_seq,style=styles["Normal"])
 flow_obj.append(p_seq_text)
 flow_obj.append(Spacer(1,15))
 p_con='<font name=Helvetica size=15 color=green>content %s</font>'% i
 p_con_text=Paragraph(p_con,style=styles["Normal"])
 flow_obj.append(p_con_text)
 flow_obj.append(Spacer(1,45))
pdf.build(flow_obj) 



