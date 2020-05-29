#tutorial 36
#create index

#reportlab graphics sub package

#RECTANGLE DRAWING
from reportlab.graphics import shapes,renderPDF
from reportlab.lib import colors
drawing_obj=shapes.Drawing(500,200)
drawing_obj.add(shapes.Rect(10,10,250,100,fillColor=colors.blue))
renderPDF.drawToFile(drawing_obj,"tutorial36.pdf",msg="tutorial36")

#CIRCLE DRAWING
from reportlab.graphics import shapes,renderPDF
from reportlab.lib import colors
drawing_obj=shapes.Drawing(500,200)
drawing_obj.add(shapes.Circle(50,50,50,fillColor=colors.blue))
renderPDF.drawToFile(drawing_obj,"tutorial36.pdf",msg="tutorial36")