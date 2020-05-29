#tutorial 33
#table

#create table inside frame from csv file

from reportlab.platypus import SimpleDocTemplate,Table,TableStyle,PageBreak,Frame
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
import csv

pdf=canvas.Canvas("tutorial33.pdf")
#pdf=SimpleDocTemplate("tutorial33.pdf")
flow_obj=[]
with open("testdata.csv")as f1:
    datacsv=csv.reader(f1,delimiter="|")
    data=[]
    for row in datacsv:
        
        name=row[0]
        cmp=row[1]
        dep=row[2]
        country=row[3]
        email=row[4]
        data.append(row)
        
        
i=1        
for i in range(len(data)-1):
    pdf.setLineWidth(5)
    pdf.setStrokeColor(colors.green)
    pdf.setFillColor(colors.darkkhaki)
    pdf.rect(50,500,500,300,fill=1)
    pdf.setFillColor(colors.lightskyblue)
    pdf.rect(50,650,500,50,fill=1)
    pdf.setFillColor(colors.darkgoldenrod)
    pdf.drawCentredString(250, 670, f"ROW {i+1}")
    pdf.circle(300,520,20)
    pdf.setFillColor(colors.red)
    pdf.drawCentredString(300,510,str(pdf.getPageNumber()))
    
    theader=Table([data[0]],colWidths=[60,80,70,100,130])
    tstyle1=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
                       ("FONT",(0,0),(-1,-1),"Times-Italic",6),
                       ("BACKGROUND",(0,0),(-1,-1),colors.yellow)])
    tstyle2=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
                       ("FONT",(0,0),(-1,-1),"Times-Italic",6),
                       ("BACKGROUND",(0,0),(-1,-1),colors.blueviolet)])
                      
    theader.setStyle(tstyle1)
    flow_obj.append(theader)
    trow=Table([data[i+1]],colWidths=[60,80,70,100,130])
    trow.setStyle(tstyle2)
    flow_obj.append(trow)
    frame=Frame(50,500,500,300,showBoundary=1)
    frame.addFromList(flow_obj, pdf)
    pdf.showPage()
pdf.save()
    