import sys
from PyQt5 import QtGui, QtSvg
from PyQt5.QtWidgets import QApplication, QWidget,QLabel

app = QApplication([])#sys.argv) 

widget = QLabel()
widget.setGeometry(50,200,500,500)
renderer =  QtSvg.QSvgRenderer('Zeichen_123.svg')
widget.resize(renderer.defaultSize())
painter = QtGui.QPainter(widget)
painter.restore()
renderer.render(painter)
widget.show()

sys.exit(app.exec_())
