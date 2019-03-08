from PyQt5 import QtGui, QtSvg

renderer = QtSvg.QSvgRenderer()
if renderer.load('anim.svg'):
    print("load successful")
else:
    print("load not successful")

#renderer.setFramesPerSecond(30)
print(renderer.animated())
