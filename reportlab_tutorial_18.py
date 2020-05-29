#tutorial 18
#Intra paragrpah mark-up

#without any mark up
from reportlab.platypus import Paragraph,SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

pdf=SimpleDocTemplate("tutorial18.pdf")
flow_obj=[]
styles=getSampleStyleSheet()
text='''
    This is <b>formatted paragraph</b> , <br></br>with any break and bold markups.
     '''

para_text=Paragraph(text,style=styles["Normal"])
flow_obj.append(para_text)
pdf.build(flow_obj)



