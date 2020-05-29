from reportlab.pdfgen import canvas
from reportlab.platypus import Frame,Table,TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
pdf=canvas.Canvas("tutorial52.pdf",pagesize=(1024,900))
pdf.translate(cm, cm)
for i in range(1,10):
 pdf.translate(cm, cm)
 ts=TableStyle([("FONT",(0,0),(-1,-1),"Helvetica-Bold",13),
 ("TEXTCOLOR",(0,0),(-1,-1),"BLUE")])
 frameh=Frame(10,800,900,40,showBoundary=1)
 flow_obj1=[]
 tableh=Table([["BY TOTAL TECHNOLOGY"]])
 tableh.setStyle(ts)
 flow_obj1.append(tableh)
 tablef=Table([["ALL RIGHTS RESERVED ,page no: "+str(pdf.getPageNumber())]])
 tablef.setStyle(ts)
 flow_obj1.append(tableh)
 frameh.addFromList(flow_obj1, pdf)
 pdf.setFontSize(20)
 pdf.drawString(30,700,"lorem ipsum samle text for header & footer")
 framef=Frame(10,50,900,40,showBoundary=1)
 flow_obj2=[]
 flow_obj2.append(tablef)
 framef.addFromList(flow_obj2, pdf)
 pdf.showPage()
pdf.save()
