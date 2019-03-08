# reads an animated svg filename, an audiofilename
# and creates a video (without sound) containing an animation of the svg file
# afterwards it also creates a video with sound
 
from PyQt5 import QtGui, QtSvg, QtCore
import cv2
import np
#import pymedia


def convertQImageToMat(incomingImage):
    '''  Converts a QImage into an opencv MAT format  '''
    incomingImage = incomingImage.convertToFormat(4)

    width = incomingImage.width()
    height = incomingImage.height()

    ptr = incomingImage.bits()
    ptr.setsize(incomingImage.byteCount())
    arr = np.array(ptr).reshape(height, width, 4)  #  Copies the data
    return arr

file=QtCore.QFile("animated_123.svg");
if(file.open(QtCore.QIODevice.ReadOnly)):
    xmlReader=QtCore.QXmlStreamReader();
    xmlReader.setDevice(file);
    xmlReader.readNext();
    #Reading from the file
    while (not xmlReader.isEndDocument()):
        #if (xmlReader.isStartElement()):
        #    name = xmlReader.name().toString();
        #    print(name)
        #elif (xmlReader.isEndElement()):
        #    xmlReader.readNext();
        #print(xmlReader.readNext())
        xmlReader.readNext()
        pref = ""
        if (xmlReader.isStartElement()):
            pref="start: "
        if (xmlReader.isEndElement()):
            pref="end: "
        
        print(pref+xmlReader.name())
    if (xmlReader.hasError()):
        print("XML error: %s" %xmlReader.errorString());
#reader=QtCore.QXmlStreamReader(f)
#print(reader.readNext())


#renderer = QtSvg.QSvgRenderer('animated_123.svg')
#renderer.setFramesPerSecond(30)
#print(renderer.animated())

#image = QtGui.QImage(500,500,QtGui.QImage.Format_RGB32)#Format_RGB32
#painter = QtGui.QPainter(image)
#writer = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"MJPG"), 30,(500,500))
#for i in range(90):
#    print(i)
#    image.fill(QtGui.QColor(255,255,255))
#    renderer.render(painter)
#    renderer.setCurrentFrame(i*1000)
#    image.save("outputimage_%i.png"%i)
    
    #writer.write(convertQImageToMat(image).astype('uint8'))

#writer.release()
#cv2.destroyAllWindows()
