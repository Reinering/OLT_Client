# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\git\OLT_Client\testWindows.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setGeometry(QtCore.QRect(180, 120, 351, 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 349, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(10, 0, 329, 391))
        self.widget.setObjectName("widget")
        self.verticalLayout_onu = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_onu.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_onu.setObjectName("verticalLayout_onu")
        self.horizontalLayout_onu_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_onu_1.setObjectName("horizontalLayout_onu_1")
        self.label_onu_1 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_onu_1.setFont(font)
        self.label_onu_1.setObjectName("label_onu_1")
        self.horizontalLayout_onu_1.addWidget(self.label_onu_1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_onu_1.addItem(spacerItem)
        self.checkBox_onu_1 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_onu_1.setText("")
        self.checkBox_onu_1.setObjectName("checkBox_onu_1")
        self.horizontalLayout_onu_1.addWidget(self.checkBox_onu_1)
        self.verticalLayout_onu.addLayout(self.horizontalLayout_onu_1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_onu.addItem(spacerItem1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_onu_1.setText(_translate("MainWindow", "QQQQQQQQQQQQQQQQQQQQ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

