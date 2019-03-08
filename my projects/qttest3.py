import sys
from PyQt5 import QtGui, QtSvg
from PyQt5.QtWidgets import QApplication, QWidget,QLabel

app = QApplication([])#sys.argv) 

#renderer = QtSvg.QSvgRenderer('Zeichen_123.svg')
#renderer = QtSvg.QSvgRenderer('anim.svg')
renderer = QtSvg.QSvgRenderer('formula.svg')
#renderer.setFramesPerSecond(30)

image = QtGui.QImage(500,200,QtGui.QImage.Format_RGB32)#Format_RGB32
image.fill(QtGui.QColor(255,255,255))
painter = QtGui.QPainter(image)
renderer.render(painter)
image.save("output.png")

#sys.exit(app.exec_())
