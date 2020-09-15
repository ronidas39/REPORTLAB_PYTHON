#tutorial 61
#generate payslip from csv file reportlab
import io
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate,Table,TableStyle,Frame,Spacer,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib import colors
from nltk.metrics.association import TOTAL
from num2words import num2words
company="Total Technology"
address="4a/cc London 5RWQWE UNITED KINGDOM"
month="Salary Slip For Month Of June 2020"

with io.open("salary_slip_csv.csv","r",encoding="utf-8")as f1:
    csv_data=f1.read()
    f1.close()
file_data=csv_data.split("\n")[1:]
flow_obj=[]
styles=getSampleStyleSheet()
#top 3 row
data=[[company],[address],[month]]



#remaining rows from csv
for rows in file_data:
    tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
                   ("ALIGN",(0,0),(-1,-1),"CENTER")])
    t=Table(data,colWidths=[500],rowHeights=[20,20,20])
    t.setStyle(tstyle)
    flow_obj.append(t)
   
   
    row=rows.split(",")
    pdf=canvas.Canvas(row[0]+"_payslip.pdf")
    pdf.translate(cm, cm)
    total=int(row[6])+int(row[7])+int(row[15])+int(row[17])+int(row[18])+int(row[19])+int(row[20])
    deductions=int(row[12])+int(row[13])+int(row[14])+int(row[16])
    row1=["EMPLOYEE_ID",row[0],"EMPLOYEE_NAME",row[8]]
    row2=["PAN",row[1],"DESIGNATION",row[9]]
    row3=["PAY_DAYS",row[3],"TOTAL_DAYS",row[11]]
    row4=["DOJ",row[4],"PAID_LEAVE",row[-2]]
    row5=["DOB",row[5],"UNPAID_LEAVE",row[-1]]
    row6=["EARNINGS","AMOUNT","DEDUCTIONS","AMOUNT"]
    row7=["BASIC",row[6],"PROFESSIONAL_TAX",row[12]]
    row8=["HRA",row[7],"PF",row[13]]
    row9=["MEDICAL_ALLOWANCE",row[15],"RETENTION_DEDUCTION",row[16]]
    row10=["TRANSPORT",row[17],"TDS",row[14]]
    row11=["EDUCATION",row[18],"",""]
    row12=["UNIFORM_ALLOWANCE",row[19],"",""]
    row13=["SPECIAL_ALLOWANCE",row[20],"",""]
    row14=["TOTAL",total,"DEDUCTIONS",deductions]
    data1=[row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,row12,row13,row14]
    t1=Table(data1,colWidths=[100,100,175,125],rowHeights=[20,20,20,20,20,20,20,20,20,20,20,20,20,20])
     
    tstyle=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
("ALIGN",(0,0),(-1,-1),"CENTER"),
("FONTSIZE",(0,0),(-1,-1),8),
("FONTSIZE",(0,5),(-1,-9),12),
("BACKGROUND",(0,5),(-1,-9),colors.yellow)])
    t1.setStyle(tstyle)
    net_pay=total-deductions
    words=num2words(net_pay, ordinal="currency", lang="en")
    text1=Paragraph("TOTAL_NETPAY:"+str(net_pay)+" INR",style=styles["Normal"])
    text2=Paragraph("IN_WORDS:"+words+" INR",style=styles["Normal"])
    flow_obj.append(t1)
    flow_obj.append(text1)
    flow_obj.append(text2)
    frame1=Frame(40,100,500,450,showBoundary=1)
    frame1.addFromList(flow_obj, pdf)
    text3=Paragraph("SIGNATURE:",style=styles["Normal"])
    flow_obj1=[]
    flow_obj1.append(text3)
    frame2=Frame(440,100,100,60,showBoundary=1)
    frame2.addFromList(flow_obj1, pdf)
    text4=Paragraph("""NOTE:THIS IS COMPUTER GENERATED DOCUENT ,HENCE NO PHYSICAL SIGNATURE REQUIRED FOR VERIFICATION
PLEASE REACH OUT TO THE HR FOR MORE INFORMATION""",style=styles["Normal"])
    frame3=Frame(40,30,500,60,showBoundary=1)
    flow_obj2=[]
    flow_obj2.append(text4)
    frame3.addFromList(flow_obj2, pdf)
    pdf.save()
    

