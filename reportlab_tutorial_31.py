#tutorial 31
#table

#create table from csv file

from reportlab.platypus import SimpleDocTemplate,Table,TableStyle
from reportlab.lib import colors
import csv
pdf=SimpleDocTemplate("tutorial31.pdf")
flow_obj=[]
with open("testdata.csv")as f1:
    csvdata=csv.reader(f1,delimiter=",")
    tdata=[]
    for row in csvdata:
        data=[]
        #print(row)
        name=row[0]
        company=row[1]
        dep=row[2]
        country=row[3]
        email=row[4]
        data.append(name)
        data.append(company)
        data.append(dep)
        data.append(country)
        data.append(email)
        tdata.append(data)
        
#print(tdata)
t=Table(tdata)
tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.red),
                   ("BACKGROUND",(0,0),(-1,-30),colors.blue),
                   ("BACKGROUND",(0,1),(-1,-1),colors.yellow),
                   ("FONT",(0,0),(-1,-1),"Times-Italic",7)])

t.setStyle(tstyle)
flow_obj.append(t) 
pdf.build(flow_obj)   
        
                  



 
