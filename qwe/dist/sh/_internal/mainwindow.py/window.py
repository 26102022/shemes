# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 1072)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 860, 691, 91))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.mplWidget = QtWidgets.QWidget(self.centralwidget)
        self.mplWidget.setGeometry(QtCore.QRect(20, 520, 691, 341))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mplWidget.setFont(font)
        self.mplWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.mplWidget.setObjectName("mplWidget")
        self.ininsk = QtWidgets.QCheckBox(self.centralwidget)
        self.ininsk.setGeometry(QtCore.QRect(20, 460, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.ininsk.setFont(font)
        self.ininsk.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.ininsk.setObjectName("ininsk")
        self.mplWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.mplWidget_2.setGeometry(QtCore.QRect(910, 0, 650, 500))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mplWidget_2.setFont(font)
        self.mplWidget_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.mplWidget_2.setObjectName("mplWidget_2")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 240, 901, 221))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_6.addWidget(self.label_16)
        self.inskv = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.inskv.setFont(font)
        self.inskv.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.inskv.setMaxVisibleItems(17)
        self.inskv.setObjectName("inskv")
        self.inskv.addItem("")
        self.inskv.addItem("")
        self.inskv.addItem("")
        self.inskv.addItem("")
        self.inskv.addItem("")
        self.inskv.addItem("")
        self.inskv.addItem("")
        self.inskv.addItem("")
        self.inskv.addItem("")
        self.inskv.addItem("")
        self.inskv.addItem("")
        self.inskv.addItem("")
        self.inskv.addItem("")
        self.inskv.addItem("")
        self.inskv.addItem("")
        self.inskv.addItem("")
        self.inskv.addItem("")
        self.inskv.addItem("")
        self.verticalLayout_6.addWidget(self.inskv)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_35 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_35.setFont(font)
        self.label_35.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_10.addWidget(self.label_35)
        self.mid_in = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mid_in.setFont(font)
        self.mid_in.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.mid_in.setObjectName("mid_in")
        self.verticalLayout_10.addWidget(self.mid_in)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_16.addWidget(self.label_11)
        self.sig_in = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sig_in.setFont(font)
        self.sig_in.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.sig_in.setObjectName("sig_in")
        self.verticalLayout_16.addWidget(self.sig_in)
        self.horizontalLayout.addLayout(self.verticalLayout_16)
        self.verticalLayout_8.addLayout(self.horizontalLayout)
        self.horizontalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setScaledContents(False)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_9.addWidget(self.label_12)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_18.addWidget(self.label_18)
        self.vrub = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.vrub.setFont(font)
        self.vrub.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.vrub.setObjectName("vrub")
        self.vrub.addItem("")
        self.vrub.addItem("")
        self.vrub.addItem("")
        self.vrub.addItem("")
        self.vrub.addItem("")
        self.vrub.addItem("")
        self.vrub.addItem("")
        self.verticalLayout_18.addWidget(self.vrub)
        self.horizontalLayout_3.addLayout(self.verticalLayout_18)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_21.setFont(font)
        self.label_21.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_19.addWidget(self.label_21)
        self.mid_vr = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mid_vr.setFont(font)
        self.mid_vr.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.mid_vr.setObjectName("mid_vr")
        self.verticalLayout_19.addWidget(self.mid_vr)
        self.horizontalLayout_3.addLayout(self.verticalLayout_19)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_65 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_65.setFont(font)
        self.label_65.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_65.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_65.setObjectName("label_65")
        self.verticalLayout_20.addWidget(self.label_65)
        self.sig_vr = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sig_vr.setFont(font)
        self.sig_vr.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.sig_vr.setObjectName("sig_vr")
        self.verticalLayout_20.addWidget(self.sig_vr)
        self.horizontalLayout_3.addLayout(self.verticalLayout_20)
        self.verticalLayout_17.addLayout(self.horizontalLayout_3)
        self.verticalLayout_9.addLayout(self.verticalLayout_17)
        self.horizontalLayout_9.addLayout(self.verticalLayout_9)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_40 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_40.setFont(font)
        self.label_40.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_40.setTextFormat(QtCore.Qt.AutoText)
        self.label_40.setScaledContents(False)
        self.label_40.setWordWrap(True)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_11.addWidget(self.label_40)
        self.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_22.addWidget(self.label_23)
        self.esh = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.esh.setFont(font)
        self.esh.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.esh.setObjectName("esh")
        self.esh.addItem("")
        self.esh.addItem("")
        self.esh.addItem("")
        self.esh.addItem("")
        self.esh.addItem("")
        self.esh.addItem("")
        self.esh.addItem("")
        self.verticalLayout_22.addWidget(self.esh)
        self.horizontalLayout_10.addLayout(self.verticalLayout_22)
        self.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_41 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_41.setFont(font)
        self.label_41.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_23.addWidget(self.label_41)
        self.mid_esh = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mid_esh.setFont(font)
        self.mid_esh.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.mid_esh.setObjectName("mid_esh")
        self.verticalLayout_23.addWidget(self.mid_esh)
        self.horizontalLayout_10.addLayout(self.verticalLayout_23)
        self.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.label_67 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_67.setFont(font)
        self.label_67.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_67.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_67.setObjectName("label_67")
        self.verticalLayout_24.addWidget(self.label_67)
        self.sig_esh = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sig_esh.setFont(font)
        self.sig_esh.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.sig_esh.setObjectName("sig_esh")
        self.verticalLayout_24.addWidget(self.sig_esh)
        self.horizontalLayout_10.addLayout(self.verticalLayout_24)
        self.verticalLayout_21.addLayout(self.horizontalLayout_10)
        self.verticalLayout_11.addLayout(self.verticalLayout_21)
        self.horizontalLayout_9.addLayout(self.verticalLayout_11)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.addButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.addButton.setFont(font)
        self.addButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.addButton.setObjectName("addButton")
        self.verticalLayout_2.addWidget(self.addButton)
        self.mplWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.mplWidget_3.setGeometry(QtCore.QRect(900, 570, 651, 401))
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mplWidget_3.setFont(font)
        self.mplWidget_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.mplWidget_3.setObjectName("mplWidget_3")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 639, 198))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_13.addWidget(self.label_9)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.poty = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.poty.setFont(font)
        self.poty.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.poty.setChecked(True)
        self.poty.setObjectName("poty")
        self.verticalLayout_12.addWidget(self.poty)
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_12.addWidget(self.radioButton_4)
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_12.addWidget(self.radioButton_2)
        self.zheskyi = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.zheskyi.setFont(font)
        self.zheskyi.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.zheskyi.setObjectName("zheskyi")
        self.verticalLayout_12.addWidget(self.zheskyi)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_2.addWidget(self.checkBox_3)
        self.checkBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox.setFont(font)
        self.checkBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.checkBox_4 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_2.addWidget(self.checkBox_4)
        self.verticalLayout_12.addLayout(self.horizontalLayout_2)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        self.horizontalLayout_5.addLayout(self.verticalLayout_13)
        self.verticalLayout_44 = QtWidgets.QVBoxLayout()
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.wels = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.wels.setFont(font)
        self.wels.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.wels.setMinimum(3)
        self.wels.setMaximum(10)
        self.wels.setProperty("value", 5)
        self.wels.setObjectName("wels")
        self.verticalLayout.addWidget(self.wels)
        self.verticalLayout_44.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.rows = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.rows.setFont(font)
        self.rows.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.rows.setMinimum(3)
        self.rows.setMaximum(5)
        self.rows.setObjectName("rows")
        self.verticalLayout_3.addWidget(self.rows)
        self.no_miss = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.no_miss.setFont(font)
        self.no_miss.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.no_miss.setObjectName("no_miss")
        self.verticalLayout_3.addWidget(self.no_miss)
        self.verticalLayout_44.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_44)
        self.montecarlo = QtWidgets.QLabel(self.centralwidget)
        self.montecarlo.setGeometry(QtCore.QRect(20, 950, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.montecarlo.setFont(font)
        self.montecarlo.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.montecarlo.setText("")
        self.montecarlo.setObjectName("montecarlo")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(900, 500, 791, 72))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.dumai = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(12)
        self.dumai.setFont(font)
        self.dumai.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dumai.setObjectName("dumai")
        self.verticalLayout_4.addWidget(self.dumai)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.inskv.setCurrentIndex(15)
        self.vrub.setCurrentIndex(3)
        self.esh.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ininsk.setText(_translate("MainWindow", "Учесть внутрискважинное замедление"))
        self.label_3.setText(_translate("MainWindow", "Внутрискважинное замедление"))
        self.label_16.setText(_translate("MainWindow", "Выбор \n"
"замедления"))
        self.inskv.setCurrentText(_translate("MainWindow", "500"))
        self.inskv.setItemText(0, _translate("MainWindow", "0"))
        self.inskv.setItemText(1, _translate("MainWindow", "25"))
        self.inskv.setItemText(2, _translate("MainWindow", "50"))
        self.inskv.setItemText(3, _translate("MainWindow", "75"))
        self.inskv.setItemText(4, _translate("MainWindow", "100"))
        self.inskv.setItemText(5, _translate("MainWindow", "125"))
        self.inskv.setItemText(6, _translate("MainWindow", "150"))
        self.inskv.setItemText(7, _translate("MainWindow", "175"))
        self.inskv.setItemText(8, _translate("MainWindow", "200"))
        self.inskv.setItemText(9, _translate("MainWindow", "225"))
        self.inskv.setItemText(10, _translate("MainWindow", "250"))
        self.inskv.setItemText(11, _translate("MainWindow", "300"))
        self.inskv.setItemText(12, _translate("MainWindow", "350"))
        self.inskv.setItemText(13, _translate("MainWindow", "400"))
        self.inskv.setItemText(14, _translate("MainWindow", "450"))
        self.inskv.setItemText(15, _translate("MainWindow", "500"))
        self.inskv.setItemText(16, _translate("MainWindow", "750"))
        self.inskv.setItemText(17, _translate("MainWindow", "1000"))
        self.label_35.setText(_translate("MainWindow", "Среднее \n"
"значение"))
        self.mid_in.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "Среднеквадратичное \n"
"отклонение"))
        self.sig_in.setText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "Замедление во врубовом ряду"))
        self.label_18.setText(_translate("MainWindow", "Выбор\n"
"замедления"))
        self.vrub.setItemText(0, _translate("MainWindow", "0"))
        self.vrub.setItemText(1, _translate("MainWindow", "17"))
        self.vrub.setItemText(2, _translate("MainWindow", "25"))
        self.vrub.setItemText(3, _translate("MainWindow", "42"))
        self.vrub.setItemText(4, _translate("MainWindow", "67"))
        self.vrub.setItemText(5, _translate("MainWindow", "109"))
        self.vrub.setItemText(6, _translate("MainWindow", "176"))
        self.label_21.setText(_translate("MainWindow", "Среднее \n"
"значение"))
        self.mid_vr.setText(_translate("MainWindow", "0"))
        self.label_65.setText(_translate("MainWindow", "Среднеквадратичное \n"
"отклонение"))
        self.sig_vr.setText(_translate("MainWindow", "0"))
        self.label_40.setText(_translate("MainWindow", "Замедление в эшелоне"))
        self.label_23.setText(_translate("MainWindow", "Выбор \n"
"замедления"))
        self.esh.setItemText(0, _translate("MainWindow", "0"))
        self.esh.setItemText(1, _translate("MainWindow", "17"))
        self.esh.setItemText(2, _translate("MainWindow", "25"))
        self.esh.setItemText(3, _translate("MainWindow", "42"))
        self.esh.setItemText(4, _translate("MainWindow", "67"))
        self.esh.setItemText(5, _translate("MainWindow", "109"))
        self.esh.setItemText(6, _translate("MainWindow", "176"))
        self.label_41.setText(_translate("MainWindow", "Среднее \n"
"значение"))
        self.mid_esh.setText(_translate("MainWindow", "0"))
        self.label_67.setText(_translate("MainWindow", "Среднеквадратичное \n"
"отклонение"))
        self.sig_esh.setText(_translate("MainWindow", "0"))
        self.addButton.setText(_translate("MainWindow", "Построить"))
        self.label_9.setText(_translate("MainWindow", "Выбор статистических данных"))
        self.poty.setText(_translate("MainWindow", "По ТУ"))
        self.radioButton_4.setText(_translate("MainWindow", "По данным В.А. Белина"))
        self.radioButton_2.setText(_translate("MainWindow", "По данным КузГТУ"))
        self.zheskyi.setText(_translate("MainWindow", "Ввести свои значения замедления и отклонений"))
        self.checkBox_3.setText(_translate("MainWindow", "Учет времени \n"
"хранения"))
        self.checkBox.setText(_translate("MainWindow", "Учет температуры"))
        self.checkBox_4.setText(_translate("MainWindow", "Отклонение в минус\n"
" от номинала"))
        self.label_7.setText(_translate("MainWindow", "Число скважин в ряду"))
        self.label_6.setText(_translate("MainWindow", "Рядов скважин"))
        self.no_miss.setText(_translate("MainWindow", "Без учета ошибки"))
        self.label_10.setText(_translate("MainWindow", "Разница во времени срабатывания между соседними соединенным скважинами\n"
" по поперечной схеме инициирования (врубовый ряд сверху)"))
        self.dumai.setText(_translate("MainWindow", "проверка на частоту неправильной отработки (на 100 случаев)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())