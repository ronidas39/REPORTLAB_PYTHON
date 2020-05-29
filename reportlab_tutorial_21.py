from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph,SimpleDocTemplate
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet    
pdf=SimpleDocTemplate("tutorial21.pdf") 
flow_object=[]   
styles=getSampleStyleSheet()
text='''
       <font name="Times-Italic" size=20 color="red">sample text without custom font </font>
              '''
p_text=Paragraph(text,style=styles["Normal"])  
flow_object.append(p_text)  
pdf.build(flow_object)   

