#tutorial 50
#CREATE PORTRAIT & LANDSCAPE ORIENTATION TOGETHER IN SAME PDF
from reportlab.platypus.doctemplate import SimpleDocTemplate, PageTemplate,PageBreak
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph,SimpleDocTemplate,PageTemplate,NextPageTemplate,Frame
from reportlab.lib.styles import getSampleStyleSheet
pdf=SimpleDocTemplate("tutorial50.pdf")
frame1=Frame(10,20,600,1000,showBoundary=1)
frame2=Frame(10,20,1000,700,showBoundary=1)
port=PageTemplate(id="p",pagesize=[800,1200],frames=[frame1])
land=PageTemplate(id="l",pagesize=[1200,900],frames=[frame2])
pdf.addPageTemplates([port,land])
text="text"
flow_obj=[]
styles=getSampleStyleSheet()
ptext=Paragraph(text,style=styles["Normal"])
flow_obj.append(ptext)

flow_obj.append(NextPageTemplate("l"))
flow_obj.append(PageBreak())
flow_obj.append(ptext)
flow_obj.append(NextPageTemplate("p"))
flow_obj.append(PageBreak())
flow_obj.append(ptext)
pdf.build(flow_obj)

