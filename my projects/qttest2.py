import sys
from PyQt5 import QtGui, QtSvg
from PyQt5.QtWidgets import QApplication, QWidget,QLabel#,QSvgWidget

app = QApplication(sys.argv) 
svgWidget = QtSvg.QSvgWidget('animated_123.svg')
svgWidget.setGeometry(50,50,759,668)
svgWidget.show()

sys.exit(app.exec_())
