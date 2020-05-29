#tutorial 37
#create png

#reportlab graphics sub package save to png

#save to png

#rectangle

from reportlab.graphics import shapes,renderPM
from reportlab.lib import colors
drawing_obj=shapes.Drawing(700,800)
drawing_obj.add(shapes.Rect(20,20,300,300,fillColor=colors.green))
renderPM.drawToFile(drawing_obj,"tutorial37.png","PNG")

#circle
from reportlab.graphics import shapes,renderPM
from reportlab.lib import colors
drawing_obj=shapes.Drawing(700,800)
drawing_obj.add(shapes.Circle(150,150,75,fillColor=colors.green))
renderPM.drawToFile(drawing_obj,"tutorial37.png","PNG")