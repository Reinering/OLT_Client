# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\git\OLT_Client\OLTv1_2.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1544, 631)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.comboBox_OLTFactory = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_OLTFactory.setFont(font)
        self.comboBox_OLTFactory.setObjectName("comboBox_OLTFactory")
        self.comboBox_OLTFactory.addItem("")
        self.comboBox_OLTFactory.setItemText(0, "")
        self.comboBox_OLTFactory.addItem("")
        self.comboBox_OLTFactory.addItem("")
        self.comboBox_OLTFactory.addItem("")
        self.comboBox_OLTFactory.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_OLTFactory)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_IPAddr = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_IPAddr.setFont(font)
        self.lineEdit_IPAddr.setText("")
        self.lineEdit_IPAddr.setObjectName("lineEdit_IPAddr")
        self.horizontalLayout_4.addWidget(self.lineEdit_IPAddr)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.lineEdit_oltUser = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_oltUser.setMinimumSize(QtCore.QSize(0, 27))
        self.lineEdit_oltUser.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_oltUser.setObjectName("lineEdit_oltUser")
        self.horizontalLayout.addWidget(self.lineEdit_oltUser)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_10.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_OLTType = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_OLTType.setFont(font)
        self.comboBox_OLTType.setObjectName("comboBox_OLTType")
        self.comboBox_OLTType.addItem("")
        self.comboBox_OLTType.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_OLTType)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.comboBox_loginMethod = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_loginMethod.setFont(font)
        self.comboBox_loginMethod.setObjectName("comboBox_loginMethod")
        self.comboBox_loginMethod.addItem("")
        self.comboBox_loginMethod.addItem("")
        self.comboBox_loginMethod.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_loginMethod)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.lineEdit_oltPasswd = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_oltPasswd.setMinimumSize(QtCore.QSize(0, 27))
        self.lineEdit_oltPasswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_oltPasswd.setObjectName("lineEdit_oltPasswd")
        self.horizontalLayout_9.addWidget(self.lineEdit_oltPasswd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.comboBox_7 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_7.setFont(font)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_7)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_3.addWidget(self.radioButton)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_5.addWidget(self.radioButton_2)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(207, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addWidget(self.groupBox)


        self.scrollArea = QtWidgets.QScrollArea(self.layoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 418, 379))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5.addWidget(self.scrollArea)
        self.widget_onu = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_onu.setGeometry(QtCore.QRect(10, 0, 398, 371))
        self.widget_onu.setObjectName("widget_onu")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_onu = QtWidgets.QVBoxLayout(self.widget_onu)
        self.verticalLayout_onu.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_onu.setObjectName("verticalLayout_onu")


        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_login = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setObjectName("pushButton_login")
        self.verticalLayout_4.addWidget(self.pushButton_login)
        self.pushButton_exit = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.verticalLayout_4.addWidget(self.pushButton_exit)
        self.pushButton_query = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_query.setFont(font)
        self.pushButton_query.setObjectName("pushButton_query")
        self.verticalLayout_4.addWidget(self.pushButton_query)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_reg = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_reg.setFont(font)
        self.pushButton_reg.setObjectName("pushButton_reg")
        self.gridLayout.addWidget(self.pushButton_reg, 1, 0, 1, 1)
        self.pushButton_addService = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_addService.setFont(font)
        self.pushButton_addService.setObjectName("pushButton_addService")
        self.gridLayout.addWidget(self.pushButton_addService, 3, 0, 1, 1)
        self.pushButton_unreg = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_unreg.setFont(font)
        self.pushButton_unreg.setObjectName("pushButton_unreg")
        self.gridLayout.addWidget(self.pushButton_unreg, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 4, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_service_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_service_1.setObjectName("verticalLayout_service_1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_service_1.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_service_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_service_1.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_service_1.setObjectName("horizontalLayout_service_1")
        self.pushButton_add_1 = QtWidgets.QPushButton(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add_1.sizePolicy().hasHeightForWidth())
        self.pushButton_add_1.setSizePolicy(sizePolicy)
        self.pushButton_add_1.setMaximumSize(QtCore.QSize(24, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_add_1.setFont(font)
        self.pushButton_add_1.setObjectName("pushButton_add_1")
        self.horizontalLayout_service_1.addWidget(self.pushButton_add_1)
        self.label_service_1 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_service_1.setFont(font)
        self.label_service_1.setObjectName("label_service_1")
        self.horizontalLayout_service_1.addWidget(self.label_service_1)
        self.comboBox_service_1 = QtWidgets.QComboBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_service_1.setFont(font)
        self.comboBox_service_1.setObjectName("comboBox_service_1")
        self.comboBox_service_1.addItem("")
        self.comboBox_service_1.addItem("")
        self.comboBox_service_1.addItem("")
        self.comboBox_service_1.addItem("")
        self.horizontalLayout_service_1.addWidget(self.comboBox_service_1)
        self.label_servicevlanmode_1 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_servicevlanmode_1.setFont(font)
        self.label_servicevlanmode_1.setObjectName("label_servicevlanmode_1")
        self.horizontalLayout_service_1.addWidget(self.label_servicevlanmode_1)
        self.comboBox_servicevlanmode_1 = QtWidgets.QComboBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_servicevlanmode_1.setFont(font)
        self.comboBox_servicevlanmode_1.setObjectName("comboBox_servicevlanmode_1")
        self.comboBox_servicevlanmode_1.addItem("")
        self.comboBox_servicevlanmode_1.addItem("")
        self.comboBox_servicevlanmode_1.addItem("")
        self.horizontalLayout_service_1.addWidget(self.comboBox_servicevlanmode_1)
        self.label_svlan_1 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_svlan_1.setFont(font)
        self.label_svlan_1.setObjectName("label_svlan_1")
        self.horizontalLayout_service_1.addWidget(self.label_svlan_1)
        self.lineEdit_svlan_1 = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_svlan_1.setFont(font)
        self.lineEdit_svlan_1.setObjectName("lineEdit_svlan_1")
        self.horizontalLayout_service_1.addWidget(self.lineEdit_svlan_1)
        self.label_cvlan_1 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_cvlan_1.setFont(font)
        self.label_cvlan_1.setObjectName("label_cvlan_1")
        self.horizontalLayout_service_1.addWidget(self.label_cvlan_1)
        self.lineEdit_cvlan_1 = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_cvlan_1.setFont(font)
        self.lineEdit_cvlan_1.setObjectName("lineEdit_cvlan_1")
        self.horizontalLayout_service_1.addWidget(self.lineEdit_cvlan_1)
        self.label_uservlanmode_1 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_uservlanmode_1.setFont(font)
        self.label_uservlanmode_1.setObjectName("label_uservlanmode_1")
        self.horizontalLayout_service_1.addWidget(self.label_uservlanmode_1)
        self.comboBox_uservlanmode_1 = QtWidgets.QComboBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.comboBox_uservlanmode_1.setFont(font)
        self.comboBox_uservlanmode_1.setObjectName("comboBox_uservlanmode_1")
        self.comboBox_uservlanmode_1.addItem("")
        self.comboBox_uservlanmode_1.addItem("")
        self.comboBox_uservlanmode_1.addItem("")
        self.comboBox_uservlanmode_1.addItem("")
        self.horizontalLayout_service_1.addWidget(self.comboBox_uservlanmode_1)
        self.label_uservlan_1 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_uservlan_1.setFont(font)
        self.label_uservlan_1.setObjectName("label_uservlan_1")
        self.horizontalLayout_service_1.addWidget(self.label_uservlan_1)
        self.lineEdit_usevlan_1 = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.lineEdit_usevlan_1.setFont(font)
        self.lineEdit_usevlan_1.setObjectName("lineEdit_usevlan_1")
        self.horizontalLayout_service_1.addWidget(self.lineEdit_usevlan_1)
        self.verticalLayout_service_1.addLayout(self.horizontalLayout_service_1)
        self.verticalLayout_7.addLayout(self.verticalLayout_service_1)
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget2)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser.setMidLineWidth(0)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_7.addWidget(self.textBrowser)
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "OLT厂家"))
        self.comboBox_OLTFactory.setItemText(1, _translate("MainWindow", "FiberHome"))
        self.comboBox_OLTFactory.setItemText(2, _translate("MainWindow", "HuaWei"))
        self.comboBox_OLTFactory.setItemText(3, _translate("MainWindow", "ZTE"))
        self.comboBox_OLTFactory.setItemText(4, _translate("MainWindow", "Bell"))
        self.label_3.setText(_translate("MainWindow", "IP ADD "))
        self.label_8.setText(_translate("MainWindow", "用户名"))
        self.label_2.setText(_translate("MainWindow", "OLT类型"))
        self.comboBox_OLTType.setItemText(0, _translate("MainWindow", "GPON"))
        self.comboBox_OLTType.setItemText(1, _translate("MainWindow", "EPON"))
        self.label_4.setText(_translate("MainWindow", "登录方式"))
        self.comboBox_loginMethod.setItemText(0, _translate("MainWindow", "Telnet"))
        self.comboBox_loginMethod.setItemText(1, _translate("MainWindow", "SSH2"))
        self.comboBox_loginMethod.setItemText(2, _translate("MainWindow", "SSH"))
        self.label_9.setText(_translate("MainWindow", "登陆密码"))
        self.label_7.setText(_translate("MainWindow", "产品型号："))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "吉视汇通-2ETH"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "吉视汇通-4ETH"))
        self.radioButton.setText(_translate("MainWindow", "查看未注册设备"))
        self.radioButton_2.setText(_translate("MainWindow", "查看已注册设备"))
        self.label_5.setText(_translate("MainWindow", "MAC"))
        self.lineEdit_2.setText(_translate("MainWindow", "1111111111111111111111"))
        self.pushButton_login.setText(_translate("MainWindow", "LOGIN"))
        self.pushButton_exit.setText(_translate("MainWindow", "EXIT"))
        self.pushButton_query.setText(_translate("MainWindow", "查询"))
        self.pushButton_reg.setText(_translate("MainWindow", "注册"))
        self.pushButton_addService.setText(_translate("MainWindow", "添加业务"))
        self.pushButton_unreg.setText(_translate("MainWindow", "去注册"))
        self.label_6.setText(_translate("MainWindow", "业务配置"))
        self.pushButton_add_1.setText(_translate("MainWindow", "+"))
        self.label_service_1.setText(_translate("MainWindow", "业务类型"))
        self.comboBox_service_1.setItemText(0, _translate("MainWindow", "Internet"))
        self.comboBox_service_1.setItemText(1, _translate("MainWindow", "IPTV"))
        self.comboBox_service_1.setItemText(2, _translate("MainWindow", "VOIP"))
        self.comboBox_service_1.setItemText(3, _translate("MainWindow", "TR069"))
        self.label_servicevlanmode_1.setText(_translate("MainWindow", "业务VLAN模式"))
        self.comboBox_servicevlanmode_1.setItemText(0, _translate("MainWindow", "Statcked"))
        self.comboBox_servicevlanmode_1.setItemText(1, _translate("MainWindow", "Tag"))
        self.comboBox_servicevlanmode_1.setItemText(2, _translate("MainWindow", "Untag"))
        self.label_svlan_1.setText(_translate("MainWindow", "SVLAN"))
        self.lineEdit_svlan_1.setText(_translate("MainWindow", "4096"))
        self.label_cvlan_1.setText(_translate("MainWindow", "CVLAN"))
        self.lineEdit_cvlan_1.setText(_translate("MainWindow", "4096"))
        self.label_uservlanmode_1.setText(_translate("MainWindow", "用户VLAN模式"))
        self.comboBox_uservlanmode_1.setItemText(0, _translate("MainWindow", "Transparent"))
        self.comboBox_uservlanmode_1.setItemText(1, _translate("MainWindow", "Translate"))
        self.comboBox_uservlanmode_1.setItemText(2, _translate("MainWindow", "Default"))
        self.comboBox_uservlanmode_1.setItemText(3, _translate("MainWindow", "Untag"))
        self.label_uservlan_1.setText(_translate("MainWindow", "用户VLAN"))
        self.lineEdit_usevlan_1.setText(_translate("MainWindow", "4096"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

