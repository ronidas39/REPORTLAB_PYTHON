import requests
import os
import datetime
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Paragraph,Table,TableStyle,Frame,Spacer,Image
from reportlab.lib.styles import getSampleStyleSheet
import json
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams.update({"figure.max_open_warning":0})


url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "7d18fd6581msh81a4886d454a322p1e64c5jsn2c784c87b0cf"
    }

response = requests.request("GET", url, headers=headers)
data=response.text
data=json.loads(data)
pdf=canvas.Canvas("report.pdf")
flow_obj1=[]
flow_obj2=[]
styles=getSampleStyleSheet()
for i in range(len(data["response"])):
    #print(data["response"][i]["deaths"])
    country=data["response"][i]["country"]
    total=data["response"][i]["cases"]["total"]
    active=data["response"][i]["cases"]["active"]
    recovered=data["response"][i]["cases"]["recovered"]
    critical=data["response"][i]["cases"]["critical"]
    new=data["response"][i]["cases"]["new"]
    total_deaths=data["response"][i]["deaths"]["total"]
    new_deaths=data["response"][i]["deaths"]["new"]
    dc={}
    try:
        dc.update({"total_case":int(total)})
        dc.update({"active_case":int(active)})
        dc.update({"recovered_case":int(recovered)})
        dc.update({"critical_case":int(critical)})
        dc.update({"new_case":int(new)})
        dc.update({"total_deaths":int(total_deaths)})
        dc.update({"new_deaths":int(new_deaths)})
    except:
        pass
    df=pd.DataFrame.from_dict(dc, orient="index",columns=["ALL CATEGORIES"])
    fig=plt.figure(figsize=(40,10))
    plt.style.use("dark_background")
    df["ALL CATEGORIES"].plot(kind="bar",color=["red","blue","green","yellow","brown","skyblue","purple"],fontsize=40)
    plt.xlabel("ALL CATEGORIES",fontsize=50,color="red",fontweight="bold")
    plt.grid(b=True,which="both",color="white",linestyle="-")
    plt.title("Data of corona virus for : "+ country,color="blue",fontsize=80)
    plt.savefig("pic.png",bbox_inches="tight")
    text='''
This is the data of <b> {} </b> ,<br></br>'''.format(country)
    t1=Paragraph(text,style=styles["Normal"])
    flow_obj1.append(t1)
    flow_obj1.append(Spacer(6,6))
    text1="data generated at : "+ str(datetime.datetime.now())
    t2=Paragraph(text1,style=styles["Normal"])
    flow_obj1.append(t2)
    flow_obj1.append(Spacer(6,6))
    frame=Frame(40,600,500,100,showBoundary=1)
    table1=Table([["total","active_cases","recovered","critical_cases","new_cases","total_deaths","new_daths"],
                   [total,active,recovered,critical,new,total_deaths,new_deaths]])
    ts=TableStyle([("GRID",(0,0),(-1,-1),2,colors.red),
                   ("BACKGROUND",(0,0),(-1,-1),colors.yellow)])
    table1.setStyle(ts)
    flow_obj1.append(table1)
    frame.addFromList(flow_obj1, pdf)
    im=Image("pic.png",400,150)
    table2=Table([[im]])
    flow_obj2.append(table2)
    frame2=Frame(40,400,500,200,showBoundary=1)
    frame2.addFromList(flow_obj2, pdf)
    pdf.showPage()
    print(i)
pdf.save()
    
