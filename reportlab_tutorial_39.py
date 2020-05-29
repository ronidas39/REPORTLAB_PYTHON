#tutorial 39
#create multiple shapes

#reportlab graphics sub package to create multiple shapes

from reportlab.graphics.barcode import code39
from reportlab.platypus import SimpleDocTemplate,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
pdf=SimpleDocTemplate("tutorial39.pdf")
flow_obj=[]
styles=getSampleStyleSheet()
codetext="-paste-colgatemax white-100gm-5usd-"
code=code39.Standard39(codetext,barHeight=50)
flow_obj.append(code)
pdf.build(flow_obj)

