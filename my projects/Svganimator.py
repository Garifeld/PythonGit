import sys
from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import *
#QMainWindow,QApplication, QWidget,QLabel,QPushButton

class Window(QMainWindow):
    
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Svg Animator")
        self.setWindowIcon(QtGui.QIcon('mainlogowhitethick.jpg'))

        ##CREATING THE MAIN MENU
        
        openSoundAction = QAction("Open new Soundfile",self)
        openSoundAction.setStatusTip("Opens a new soundfile to animate")
        openSoundAction.triggered.connect(self.notimpl)

        addSvgAction=QAction("&Add a Svg File at the current time",self)
        addSvgAction.setShortcut("Ctrl+A")
        addSvgAction.setStatusTip("Add a Svg File at the current time")
        addSvgAction.triggered.connect(self.notimpl)
        
        
        
        extractAction = QAction("&GET TO THE CHOPPA!!!",self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip("Leave the app")
        extractAction.triggered.connect(self.close_application)
        
        mainmenu = self.menuBar()
        filemenu = mainmenu.addMenu("&File")
        filemenu.addAction(openSoundAction)
        filemenu.addAction(addSvgAction)
        filemenu.addAction(extractAction)


        ### CREATING THE TOOLBAR

        toolbar= self.addToolBar("TEST")
        #TODO Fix the toolbar at the top of the frame
        dosthAction  = QAction(QtGui.QIcon("stuff.png"),'DO STH',self)
        toolbar.addAction(dosthAction)
        mainwidget=QWidget(self)
        self.setCentralWidget(mainwidget)

        hbox = QVBoxLayout(mainwidget)
        self.svgTreeView = QTreeView(self)
        self.actionPane = QFrame(self)
        self.actionPane.setFrameShape(QFrame.StyledPanel)
        self.PropertyPane = QFrame(self)
        self.PropertyPane.setFrameShape(QFrame.StyledPanel)
        
        splitter1 = QSplitter(QtCore.Qt.Horizontal,self)
        splitter1.addWidget(self.svgTreeView)
        splitter1.addWidget(self.actionPane)
        splitter1.addWidget(self.PropertyPane)
		
        hbox.addWidget(splitter1)
		
        mainwidget.setLayout(hbox)
        #wid = QtGui.QWidget(self)
        #lf.setCentralWidget(wid)
        #yout = QtGui.QVBoxLayout()
        #d.setLayout(layout)

        self.statusBar()
        self.home()

    def ignoredCode(self):
        btn = QPushButton("Quit",self)
        #btn.clicked.connect(lambda: print("ButtonPressed"))
        btn.clicked.connect(self.close_application)
        btn.resize(100, 100)
        btn.move(100, 100)
        checkBox = QCheckBox("Enlarge Window",self)
        checkBox.move(100, 25)
        checkBox.stateChanged.connect(self.enlarge_window)
        checkBox.toggle()        

    def home(self):
        self.populateTreeView()
        self.show()

    def populateTreeView(self):
        model = QtGui.QStandardItemModel(0, 1, self)
        model.setHeaderData(0, 0, "title")
        self.svgTreeView.setModel(model)
        model.insertRow(0)
        model.setData(model.index(0, 0), "teststring")
        model.insertRow(0)
        model.setData(model.index(0, 0), "teststring2")
    
        #model.setData(QtCore.QModelIndex(0),"Teststring")

    def enlarge_window(self,state):
        if state ==QtCore.Qt.Checked:
            self.setGeometry(50,50,1000,600)
        else:
            self.setGeometry(50,50,500,300)

    def notimpl(self):
        print("NOTIMPLEMENTED")
        raise NotImplementedError

    def close_application(self):
        choice = QMessageBox.question(self,"Exit ? ","Are you sure ?",QMessageBox.Yes|QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("leaving now")
        elif choice ==QMessageBox.No:
            print("You chose no!")
        print("Closed application")
        #sys.exit()

    
        
if __name__=="__main__":
    app = QApplication([])
    window = Window()
    app.exec_()
