# import matplotlib.pyplot as plt
# from PIL import Image
import cv2
import os
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog

# overwrite
'''
class MyLineEdit(QLineEdit):
    clicked = pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() ==Qt.LeftButton:
            self.clicked.emit()
            '''


class Photo_Chose(object):
    # a is drawing x
    # b is drawing y
    # c is click x
    # d si click y
    def get_Pos(self, photodir):
        self.img = cv2.imread(photodir)
        self.a = []
        self.b = []
        self.c = []
        self.d = []
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", self.on_EVENT_MOUSE)
        cv2.imshow("image", self.img)
        cv2.waitKey(0)
        return self.a, self.b, self.c, self.d

    def on_EVENT_MOUSE(self, event, x, y, flags, param):
        if flags == cv2.EVENT_FLAG_CTRLKEY:
            xy = "%d,%d" % (x, y)
            self.a.append(x)
            self.b.append(y)
            cv2.circle(self.img, (x, y), 1, (0, 0, 255), thickness=-1)
            cv2.imshow("image", self.img)
        elif event == cv2.EVENT_LBUTTONDOWN:
            xy = '%d,%d' % (x, y)
            self.c.append(x)
            self.d.append(y)
            cv2.circle(self.img, (x, y), 2, (0, 255, 0), thickness=-1)
            cv2.imshow('image', self.img)
        elif event == cv2.EVENT_RBUTTONDOWN:
            try:
                cre = self.c.pop()
                dre = self.d.pop()
                cv2.circle(self.img, (cre, dre), 2, (255, 99, 71), thickness=-1)
                cv2.imshow('image', self.img)
            except:
                print('Error in cancelling chosen point')
        elif flags == cv2.EVENT_FLAG_ALTKEY:
            try:
                are = self.a.pop()
                bre = self.b.pop()
                cv2.circle(self.img, (are, bre), 1, (255, 218, 185), thickness=-1)
                cv2.imshow('image', self.img)
            except:
                print('Error in cancelling chosen point')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(845, 567)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QtCore.QSize(10, 0))
        self.label_12.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 9, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 2, 1, 1)

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(20, 0))
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(0, 30))
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 9, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_2.addWidget(self.radioButton_2, 3, 7, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_2.addWidget(self.radioButton, 4, 7, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(100, 70))
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 8, 7, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Times New Roman')
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(70, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(130, 60))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 5, 7, 1, 1)

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 5, 5, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setMinimumSize(QtCore.QSize(70, 0))
        self.checkBox.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setIconSize(QtCore.QSize(40, 40))
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 3, 5, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_7.setTextFormat(QtCore.Qt.PlainText)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 3, 1, 3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 6, 1, 2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 1, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QtCore.QSize(10, 0))
        self.label_13.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 3, 8, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Arial Narrow')
        font.setPointSize(16)
        self.textBrowser.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 50))
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 60))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 0, 1, 1, 5)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Myungjo Std M")
        font.setPointSize(12)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(90, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(120, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 6, 7, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 6, 5, 1, 1)

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(20, 0))
        self.label_11.setMaximumSize(QtCore.QSize(16677215, 16777215))
        self.label_11.setText("")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 2, 6, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily('Times New Roman')
        font.setPointSize(16)
        self.lineEdit_3.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(16777215, 120))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 5, 2, 2, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 120))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 3, 2, 2, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(16777215, 120))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 8, 2, 1, 1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bodoni MT Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 1, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 5, 1, 3, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 8, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.menuappendix()
        self.links()
        self.retranslateUi(MainWindow)
        self.shortCut()
        self.styles()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def styles(self):
        mainWindow.setWindowIcon(QIcon('main.ico'))
        mainWindow.setStyleSheet('QMainWindow{border-image:url(bg1.png);}')
        self.pushButton.setStyleSheet('border-radius:10px;border-image:url(go.jpg)')
        self.pushButton_2.setStyleSheet('border-radius:4px;border: 2px solid orange; background:rgb(64,224,208)')
        self.textBrowser.setStyleSheet(
            'border:2px solid pink;border-radius:10px;padding:2px 4px;background:rgba(171,130,255,0.8)')
        linestyl = 'border:5px solid orange; border-radius:20px;padding: 2px 4px;background:rgba(250,128,114,0.7)'
        statusstyl = 'border-radius:5px;background:rgb(171,130,255)'
        labelhdstyl = 'border: 2px solid pink;border-radius:4px; background:rgba(255,218,185,0.8)'
        filterstyl = 'border:2px solid pink;border-radius:3px;background:rgba(171,130,255,0.7)'
        projstyl = filterstyl
        radiostyl = 'border:3px solid orange;border-radius:7px;padding: 2px 4px;background:rgba(255, 62 ,150,0.5)'
        pointstyl = 'border:3px solid orange;border-radius:7px;padding:2px 4px;background:rgba(250,128,114,0.7)'
        self.label_6.setStyleSheet(labelhdstyl)
        self.label_7.setStyleSheet(labelhdstyl)
        self.label_5.setStyleSheet(labelhdstyl)
        self.checkBox.setStyleSheet(filterstyl)
        self.radioButton.setStyleSheet(radiostyl)
        self.radioButton_2.setStyleSheet(radiostyl)
        self.label_8.setStyleSheet(projstyl)
        self.lineEdit.setStyleSheet(pointstyl)
        self.lineEdit_2.setStyleSheet(linestyl)
        self.lineEdit_3.setStyleSheet(linestyl)
        self.lineEdit_4.setStyleSheet(linestyl)
        self.statusbar.setStyleSheet(statusstyl)

    def menuappendix(self):
        self.actionAuthor = QtWidgets.QAction(mainWindow)
        self.menuShortcut = QtWidgets.QMenu(mainWindow)
        self.actionAuthor.setObjectName('actionAuthor')
        self.menuShortcut.setObjectName('menuShortcut')
        self.actionSc1 = QtWidgets.QAction(mainWindow)
        self.actionSc2 = QtWidgets.QAction(mainWindow)
        self.actionSc3 = QtWidgets.QAction(mainWindow)
        self.actionSc4 = QtWidgets.QAction(mainWindow)
        self.actionSc5 = QtWidgets.QAction(mainWindow)
        self.actionSc1.setObjectName('actionSc1')
        self.actionSc2.setObjectName('actionSc2')
        self.actionSc3.setObjectName('actionSc3')
        self.actionSc4.setObjectName('actionSc4')
        self.actionSc5.setObjectName('actionSc5')
        self.menuAbout.addAction(self.actionAuthor)
        self.menuHelp.addMenu(self.menuShortcut)
        self.actionAuthor.triggered.connect(self.action_author)
        self.menuShortcut.addAction(self.actionSc1)
        self.menuShortcut.addAction(self.actionSc2)
        self.menuShortcut.addAction(self.actionSc3)
        self.menuShortcut.addAction(self.actionSc4)
        self.menuShortcut.addAction(self.actionSc5)

    def action_author(self):
        import webbrowser
        webbrowser.open('https://zekyou.github.io')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ZkPhoto"))
        self.label.setText(_translate("MainWindow", "Basic Position"))
        self.label_3.setText(_translate("MainWindow", "2"))
        self.radioButton_2.setText(_translate("MainWindow", "All Point\n"
                                                            "(Not recommended)"))
        self.radioButton.setText(_translate("MainWindow", "Specify Point\n"
                                                          "(Start Inc End)"))
        self.pushButton.setText(_translate("MainWindow", ""))
        #    self.lineEdit.setText(_translate("MainWindow", "Start Increment End"))
        self.lineEdit_3.setText(_translate('MainWindow', 'Not Used'))
        self.lineEdit_4.setText(_translate('MainWindow', 'Not Used'))
        self.label_6.setText(_translate("MainWindow", "OPTION"))
        self.label_8.setText(_translate("MainWindow", "Projection"))
        self.checkBox.setText(_translate("MainWindow", "Filter"))
        self.label_7.setText(_translate("MainWindow", "INPUT"))
        self.label_4.setText(_translate("MainWindow", "3"))
        self.pushButton_2.setText(_translate("MainWindow", "From File"))
        self.comboBox.setItemText(0, _translate("MainWindow", "-Jx/X"))
        self.comboBox.setItemText(1, _translate("MainWindow", "-JM"))
        self.label_5.setText(_translate("MainWindow", "OPERATE"))
        self.label_2.setText(_translate("MainWindow", "1"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionAuthor.setText(_translate('MainWindow', 'Author'))
        self.menuShortcut.setTitle(_translate('MainWindow', 'Shortcuts'))
        self.actionSc1.setText(_translate('MainWindow', 'OpenFile(ctrl+o)'))
        self.actionSc2.setText(_translate('MainWindow', 'GO/Statr(ctrl+g)'))
        self.actionSc3.setText(_translate('MainWindow', 'UsingFilter(ctrl+f)'))
        self.actionSc4.setText(_translate('MainWindow', 'ChooseAllPoint(alt+a)'))
        self.actionSc5.setText(_translate('MainWindow', 'ChooseSpePoint(alt+s)'))

    def shortCut(self):
        self.actionOpen.setShortcut('ctrl+o')
        self.pushButton.setShortcut('ctrl+g')
        self.pushButton_2.setShortcut('ctrl+f')
        self.radioButton.setShortcut('alt+s')
        self.radioButton_2.setShortcut('alt+a')

    def links(self):
        self.pushButton.clicked.connect(self.calcu)
        self.pushButton_2.clicked.connect(self.openSP)
        self.actionOpen.triggered.connect(self.openImg)

    def clearTips(self):
        self.lineEdit.setText('')

    def openSP(self):
        pass

    def openImg(self):
        global plotpx, plotpy, basicx, basicy
        plotpx = []
        plotpy = []
        basicx = []
        basicy = []
        try:
            fname, _ = QFileDialog.getOpenFileName(None, 'Select Picture', os.getcwd(),
                                                   'All Files(*);;Photo Files(*.png)', 'Photo Files(*.png)')
            pChose = Photo_Chose()
            self.textBrowser.setText(fname)
            plotpx, plotpy, basicx, basicy = pChose.get_Pos(fname)
        except:
            self.statusbar.showMessage('Invalid Picture File', 1000)

    def getypixel(self, xpixel):
        for i in range(len(plotpx) - 1):
            flag = (xpixel - plotpx[i]) * (xpixel - plotpx[i + 1])
            if flag <= 0:
                ypixel = (plotpy[i] + plotpy[i + 1]) / 2
                return ypixel
                break
            else:
                continue

    def writetxt(self, spex, spey):
        dir = self.textBrowser.toPlainText()
        txtdir = os.path.splitext(dir)[0] + '.txt'
        ftxt = open(txtdir, 'w')
        for i in range(len(spex)):
            txtline = str(round(spex[i], 4)) + '\t' + str(round(spey[i], 4)) + '\n'
            ftxt.write(txtline)
        ftxt.close()

    def calcu(self):
        try:
            bposx, bposy = self.basicPos()
            # modified v1.2
            for i in range(3):
                if bposy[i] - bposy[0] == 0:
                    continue
                else:
                    yinc = (basicy[i] - basicy[0]) / (bposy[i] - bposy[0])
                    break
            for i in range(3):
                if bposx[i] - bposx[0] == 0:
                    continue
                else:
                    xinc = (basicx[i] - basicx[0]) / (bposx[i] - bposx[0])
                    break
        except:
            self.statusbar.showMessage('Invalid Basic Position', 700)
        self.filter()
        self.projection()
        if self.radioButton.isChecked():
            try:
                spex = self.pointType()
            except:
                self.statusbar.showMessage('Invalid Input of Specified Point', 1000)
            spey = []
            #    xinc = (bposx[2]-bposx[1])/(basicx[2]-basicx[1])
            #    yinc = (bposy[1]-bposy[0])/(basicy[1]-basicy[0])

            try:
                for i in range(len(spex)):
                    xpixel = (spex[i] - bposx[1]) * xinc + basicx[1]
                    ypixel = self.getypixel(xpixel)
                    spey.append((ypixel - basicy[1]) / yinc + bposy[1])
            except:
                self.statusbar.showMessage('Error in calculating position. Ploting Window may not be closed', 2000)
        elif self.radioButton_2.isChecked():
            spex = []
            spey = []
            for i in range(len(plotpx)):
                spex.append(bposx[0] + (plotpx[i] - basicx[0]) / xinc)
                spey.append(bposy[0] + (plotpy[i] - basicy[0]) / yinc)
        try:
            self.writetxt(spex, spey)
            self.statusbar.showMessage('Write txt successfully!', 1000)
        except:
            self.statusbar.showMessage('Error at writing txt', 500)

    def basicPos(self):
        bpos = self.lineEdit_2.text()
        bpos = list(map(float, bpos.split()))
        bposx = bpos[::2];
        bposy = bpos[1::2]
        return bposx, bposy

    def filter(self):
        if self.checkBox.isChecked():
            pass

    def projection(self):
        if self.comboBox.currentIndex() == 1:
            pass
        elif self.comboBox.currentIndex() == 2:
            pass

    def pointType(self):
        if self.radioButton.isChecked():
            spe_point = self.lineEdit.text()
            spe_point = list(map(float, spe_point.split()))
            if spe_point[2] < spe_point[0]:
                self.statusbar.showMessage('Invalid Start and End point', 1000)
            else:
                i = 0
                spex = [spe_point[0]]
                while (spex[-1] < spe_point[2]):
                    spex.append(spe_point[0] + spe_point[1] * (i + 1))
                    i = i + 1
                return spex
        else:
            pass


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())
