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

N = docElem#.firstChild();
n=N
#n.toElement().QIt  = QtGui.QStandardItem("Godfather")
depth = 0
model = QtGui.QStandardItemModel();
curIt = QtGui.QStandardItem("My File");
model.setItem(0,curIt)
#self.svgTreeView.setModel(model)
while(not n.isNull()):
    e = n.toElement();# try to convert the node to an element.
    if(not n.isNull()):
        print("."*depth+e.tagName())
        nextIt = QtGui.QStandardItem(e.tagName());
        curIt.appendRow(nextIt);
        print("Parent did %swork"%("not " if nextIt.parent()==curIt else ""))
        curIt=nextIt
    if n.hasChildNodes():
        n = n.firstChild()
        depth+=1
    else:
        while not n.isNull() and n.nextSibling().isNull():
            depth-=1
            n=n.parentNode()
            curIt=curIt.parent()
        if n.isNull():
            break;
        n=n.nextSibling()
        curIt=curIt.parent()
        
    


