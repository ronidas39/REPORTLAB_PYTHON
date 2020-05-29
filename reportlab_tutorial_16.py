#tutorial 16
#INTRODUCTION TO PLATYPUS
from reportlab.platypus import Spacer,SimpleDocTemplate,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
pdf_file=SimpleDocTemplate("tutorial_16.pdf")
flow=[]
styles=getSampleStyleSheet()
text="sample text"
par_text=Paragraph("sample text1",styles["Normal"])
flow.append(par_text)
flow.append(Spacer(1,20))
par_text=Paragraph("sample text2",styles["Normal"])
flow.append(par_text)
flow.append(Spacer(1,40))
par_text=Paragraph("sample text3",styles["Normal"])
flow.append(par_text)
pdf_file.build(flow)




