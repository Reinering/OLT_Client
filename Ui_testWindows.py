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
        MainWindow.resize(386, 425)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralWidget)
        self.scrollArea.setGeometry(QtCore.QRect(9, 9, 364, 401))
        self.scrollArea.setMinimumSize(QtCore.QSize(351, 401))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 345, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(220, 100, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textEdit.setGeometry(QtCore.QRect(80, 190, 211, 331))
        self.textEdit.setObjectName("textEdit")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        aux = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        aux.setFixedSize(10,10)
        aux.setStyleSheet("""background: red;""")

        aux2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        aux2.setFixedSize(20, 20)
        aux2.setStyleSheet("""background: blue;""")

        aux3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        aux3.setFixedSize(15, 15)
        aux3.setStyleSheet("""background: yellow;""")

        aux4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        aux4.setFixedSize(50,50)
        aux4.setStyleSheet("""background: rgb(0,255,0,30%);""")

        aux5 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        aux5.setFixedSize(40, 40)
        aux5.setStyleSheet("""background: green;""")

        aux6 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        aux6.setFixedSize(40, 40)
        aux6.setStyleSheet("""background: green;""")
        
        self.v_layout_container = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.v_layout_container.setSpacing(100)
        self.v_layout_container.addWidget(aux)
        self.v_layout_container.addWidget(aux2)
        self.v_layout_container.addWidget(aux3)
        self.v_layout_container.addWidget(aux4)
        self.v_layout_container.addWidget(aux5)
        self.v_layout_container.addWidget(aux6)



        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

