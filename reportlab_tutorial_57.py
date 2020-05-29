#tutorial 57
import pyodbc
import io
import datetime
from reportlab.pdfgen import canvas
from reportlab.platypus import Table,TableStyle,Frame,Paragraph,Spacer
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
#read credentinal file
with io.open("cred.txt","r",encoding="utf-8")as f1:
    cred_data=f1.read()
    f1.close()
cred_data=cred_data.split(",")
server=cred_data[0]
database=cred_data[1]
username=cred_data[2]
pwd=cred_data[3]
#setup pdf file relaed objects
pdf=canvas.Canvas("tutorial57.pdf")
flow_obj=[]
pdf.translate(cm, cm)
#establish the db connection & get whole data set
con_obj=pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER="+server+";DATABASE="+database+";UID="+username+";PWD="+pwd)
data_obj=con_obj.cursor()
data_obj.execute("select * from dbo.EMP")
data_row=data_obj.fetchall()

#pagination
count=len(data_row)
num=int(count/45)
a=int(count/num)
print(a)
count_new=[0]
x=0
while(x+a<count):
    x=x+a
    count_new.append(x)
frame1=Frame(10,40,360,280,showBoundary=1)
styles=getSampleStyleSheet()
text="""
This is the database report for pagination <b></b>,<br></br>"""
t1=Paragraph(text,style=styles["Normal"])
flow_obj.append(t1)
flow_obj.append(Spacer(6,6))
text="""
data generated at: """ + str(datetime.datetime.now())
t2=Paragraph(text,style=styles["Normal"])
flow_obj.append(t2)
frame1.addFromList(flow_obj, pdf)
pdf.showPage()

#looping for pagination
for j in range(len(count_new)):
    frame=Frame(10,40,560,780,showBoundary=1)
    data1=[["EMPID","FNAME","SNAME","COMPANY","DEPARTMENT","JOB","EMAIL"]]
    if(j==len(count_new)-1):
        for row in data_row[count_new[j]:]:
            data1.append([row.EMPID,row.FNAME,row.SNAME,row.COMPANY,row.DEPARTMENT,row.JOB,row.EMAIL])
        table=Table(data1,colWidths=[40,40,40,50,100,50,160],rowHeights=[15 for i in range(len(data1))]) 
        ts=TableStyle([("GRID",(0,0),(-1,-1),2,colors.red),
                       ("BACKGROUND",(0,0),(-1,0),colors.yellow),
                       ("BACKGROUND",(0,1),(-1,-1),colors.lightblue),
                       ("SIZE",(0,0),(-1,-1),6,colors.yellow),
                       ("ALIGN",(0,0),(-1,-1),"LEFT")])
        table.setStyle(ts)
        flow_obj.append(Spacer(8,8))
        flow_obj.append(table)
        frame.addFromList(flow_obj, pdf)
        pdf.showPage()    
    else:
                
        for row in data_row[count_new[j]:count_new[j+1]]:
         data1.append([row.EMPID,row.FNAME,row.SNAME,row.COMPANY,row.DEPARTMENT,row.JOB,row.EMAIL])
        table=Table(data1,colWidths=[40,40,40,50,100,50,160],rowHeights=[15 for i in range(len(data1))]) 
        ts=TableStyle([("GRID",(0,0),(-1,-1),2,colors.red),
                       ("BACKGROUND",(0,0),(-1,0),colors.yellow),
                       ("BACKGROUND",(0,1),(-1,-1),colors.lightblue),
                       ("SIZE",(0,0),(-1,-1),6,colors.yellow),
                       ("ALIGN",(0,0),(-1,-1),"LEFT")])
        table.setStyle(ts)
        print(data1)
        flow_obj.append(Spacer(8,8))
        flow_obj.append(table)
        
        frame.addFromList(flow_obj, pdf)
        pdf.showPage()
        
        
        
    
pdf.save()


  










