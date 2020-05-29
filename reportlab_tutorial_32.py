#tutorial 32
#table

#create multi page table from csv file
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle,PageBreak
from reportlab.lib import colors
import csv
from bleach._vendor.html5lib._ihatexml import name
pdf=SimpleDocTemplate("tutorial32.pdf")
flow_obj=[]
with open("testdata.csv") as f1:
    csvdata=csv.reader(f1,delimiter="|")
    tdata=[]
    for data in csvdata:
        rowdata=[]
        name=data[0]
        company=data[1]
        dep=data[2]
        country=data[3]
        email=data[4]
        rowdata.append(name)
        rowdata.append(company)
        rowdata.append(dep)
        rowdata.append(country)
        rowdata.append(email)
        tdata.append(rowdata)        
for i in range(len(tdata)):
    if(i%10==0 and i>0): 
        flow_obj.append(PageBreak())       
        t=Table([tdata[0]],colWidths=[50,100,100,80,120]) 
        tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
                       ("FONT",(0,0),(-1,-1),"Times-Italic",5),
                       ("BACKGROUND",(0,0),(-1,-1),colors.yellow)]) 
    
        t.setStyle(tstyle)  
        flow_obj.append(t)              
    if (i==0):
        t=Table([tdata[0]],colWidths=[50,100,100,80,120]) 
        tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
                       ("FONT",(0,0),(-1,-1),"Times-Italic",5),
                        ("BACKGROUND",(0,0),(-1,-1),colors.yellow)])
                        
    
        t.setStyle(tstyle)  
        flow_obj.append(t)
        
    else: 
        t=Table([tdata[i]],colWidths=[50,100,100,80,120]) 
        tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
                       ("FONT",(0,0),(-1,-1),"Times-Italic",5)])
                        
    
        t.setStyle(tstyle)  
        flow_obj.append(t)     
pdf.build(flow_obj)   


