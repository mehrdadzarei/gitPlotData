
from PyQt4 import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraph.exporters
import threading, time, sys
from os.path import isfile, isdir
from numpy import linspace
from os import mkdir
import subprocess
import shutil

class RunExe(threading.Thread):
        
    def __init__(self, name):
        threading.Thread.__init__(self)
        
        self.nameEx = name
                
    def run(self):
        
        # system('ftdxx245')
        try:
                
            self.p = subprocess.Popen([self.nameEx])
        except: pass                       

    def ex(self):
        
        try:
        
            self.p.terminate()
        except: pass
        
class Ui_MainWindow(object):
    
    end = 0
    def setupUi(self, MainWindow):
                
        self.mypath = 'C:\\JAHAD\\data'
        self.nameEx = 'C:\\JAHAD\\ftdxx245.exe'                
        self.sv = 1    # for get folder path
        self.nw = 1    # for new button
        self.sp = 0    # for stop button
        self.up = 0    # for update function
        self.cntF = 0  # counter of files
        self.nF = 0    # number of files
        self.framRate = 2 # frame rate
        
        MainWindow.setWindowTitle("Plot")
        MainWindow.resize(800, 500)
        MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("img\\icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(self.icon)
        
        self.font = QtGui.QFont()
        self.font.setPointSize(10)
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.grid = QtGui.QGridLayout()
                                       
        self.run = QtGui.QPushButton(self.centralwidget)
        self.run.setText("Run")
        self.grid.addWidget(self.run, 0, 0)
        self.run.clicked.connect(self.Run)
        self.run.setAutoDefault(True)       # for use of enter key instead of click
        self.grid.setAlignment(QtCore.Qt.AlignTop)  # set Alignment button on top
        self.run.setFont(self.font)
        
        self.stop = QtGui.QPushButton(self.centralwidget)
        self.stop.setText("Stop")
        # self.stop.setEnabled(False)
        self.grid.addWidget(self.stop, 0, 1)
        self.stop.clicked.connect(self.Stop)
        self.stop.setAutoDefault(True)
        self.stop.setFont(self.font)
        
        self.setFrame = QtGui.QPushButton(self.centralwidget)
        self.setFrame.setText("Set Frame")
        # self.setFrame.setEnabled(False)
        self.grid.addWidget(self.setFrame, 0, 2)
        self.setFrame.clicked.connect(self.SetFrame)
        self.setFrame.setAutoDefault(True)
        self.setFrame.setFont(self.font)
        
        self.exit = QtGui.QPushButton(self.centralwidget)
        self.exit.setText("Exit")
        # self.exit.setEnabled(False)
        self.grid.addWidget(self.exit, 0, 3)
        self.exit.clicked.connect(self.Exit)        
        self.exit.setAutoDefault(True)
        self.exit.setFont(self.font)
        
        self.plotD = pg.PlotWidget(title = '')        
        self.plotD.setLabels(left = ('Amplitude'), bottom = ('time (s)'))        
        self.plotD.setMouseEnabled(x = False, y = False)        
        self.plotD.clear()        
        self.plotData = self.plotD.plot(pen = (0,255,0))
        self.grid.addWidget(self.plotD, 1, 0, 10, 4)
        # self.exporter = pg.exporters.ImageExporter(self.plotD.plotItem)
        # self.exporter.parameters()['width'] = 800
                       
        self.centralwidget.setLayout(self.grid)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setTitle("File")
        self.menuRun = QtGui.QMenu(self.menubar)
        self.menuRun.setTitle("Run")
        # self.menuSetting = QtGui.QMenu(self.menubar)
        # self.menuSetting.setTitle("Settings")
        MainWindow.setMenuBar(self.menubar)       
        
        self.actionNew_Ctrl_C = QtGui.QAction(MainWindow)
        self.actionNew_Ctrl_C.setText("Stop")
        self.actionNew_Ctrl_C.setShortcut('Ctrl+c')
        self.actionNew_Ctrl_C.triggered.connect(self.Stop)
        self.actionNew_Ctrl_C.setFont(self.font)
        
        # self.actionSave_Ctrl_S = QtGui.QAction(MainWindow)
        # self.actionSave_Ctrl_S.setText("Save")
        # self.actionSave_Ctrl_S.setShortcut('Ctrl+s')
        # self.actionSave_Ctrl_S.triggered.connect(self.Save)
        # self.actionSave_Ctrl_S.setFont(self.font)
        
        self.actionQuit_Ctrl_Q = QtGui.QAction(MainWindow)
        self.actionQuit_Ctrl_Q.setText("Quit\tAlt+F4")
        self.actionQuit_Ctrl_Q.triggered.connect(QtGui.qApp.quit)
        self.actionQuit_Ctrl_Q.setFont(self.font)
        
        self.actionRun_Ctrl_R = QtGui.QAction(MainWindow)
        self.actionRun_Ctrl_R.setText("Run")        
        self.actionRun_Ctrl_R.setShortcut('Ctrl+r')
        self.actionRun_Ctrl_R.triggered.connect(self.Run)
        self.actionRun_Ctrl_R.setFont(self.font)
        
        # self.actionPause_Ctrl_P = QtGui.QAction(MainWindow)
        # self.actionPause_Ctrl_P.setText("Pause")
        # self.actionPause_Ctrl_P.setEnabled(False)
        # self.actionPause_Ctrl_P.setShortcut('Ctrl+p')
        # self.actionPause_Ctrl_P.triggered.connect(self.Pause)
        # self.actionPause_Ctrl_P.setFont(self.font)
        
        # self.actionStop_Ctrl_F = QtGui.QAction(MainWindow)
        # self.actionStop_Ctrl_F.setText("Stop")
        # self.actionStop_Ctrl_F.setEnabled(False)
        # self.actionStop_Ctrl_F.setShortcut('Ctrl+f')
        # self.actionStop_Ctrl_F.triggered.connect(self.Stop)
        # self.actionStop_Ctrl_F.setFont(self.font)
        
        # self.actionSetting = QtGui.QAction(MainWindow)
        # self.actionSetting.setText("Settings")
        # self.actionSetting.triggered.connect(self.Setting)
        # self.actionSetting.setFont(self.font)
        
        # self.menuFile.addAction(self.actionNew_Ctrl_C)
        # self.menuFile.addAction(self.actionSave_Ctrl_S)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit_Ctrl_Q)
        
        self.menuRun.addAction(self.actionRun_Ctrl_R)
        self.menuRun.addAction(self.actionNew_Ctrl_C)
        # self.menuRun.addAction(self.actionStop_Ctrl_F)
        
        # self.menuSetting.addAction(self.actionSetting)
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())
        # self.menubar.addAction(self.menuSetting.menuAction())

        # self.Setting()
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def Run(self):

        if self.nw:
        
            self.data = []
            flag = 1
            try:
            
                shutil.rmtree(self.mypath)
                mkdir(self.mypath)
            except: pass
            if not isdir(self.mypath):
                
                self.mypath = str(QtGui.QFileDialog.getExistingDirectory(None,
                    "Select Directory for data files", 'C:\\JAHAD\\', QtGui.QFileDialog.ShowDirsOnly))                
                if self.mypath[-4:] != 'data':
                    
                    print 'Invalid Directory for data files'
                    self.mypath = 'C:\\JAHAD\\data'
                    self.up = 0
                    self.nw = 1
                    self.sp = 0
                    flag = 0
            
            if flag:

                if not isfile(self.nameEx):        
                               
                    self.nameEx = str(QtGui.QFileDialog.getOpenFileName(None,
                        "Select ftdxx245.exe file", 'C:\\JAHAD\\'))
                    
                    if self.nameEx[-12:] != 'ftdxx245.exe':
                    
                        print 'Invalid ftdxx245.exe file'
                        self.nameEx = 'C:\\JAHAD\\ftdxx245.exe'
                        self.up = 0
                        self.nw = 1
                        self.sp = 0
                    else:
                
                        self.threadRun = RunExe(self.nameEx)
                        self.threadRun.start()  
                        self.respath = self.mypath[:len(self.mypath)-4] + 'rec\\peakToPeak.txt'
                        if isdir(self.respath[:len(self.respath)-15]):
                        
                            shutil.rmtree(self.respath[:len(self.respath)-15])                        
                            mkdir(self.respath[:len(self.respath)-15])
                        else:
                        
                            mkdir(self.respath[:len(self.respath)-15])
                        self.filename = open(self.respath, 'w')                        
                        self.nw = 0
                        self.sp = 1
                        self.cntF = 0
                        self.up = 1
                else:
                    
                    try:
                        
                        self.threadRun = RunExe(self.nameEx)
                        self.threadRun.start()                        
                        self.respath = self.mypath[:len(self.mypath)-4] + 'rec\\peakToPeak.txt'
                        if isdir(self.respath[:len(self.respath)-15]):
                        
                            shutil.rmtree(self.respath[:len(self.respath)-15])                        
                            mkdir(self.respath[:len(self.respath)-15])
                        else:
                        
                            mkdir(self.respath[:len(self.respath)-15])
                        self.filename = open(self.respath, 'w')
                        self.nw = 0
                        self.sp = 1
                        self.cntF = 0
                        self.up = 1
                    except: pass
                      
    def Stop(self):
        
        if self.sp:
            
            try:
                self.threadRun.ex()
                self.filename.close()
                self.up = 1
                self.nw = 1            
            except: pass
    
    def SetFrame(self):
        
        num,ok = QtGui.QInputDialog.getInt(None,"Set Frame",
            "Enter Frame Rate")
        if ok:
            
            self.framRate = num
    
    def Exit(self):
        
        QtCore.QCoreApplication.instance().quit()
    
    def update(self):
        
        if Ui_MainWindow.end:
            
            try:    
                
                self.threadRun.ex()
            except: pass
        
        if self.up:
            
            try:
                            
                name = self.mypath + '\\Frame' + `self.cntF` + '.txt'
                if isfile(name):
                    
                    f = open(name)
                    content = f.readlines()
                    f.close()
                    for x in content:

                        self.data.append(float(x.strip())*3.3/65536)
                    tm = linspace(self.cntF/float(self.framRate), (self.cntF+1)/float(self.framRate), 500)
                    tm.reshape(-1,500).tolist()
                    data = self.data[0:500]
                    del self.data[0:500]
                    self.plotData.setData(tm, data)
                    minData = float("%.6f" % min(data))
                    maxData = float("%.6f" % max(data))
                    peakToPeak = float("%.6f" % (maxData-minData))
                    self.plotD.setTitle("min = " + `minData` + "; max = " + `maxData` + "; peak to peak = " + `peakToPeak`)
                    # self.exporter.export('Frame0.png')
                    self.filename.write(`peakToPeak`)
                    self.filename.write('\n')
                    self.cntF += 1
                    self.up = 0
                        
            except: pass
            
if __name__ == "__main__":
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(ui.update)
    timer.start(10)                        # 100ms for 10 fps
    if sys.flags.interactive == 0:        
        try:
            app.exec_()		# execaution file
        except: pass
        Ui_MainWindow.end = 1
        ui.update()
