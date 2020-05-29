import pyodbc
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle
from reportlab.lib import colors
pdf=SimpleDocTemplate("tutorial51.pdf")
flow_obj=[]
#table header
td=[["ID","NAME","CITY","COMPANY","DEPARTMENT","DESIGNATION"]]
con_obj=pyodbc.connect("DRIVER={SQL Server};SERVER=SQL6005.site4now.net;DATABASE=DB_A432E8_totaltechnology;UID=DB_A432E8_totaltechnology_admin;PWD=Welcome@1")
data_obj=con_obj.cursor()
data_obj.execute("select * from dbo.EMP_DATA")
data_row=data_obj.fetchall()
for row in data_row:
    data=[row.ID,row.NAME,row.CITY,row.COMPANY,row.DEPARTMENT,row.DESIGNATION]
    td.append(data)
table=Table(td)
ts=TableStyle([("GRID",(0,0),(-1,-1),2,colors.red),
               ("BACKGROUND",(0,0),(-1,0),colors.yellow),
               ("BACKGROUND",(0,1),(-1,-1),colors.lightskyblue)])
table.setStyle(ts)
flow_obj.append(table)
pdf.build(flow_obj)