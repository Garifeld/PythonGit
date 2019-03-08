import sys
from PyQt5 import QtGui, QtSvg,QtXml,QtCore
from PyQt5.QtWidgets import QApplication, QWidget,QLabel



doc = QtXml.QDomDocument("animated_123");
file= QtCore.QFile("animated_123.svg");
#if (not file.open(QtCore.QIODevice.ReadOnly)):
doc.setContent(file);
##    file.close();
#    return;
file.close();

docElem = doc.documentElement();

n = docElem.firstChild();
depth = 0
##model = QStandartItemModel();
#curIt = QStandartItem("Tree");
#model.setItem(0,curIt)
while(not n.isNull()):
    e = n.toElement();# try to convert the node to an element.
    if(not e.isNull()):
        print("."*depth+e.tagName())
    if n.hasChildNodes():
        n =n.firstChild()
        depth+=1
    else:
        while not n.isNull() and n.nextSibling().isNull():
            depth-=1
            n=n.parentNode()
        if n.isNull():
            break;
        n=n.nextSibling()
    


