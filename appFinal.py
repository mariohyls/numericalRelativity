# -*- coding: utf-8 -*-


from christ import christoffel
from riem import riemman
from simulFromData import MyWidget
from plotGraphs import PlotGraphs
from changeConf import changeConf
import os

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(776, 513)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 12, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(206, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 12, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ds1 = QtWidgets.QLineEdit(self.tab)
        self.ds1.setObjectName("ds1")
        self.horizontalLayout.addWidget(self.ds1)
        self.ds2 = QtWidgets.QLineEdit(self.tab)
        self.ds2.setObjectName("ds2")
        self.horizontalLayout.addWidget(self.ds2)
        self.ds3 = QtWidgets.QLineEdit(self.tab)
        self.ds3.setObjectName("ds3")
        self.horizontalLayout.addWidget(self.ds3)
        self.ds4 = QtWidgets.QLineEdit(self.tab)
        self.ds4.setObjectName("ds4")
        self.horizontalLayout.addWidget(self.ds4)
        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 8, 0, 1, 3)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 7, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 5, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.m33 = QtWidgets.QLineEdit(self.tab)
        self.m33.setObjectName("m33")
        self.gridLayout.addWidget(self.m33, 3, 3, 1, 1)
        self.m03 = QtWidgets.QLineEdit(self.tab)
        self.m03.setText("")
        self.m03.setObjectName("m03")
        self.gridLayout.addWidget(self.m03, 0, 3, 1, 1)
        self.m32 = QtWidgets.QLineEdit(self.tab)
        self.m32.setText("")
        self.m32.setObjectName("m32")
        self.gridLayout.addWidget(self.m32, 3, 2, 1, 1)
        self.m23 = QtWidgets.QLineEdit(self.tab)
        self.m23.setText("")
        self.m23.setObjectName("m23")
        self.gridLayout.addWidget(self.m23, 2, 3, 1, 1)
        self.m31 = QtWidgets.QLineEdit(self.tab)
        self.m31.setText("")
        self.m31.setObjectName("m31")
        self.gridLayout.addWidget(self.m31, 3, 1, 1, 1)
        self.m00 = QtWidgets.QLineEdit(self.tab)
        self.m00.setObjectName("m00")
        self.gridLayout.addWidget(self.m00, 0, 0, 1, 1)
        self.m11 = QtWidgets.QLineEdit(self.tab)
        self.m11.setObjectName("m11")
        self.gridLayout.addWidget(self.m11, 1, 1, 1, 1)
        self.m12 = QtWidgets.QLineEdit(self.tab)
        self.m12.setText("")
        self.m12.setObjectName("m12")
        self.gridLayout.addWidget(self.m12, 1, 2, 1, 1)
        self.m30 = QtWidgets.QLineEdit(self.tab)
        self.m30.setText("")
        self.m30.setObjectName("m30")
        self.gridLayout.addWidget(self.m30, 3, 0, 1, 1)
        self.m02 = QtWidgets.QLineEdit(self.tab)
        self.m02.setText("")
        self.m02.setObjectName("m02")
        self.gridLayout.addWidget(self.m02, 0, 2, 1, 1)
        self.m20 = QtWidgets.QLineEdit(self.tab)
        self.m20.setText("")
        self.m20.setObjectName("m20")
        self.gridLayout.addWidget(self.m20, 2, 0, 1, 1)
        self.m13 = QtWidgets.QLineEdit(self.tab)
        self.m13.setText("")
        self.m13.setObjectName("m13")
        self.gridLayout.addWidget(self.m13, 1, 3, 1, 1)
        self.m22 = QtWidgets.QLineEdit(self.tab)
        self.m22.setObjectName("m22")
        self.gridLayout.addWidget(self.m22, 2, 2, 1, 1)
        self.m01 = QtWidgets.QLineEdit(self.tab)
        self.m01.setText("")
        self.m01.setObjectName("m01")
        self.gridLayout.addWidget(self.m01, 0, 1, 1, 1)
        self.m10 = QtWidgets.QLineEdit(self.tab)
        self.m10.setText("")
        self.m10.setObjectName("m10")
        self.gridLayout.addWidget(self.m10, 1, 0, 1, 1)
        self.m21 = QtWidgets.QLineEdit(self.tab)
        self.m21.setText("")
        self.m21.setObjectName("m21")
        self.gridLayout.addWidget(self.m21, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 6, 0, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 9, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 0, 0, 1, 1)
        self.label_4.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.label_11.raise_()
        TabWidget.addTab(self.tab, "")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab1)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.tab1)
        font = QtGui.QFont()
        font.setFamily("Liberation Serif")
        font.setPointSize(70)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 2, 1)
        self.chc = QtWidgets.QLineEdit(self.tab1)
        self.chc.setEnabled(True)
        self.chc.setObjectName("chc")
        self.gridLayout_2.addWidget(self.chc, 0, 1, 1, 1)
        self.cha = QtWidgets.QLineEdit(self.tab1)
        self.cha.setObjectName("cha")
        self.gridLayout_2.addWidget(self.cha, 1, 1, 1, 1)
        self.chb = QtWidgets.QLineEdit(self.tab1)
        self.chb.setObjectName("chb")
        self.gridLayout_2.addWidget(self.chb, 1, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.tab1)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calculate)
        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.tab1)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.sol = QtWidgets.QLabel(self.tab1)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.sol.setFont(font)
        self.sol.setObjectName("sol")
        self.horizontalLayout_2.addWidget(self.sol)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(17, 92, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem5, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(169, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(17, 91, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem7, 2, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(168, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 1, 2, 1, 1)
        TabWidget.addTab(self.tab1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem9, 1, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem10, 1, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem11, 2, 1, 1, 1)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.gridLayout_7.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("DejaVu Math TeX Gyre")
        font.setPointSize(60)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.rb = QtWidgets.QLineEdit(self.tab_2)
        self.rb.setEnabled(True)
        self.rb.setMaximumSize(QtCore.QSize(30, 16777215))
        self.rb.setObjectName("rb")
        self.gridLayout_6.addWidget(self.rb, 1, 1, 1, 1)
        self.ra = QtWidgets.QLineEdit(self.tab_2)
        self.ra.setEnabled(True)
        self.ra.setMaximumSize(QtCore.QSize(30, 16777215))
        self.ra.setObjectName("ra")
        self.gridLayout_6.addWidget(self.ra, 0, 0, 1, 1)
        self.rd = QtWidgets.QLineEdit(self.tab_2)
        self.rd.setEnabled(True)
        self.rd.setMaximumSize(QtCore.QSize(30, 16777215))
        self.rd.setObjectName("rd")
        self.gridLayout_6.addWidget(self.rd, 1, 3, 1, 1)
        self.rc = QtWidgets.QLineEdit(self.tab_2)
        self.rc.setEnabled(True)
        self.rc.setMaximumSize(QtCore.QSize(30, 16777215))
        self.rc.setObjectName("rc")
        self.gridLayout_6.addWidget(self.rc, 1, 2, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem13, 1, 4, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_6)
        self.gridLayout_7.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.calculateR = QtWidgets.QPushButton(self.tab_2)
        self.calculateR.clicked.connect(self.riemmanCalc)
        self.calculateR.setObjectName("calculateR")
        self.gridLayout_7.addWidget(self.calculateR, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 1, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem14, 0, 1, 1, 1)
        TabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.startSimulation)
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem15, 1, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem16, 0, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem17, 1, 2, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem18, 2, 1, 1, 1)
        TabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.writeStuff)

        self.verticalLayout_10.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.kickFortran)
        self.verticalLayout_10.addWidget(self.pushButton_4)
        self.gridLayout_9.addLayout(self.verticalLayout_10, 2, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem19, 2, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem20, 2, 2, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.label_15 = QtWidgets.QLabel(self.tab_4)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_5.addWidget(self.label_15)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.xmin = QtWidgets.QLineEdit(self.tab_4)
        self.xmin.setText("")
        self.xmin.setObjectName("xmin")
        self.verticalLayout_4.addWidget(self.xmin)
        self.xmax = QtWidgets.QLineEdit(self.tab_4)
        self.xmax.setText("")
        self.xmax.setObjectName("xmax")
        self.verticalLayout_4.addWidget(self.xmax)
        self.spatial_res = QtWidgets.QLineEdit(self.tab_4)
        self.spatial_res.setObjectName("spatial_res")
        self.verticalLayout_4.addWidget(self.spatial_res)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_16 = QtWidgets.QLabel(self.tab_4)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.tab_4)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_6.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.tab_4)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_6.addWidget(self.label_18)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.temp_res = QtWidgets.QLineEdit(self.tab_4)
        self.temp_res.setObjectName("temp_res")
        self.verticalLayout_7.addWidget(self.temp_res)
        self.amp = QtWidgets.QLineEdit(self.tab_4)
        self.amp.setText("")
        self.amp.setObjectName("amp")
        self.verticalLayout_7.addWidget(self.amp)
        self.sigma = QtWidgets.QLineEdit(self.tab_4)
        self.sigma.setObjectName("frecuencia")
        self.verticalLayout_7.addWidget(self.sigma)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_20 = QtWidgets.QLabel(self.tab_4)
        self.label_20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_8.addWidget(self.label_20)
        self.label_22 = QtWidgets.QLabel(self.tab_4)
        self.label_22.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_8.addWidget(self.label_22)
        self.label_21 = QtWidgets.QLabel(self.tab_4)
        self.label_21.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_8.addWidget(self.label_21)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.x0 = QtWidgets.QLineEdit(self.tab_4)
        self.x0.setText("")
        self.x0.setObjectName("x0")
        self.verticalLayout_9.addWidget(self.x0)
        self.bounda = QtWidgets.QLineEdit(self.tab_4)
        self.bounda.setText("")
        self.bounda.setObjectName("bounda")
        self.verticalLayout_9.addWidget(self.bounda)
        self.metric = QtWidgets.QLineEdit(self.tab_4)
        self.metric.setText("")
        self.metric.setObjectName("metric")
        self.verticalLayout_9.addWidget(self.metric)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)
        self.gridLayout_9.addLayout(self.horizontalLayout_9, 0, 0, 1, 3)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem21, 1, 1, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 1, 0, 1, 2)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_23 = QtWidgets.QLabel(self.tab_4)
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_11.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.tab_4)
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_11.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.tab_4)
        self.label_25.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_11.addWidget(self.label_25)
        self.gridLayout_10.addLayout(self.verticalLayout_11, 3, 0, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem22, 2, 0, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem23, 3, 1, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem24, 0, 0, 1, 1)
        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        TabWidget.addTab(self.tab_4, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "Numerical Relativity TOOLS"))
        self.label_11.setText(_translate("TabWidget", "Copyright (c) 2018 Diego Valledor & Mario González, released under the MIT License "))
        self.ds1.setText(_translate("TabWidget", "t"))
        self.ds2.setText(_translate("TabWidget", "r"))
        self.ds3.setText(_translate("TabWidget", "th"))
        self.ds4.setText(_translate("TabWidget", "fi"))
        self.label_2.setText(_translate("TabWidget", "Order of the variables in the interval:"))
        self.label_5.setText(_translate("TabWidget", "Note: You can use the following symbolic constants: G, M, R, C1, C2, C3"))
        self.label_4.setText(_translate("TabWidget", "Note: leave extra dimensions empty"))
        self.label_3.setText(_translate("TabWidget", "Metric (start from the upper left corner):"))
        self.m33.setText(_translate("TabWidget", "r**2*sin(th)**2"))
        self.m00.setText(_translate("TabWidget", "-(1-2*G*M/r)"))
        self.m11.setText(_translate("TabWidget", "1/(1-2*G*M/r)"))
        self.m22.setText(_translate("TabWidget", "r**2"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Inputs"))
        self.label.setText(_translate("TabWidget", "Γ"))
        self.chc.setText(_translate("TabWidget", "fi"))
        self.cha.setText(_translate("TabWidget", "r"))
        self.chb.setText(_translate("TabWidget", "fi"))
        self.pushButton.setText(_translate("TabWidget", "calculate"))
        self.label_6.setText(_translate("TabWidget", "Result:"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Christoffel symbols"))
        self.label_9.setText(_translate("TabWidget", "Result:"))
        self.label_8.setText(_translate("TabWidget", "R"))
        self.rb.setText(_translate("TabWidget", "r"))
        self.ra.setText(_translate("TabWidget", "t"))
        self.rd.setText(_translate("TabWidget", "r"))
        self.rc.setText(_translate("TabWidget", "t"))
        self.calculateR.setText(_translate("TabWidget", "calculate"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "Riemman tensor"))
        self.label_7.setText(_translate("TabWidget", "DataFile: "))
        self.lineEdit.setText(_translate("TabWidget", "N150.txt"))
        self.pushButton_2.setText(_translate("TabWidget", "Start!"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_3), _translate("TabWidget", "TheUniverse"))
        self.pushButton_3.setText(_translate("TabWidget", "write changes"))
        self.pushButton_4.setText(_translate("TabWidget", "run"))
        self.label_12.setText(_translate("TabWidget", "x min"))
        self.label_13.setText(_translate("TabWidget", "x max"))
        self.label_15.setText(_translate("TabWidget", "spatial resolution"))
        self.spatial_res.setText(_translate("TabWidget", "1000"))
        self.label_16.setText(_translate("TabWidget", "number of timesteps"))
        self.label_17.setText(_translate("TabWidget", "amplitude"))
        self.label_18.setText(_translate("TabWidget", "sigma"))
        self.temp_res.setText(_translate("TabWidget", "25000"))
        self.sigma.setText(_translate("TabWidget", "1"))
        self.label_20.setText(_translate("TabWidget", "x0"))
        self.label_22.setText(_translate("TabWidget", "boundaries"))
        self.label_21.setText(_translate("TabWidget", "metric"))
        self.label_23.setText(_translate("TabWidget", "Note: Boundaries can be either 0, 1, 2, or 3."))
        self.label_24.setText(_translate("TabWidget", "Note: 'metric' can be 0 (Minkowski) or 1 (Schwarzschild)"))
        self.label_25.setText(_translate("TabWidget", "Note: Default values will be used if a blank is left empty"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_4), _translate("TabWidget", "GW 1D"))


    def calculate(self):

        ds = [self.ds1.text(), self.ds2.text(), self.ds3.text(), self.ds4.text()]
        g_mn = [[self.m00.text(), self.m01.text(), self.m02.text(), self.m03.text()], \
                [self.m10.text(), self.m11.text(), self.m12.text(), self.m13.text()], \
                [self.m20.text(), self.m21.text(), self.m22.text(), self.m23.text()], \
                [self.m30.text(), self.m31.text(), self.m32.text(), self.m33.text()], \
                ]
        abc = [self.cha.text(), self.chb.text(), self.chc.text()]
        result = str(christoffel(ds, g_mn, abc))
        self.sol.setText(result)
    
    def riemmanCalc(self):

        ds = [self.ds1.text(), self.ds2.text(), self.ds3.text(), self.ds4.text()]
        g_mn = [[self.m00.text(), self.m01.text(), self.m02.text(), self.m03.text()], \
                [self.m10.text(), self.m11.text(), self.m12.text(), self.m13.text()], \
                [self.m20.text(), self.m21.text(), self.m22.text(), self.m23.text()], \
                [self.m30.text(), self.m31.text(), self.m32.text(), self.m33.text()], \
                ]
        abcd = [self.ra.text(), self.rb.text(), self.rc.text(), self.rd.text()]
        result = str(riemman(ds, g_mn, abcd))
        self.label_10.setText(result)

    def startSimulation (self):
        #MyWidget().dataFile = self.lineEdit.text()
        
        self.asd = MyWidget(self.lineEdit.text())

    def writeStuff (self):
        print("Hello!")
        xmin = self.xmin.text()
        xmax = self.xmax.text()
        spres = self.spatial_res.text()
        tpres = self.temp_res.text()
        amp = self.amp.text()
        sigma = self.sigma.text()
        x0 = self.x0.text()
        bound = self.bounda.text()
        metr = self.metric.text()

        changeConf(xmin=xmin, xmax=xmax, Nxx=spres, Ntt=tpres, \
        amplitude=amp, sigma=sigma, x0=x0, Boundaries=bound, Metric=metr)

    def kickFortran(self):
        try:
            os.system("./onda")
            print("execution is done!")
            self.zxc = PlotGraphs()
            self.zxc.dataFile = "Psi_2.x"
        except:
            print("oops :P")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())



