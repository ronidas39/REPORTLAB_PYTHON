#tutorial 40
#create multiple barcode file for inventory list
#reportlab graphics sub package to generate barcode for proucts inventory
from reportlab.platypus import Paragraph,SimpleDocTemplate,Spacer
from reportlab.graphics.barcode import code39
from reportlab.lib.styles import getSampleStyleSheet
import csv
styles=getSampleStyleSheet()
with open("data.csv")as f1:
    datarow=csv.reader(f1,delimiter=",")
    for row in datarow:
        pdf=SimpleDocTemplate(row[0]+"-"+row[1]+"-"+row[2]+".pdf")
        flow_obj=[]
        barcode_text="-"+row[0]+"-"+row[1]+"-"+row[2]+"-"+row[3]+"-"+row[4]+"-"
        barcode=code39.Standard39(barcode_text)
        flow_obj.append(barcode)
        flow_obj.append(Spacer(1,10))
        text=row[0]+"-"+row[1]+"-"+row[2]
        ptext=Paragraph(text,style=styles["Normal"])
        flow_obj.append(ptext)
        pdf.build(flow_obj)
    

