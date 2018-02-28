# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5 import QtWidgets, QtGui,  QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_OLTv1_1 import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.on_pushButton_service_num = 2
        self._translate = QtCore.QCoreApplication.translate
        #serviceport_namestr = ("horizontalLayout_service_", "pushButton_sub_",  "comboBox_service_",  "comboBox_servicevlanmode_",  "lineEdit_svlan_",  "lineEdit_cvlan_",  "comboBox_uservlanmode_",  "lineEdit_usevlan_")
        self.horizontalLayout_service = []
        self.pushButton_sub = []
        self.label_service = []
        self.comboBox_service = []
        self.label_servicevlanmode = []
        self.comboBox_servicevlanmode = []
        self.label_svlan = []
        self.lineEdit_svlan = []
        self.label_cvlan = []
        self.lineEdit_cvlan = []
        self.label_uservlanmode = [] 
        self.comboBox_uservlanmode = []
        self.label_uservlan = []
        self.lineEdit_usevlan = []
        self.horizontalLayout_count = 1

    def on_pushButton_sub_clicked(self, n):
        print(n)

        # self.verticalLayout_service_1.removeWidget(self.horizontalLayout_service[n])
        # QtWidgets.QWidget.destroyed(self.horizontalLayout_service[n])
        self.verticalLayout_service_1.findChild(QtWidgets.QHBoxLayout, "horizontalLayout_service_" +str(n) )  #查找child
        if self.horizontalLayout_count > 1:
            self.horizontalLayout_count -= 1
        print("on_pushButton_del_num: ", self.horizontalLayout_count)

    @pyqtSlot()
    def on_pushButton_add_1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        
        print("on_pushButton_add_1_clicked")
        print("on_pushButton_add_num: ", self.horizontalLayout_count)


        n = self.on_pushButton_service_num - 2
        i = self.on_pushButton_service_num
        if 1 <= self.horizontalLayout_count and self.horizontalLayout_count <= 7 :
            #createVar[serviceport_namestr[n + i]] = QtWidgets.QHBoxLayout()
            #创建ServicePort水平布局
            print(len(self.horizontalLayout_service))
            self.horizontalLayout_service.append(QtWidgets.QHBoxLayout())
            
            self.horizontalLayout_service[n].setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
            self.horizontalLayout_service[n].setObjectName("horizontalLayout_service_" + str(i))
            #ServicePort水平布局中添加“删除按钮”
            self.pushButton_sub.append(QtWidgets.QPushButton(self.centralWidget))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.pushButton_sub[n].sizePolicy().hasHeightForWidth())
            self.pushButton_sub[n].setSizePolicy(sizePolicy)
            self.pushButton_sub[n].setMaximumSize(QtCore.QSize(24, 24))
            self.pushButton_sub[n].setSizePolicy(sizePolicy)
            self.pushButton_sub[n].setMaximumSize(QtCore.QSize(24, 24))
            font = QtGui.QFont()
            font.setPointSize (10)
            self.pushButton_sub[n].setFont(font)
            self.pushButton_sub[n].setObjectName("pushButton_sub_" + str(i))
            self.horizontalLayout_service[n].addWidget(self.pushButton_sub[n])
            self.pushButton_sub[n].setText(self._translate("MainWindow", "-"))
            #添加手动信号
            self.pushButton_sub[n].clicked.connect(lambda: self.on_pushButton_sub_clicked(n))
            #ServicePort水平布局中添加“业务类型”
            self.label_service.append(QtWidgets.QLabel(self.centralWidget))
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            self.label_service[n].setFont(font)
            self.label_service[n].setObjectName("label_service_" + str(i))
            self.label_service[n].setText(self._translate("MainWindow", "业务类型"))
            self.horizontalLayout_service[n].addWidget(self.label_service[n])
            #ServicePort水平布局中添加“业务类型”下拉菜单
            self.comboBox_service.append(QtWidgets.QComboBox(self.centralWidget))
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            self.comboBox_service[n].setFont(font)
            self.comboBox_service[n].setObjectName("comboBox_service_" + str(i))
            self.comboBox_service[n].addItem("")
            self.comboBox_service[n].addItem("")
            self.comboBox_service[n].addItem("")
            self.comboBox_service[n].addItem("")
            self.comboBox_service[n].setItemText(0, self._translate("MainWindow", "Internet"))
            self.comboBox_service[n].setItemText(1, self._translate("MainWindow", "IPTV"))
            self.comboBox_service[n].setItemText(2, self._translate("MainWindow", "VOIP"))
            self.comboBox_service[n].setItemText(3, self._translate("MainWindow", "TR069"))
            self.horizontalLayout_service[n].addWidget(self.comboBox_service[n])
            #ServicePort水平布局中添加“业务VLAN模式”
            self.label_servicevlanmode.append(QtWidgets.QLabel(self.centralWidget))
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            self.label_servicevlanmode[n].setFont(font)
            self.label_servicevlanmode[n].setObjectName("label_servicevlanmode_" + str(i))
            self.label_servicevlanmode[n].setText(self._translate("MainWindow", "业务VLAN模式"))
            self.horizontalLayout_service[n].addWidget(self.label_servicevlanmode[n])
            #ServicePort水平布局中添加“业务VLAN模式”下拉菜单
            self.comboBox_servicevlanmode.append(QtWidgets.QComboBox(self.centralWidget))
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            self.comboBox_servicevlanmode[n].setFont(font)
            self.comboBox_servicevlanmode[n].setObjectName("comboBox_servicevlanmode_" + str(i))
            self.comboBox_servicevlanmode[n].addItem("")
            self.comboBox_servicevlanmode[n].addItem("")
            self.comboBox_servicevlanmode[n].addItem("")
            self.comboBox_servicevlanmode[n].setItemText(0, self._translate("MainWindow", "Statcked"))
            self.comboBox_servicevlanmode[n].setItemText(1, self._translate("MainWindow", "Tag"))
            self.comboBox_servicevlanmode[n].setItemText(2, self._translate("MainWindow", "Untag"))
            self.horizontalLayout_service[n].addWidget(self.comboBox_servicevlanmode[n])
            #ServicePort水平布局中添加“SVLAN”
            self.label_svlan.append(QtWidgets.QLabel(self.centralWidget))
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            self.label_svlan[n].setFont(font)
            self.label_svlan[n].setObjectName("label_svlan_" + str(i))
            self.label_svlan[n].setText(self._translate("MainWindow", "SVLAN"))
            self.horizontalLayout_service[n].addWidget(self.label_svlan[n])
            #ServicePort水平布局中添加“SVLAN”文本框
            self.lineEdit_svlan.append(QtWidgets.QLineEdit(self.centralWidget))
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            self.lineEdit_svlan[n].setFont(font)
            self.lineEdit_svlan[n].setObjectName("lineEdit_svlan_" + str(i))
            self.horizontalLayout_service[n].addWidget(self.lineEdit_svlan[n])
            #ServicePort水平布局中添加“CVLAN”
            self.label_cvlan.append(QtWidgets.QLabel(self.centralWidget))
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            self.label_cvlan[n].setFont(font)
            self.label_cvlan[n].setObjectName("label_cvlan_" + str(i))
            self.label_cvlan[n].setText(self._translate("MainWindow", "CVLAN"))
            self.horizontalLayout_service[n].addWidget(self.label_cvlan[n])
            #ServicePort水平布局中添加“CVLAN”文本框
            self.lineEdit_cvlan.append(QtWidgets.QLineEdit(self.centralWidget))
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            self.lineEdit_cvlan[n].setFont(font)
            self.lineEdit_cvlan[n].setObjectName("lineEdit_cvlan_" + str(i))
            self.horizontalLayout_service[n].addWidget(self.lineEdit_cvlan[n])
            #ServicePort水平布局中添加“用户VLAN模式”
            self.label_uservlanmode.append(QtWidgets.QLabel(self.centralWidget))
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            self.label_uservlanmode[n].setFont(font)
            self.label_uservlanmode[n].setObjectName("label_uservlanmode_" + str(i))
            self.label_uservlanmode[n].setText(self._translate("MainWindow", "用户VLAN模式"))
            self.horizontalLayout_service[n].addWidget(self.label_uservlanmode[n])
            #ServicePort水平布局中添加“用户VLAN模式”下拉菜单
            self.comboBox_uservlanmode.append(QtWidgets.QComboBox(self.centralWidget))
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            self.comboBox_uservlanmode[n].setFont(font)
            self.comboBox_uservlanmode[n].setObjectName("comboBox_uservlanmode_" + str(i))
            self.comboBox_uservlanmode[n].addItem("")
            self.comboBox_uservlanmode[n].addItem("")
            self.comboBox_uservlanmode[n].addItem("")
            self.comboBox_uservlanmode[n].addItem("")
            self.comboBox_uservlanmode[n].setItemText(0, self._translate("MainWindow", "Transparent"))
            self.comboBox_uservlanmode[n].setItemText(1, self._translate("MainWindow", "Translate"))
            self.comboBox_uservlanmode[n].setItemText(2, self._translate("MainWindow", "Default"))
            self.comboBox_uservlanmode[n].setItemText(3, self._translate("MainWindow", "Untag"))
            self.horizontalLayout_service[n].addWidget(self.comboBox_uservlanmode[n])
            #ServicePort水平布局中添加“用户VLAN”
            self.label_uservlan.append(QtWidgets.QLabel(self.centralWidget))
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            self.label_uservlan[n].setFont(font)
            self.label_uservlan[n].setObjectName("label_uservlan_" + str(i))
            self.label_uservlan[n].setText(self._translate("MainWindow", "用户VLAN"))
            self.horizontalLayout_service[n].addWidget(self.label_uservlan[n])
            #ServicePort水平布局中添加“用户VLAN”文本框
            self.lineEdit_usevlan.append(QtWidgets.QLineEdit(self.centralWidget))
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            self.lineEdit_usevlan[n].setFont(font)
            self.lineEdit_usevlan[n].setObjectName("lineEdit_usevlan_" + str(i))
            self.horizontalLayout_service[n].addWidget(self.lineEdit_usevlan[n])
            #"业务配置”垂直布局中新建的ServicePort水平布局
            self.verticalLayout_service_1.addLayout(self.horizontalLayout_service[n])
            self.horizontalLayout_count += 1
            self.on_pushButton_service_num += 1






        

import sys
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())

    
