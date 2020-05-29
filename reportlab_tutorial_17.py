#tutorial 17
#multi line paragraph

from reportlab.platypus import Paragraph ,SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet

pdf=SimpleDocTemplate("tutorial17.pdf")

flow=[]
text='''This is roni from Total Technology.<br></br>
        Please subscribe to our channel.
        Dont forget to share our videos.
        
    '''   
styles=getSampleStyleSheet() 
paragraph_text=Paragraph(text,style=styles["Normal"]) 
flow.append(paragraph_text)  
pdf.build(flow)




