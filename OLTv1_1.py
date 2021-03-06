# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5 import QtWidgets, QtGui,  QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_OLTv1_1 import Ui_MainWindow
import OLT


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
        self._translate = QtCore.QCoreApplication.translate
        self.on_pushButton_service_num = 2
        self.horizontalLayout_count = 1
        self.oltInst = OLT.OLT()


    #删除业务控件
    def on_pushButton_sub_clicked(self, horizontalLayout_service):
        # print(horizontalLayout_service)   此数组删除控件后已废弃
        if self.horizontalLayout_count > 1:
            #删除horizontalLayout_service及内部所有控件
            try:
                horizontalLayout_service[1].setParent(None)
                horizontalLayout_service[2].setParent(None)
                horizontalLayout_service[3].setParent(None)
                horizontalLayout_service[4].setParent(None)
                horizontalLayout_service[5].setParent(None)
                horizontalLayout_service[6].setParent(None)
                horizontalLayout_service[7].setParent(None)
                horizontalLayout_service[8].setParent(None)
                horizontalLayout_service[9].setParent(None)
                horizontalLayout_service[10].setParent(None)
                horizontalLayout_service[11].setParent(None)
                horizontalLayout_service[12].setParent(None)
                horizontalLayout_service[13].setParent(None)

                horizontalLayout_service[0].setParent(None)
                self.verticalLayout_service_1.removeItem(horizontalLayout_service[0])
                self.horizontalLayout_count -= 1
            except Exception as e:
                print(e)
                print("删除业务配置\"horizontalLayout_service\"失败")

        print(horizontalLayout_service)

    #添加业务控件
    @pyqtSlot()
    def on_pushButton_add_1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        
        print("on_pushButton_add_1_clicked")
        print("on_pushButton_add_num: ", self.horizontalLayout_count)
        horizontalLayout_service = []
        i = self.on_pushButton_service_num
        if 1 <= self.horizontalLayout_count and self.horizontalLayout_count <= 7 :
            #创建ServicePort水平布局
            _horizontalLayout_service = QtWidgets.QHBoxLayout()
            horizontalLayout_service.append(_horizontalLayout_service)
            _horizontalLayout_service.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
            _horizontalLayout_service.setObjectName("horizontalLayout_service_" + str(i))
            #ServicePort水平布局中添加“删除按钮”
            _pushButton_sub = QtWidgets.QPushButton(self.centralWidget)
            horizontalLayout_service.append(_pushButton_sub)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(_pushButton_sub.sizePolicy().hasHeightForWidth())
            _pushButton_sub.setSizePolicy(sizePolicy)
            _pushButton_sub.setMaximumSize(QtCore.QSize(24, 24))
            _pushButton_sub.setSizePolicy(sizePolicy)
            _pushButton_sub.setMaximumSize(QtCore.QSize(24, 24))
            font = QtGui.QFont()
            font.setPointSize (10)
            _pushButton_sub.setFont(font)
            _pushButton_sub.setObjectName("pushButton_sub_" + str(i))
            _horizontalLayout_service.addWidget(_pushButton_sub)
            _pushButton_sub.setText(self._translate("MainWindow", "-"))
            #添加手动信号
            _pushButton_sub.clicked.connect(lambda: self.on_pushButton_sub_clicked(horizontalLayout_service))
            #ServicePort水平布局中添加“业务类型”
            _label_service = QtWidgets.QLabel(self.centralWidget)
            horizontalLayout_service.append(_label_service)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _label_service.setFont(font)
            _label_service.setObjectName("label_service_" + str(i))
            _label_service.setText(self._translate("MainWindow", "业务类型"))
            _horizontalLayout_service.addWidget(_label_service)
            #ServicePort水平布局中添加“业务类型”下拉菜单
            _comboBox_service = QtWidgets.QComboBox(self.centralWidget)
            horizontalLayout_service.append(_comboBox_service)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _comboBox_service.setFont(font)
            _comboBox_service.setObjectName("comboBox_service_" + str(i))
            _comboBox_service.addItem("")
            _comboBox_service.addItem("")
            _comboBox_service.addItem("")
            _comboBox_service.addItem("")
            _comboBox_service.setItemText(0, self._translate("MainWindow", "Internet"))
            _comboBox_service.setItemText(1, self._translate("MainWindow", "IPTV"))
            _comboBox_service.setItemText(2, self._translate("MainWindow", "VOIP"))
            _comboBox_service.setItemText(3, self._translate("MainWindow", "TR069"))
            _horizontalLayout_service.addWidget(_comboBox_service)
            #ServicePort水平布局中添加“业务VLAN模式”
            _label_servicevlanmode = QtWidgets.QLabel(self.centralWidget)
            horizontalLayout_service.append(_label_servicevlanmode)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _label_servicevlanmode.setFont(font)
            _label_servicevlanmode.setObjectName("label_servicevlanmode_" + str(i))
            _label_servicevlanmode.setText(self._translate("MainWindow", "业务VLAN模式"))
            _horizontalLayout_service.addWidget(_label_servicevlanmode)
            #ServicePort水平布局中添加“业务VLAN模式”下拉菜单
            _comboBox_servicevlanmode = QtWidgets.QComboBox(self.centralWidget)
            horizontalLayout_service.append(_comboBox_servicevlanmode)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _comboBox_servicevlanmode.setFont(font)
            _comboBox_servicevlanmode.setObjectName("comboBox_servicevlanmode_" + str(i))
            _comboBox_servicevlanmode.addItem("")
            _comboBox_servicevlanmode.addItem("")
            _comboBox_servicevlanmode.addItem("")
            _comboBox_servicevlanmode.setItemText(0, self._translate("MainWindow", "Statcked"))
            _comboBox_servicevlanmode.setItemText(1, self._translate("MainWindow", "Tag"))
            _comboBox_servicevlanmode.setItemText(2, self._translate("MainWindow", "Untag"))
            _horizontalLayout_service.addWidget(_comboBox_servicevlanmode)
            #ServicePort水平布局中添加“SVLAN”
            _label_svlan = QtWidgets.QLabel(self.centralWidget)
            horizontalLayout_service.append(_label_svlan)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _label_svlan.setFont(font)
            _label_svlan.setObjectName("label_svlan_" + str(i))
            _label_svlan.setText(self._translate("MainWindow", "SVLAN"))
            _horizontalLayout_service.addWidget(_label_svlan)
            #ServicePort水平布局中添加“SVLAN”文本框
            _lineEdit_svlan = QtWidgets.QLineEdit(self.centralWidget)
            horizontalLayout_service.append(_lineEdit_svlan)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _lineEdit_svlan.setObjectName("lineEdit_svlan_" + str(i))
            _horizontalLayout_service.addWidget(_lineEdit_svlan)
            #ServicePort水平布局中添加“CVLAN”
            _label_cvlan = QtWidgets.QLabel(self.centralWidget)
            horizontalLayout_service.append(_label_cvlan)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _label_cvlan.setFont(font)
            _label_cvlan.setObjectName("label_cvlan_" + str(i))
            _label_cvlan.setText(self._translate("MainWindow", "CVLAN"))
            _horizontalLayout_service.addWidget(_label_cvlan)
            #ServicePort水平布局中添加“CVLAN”文本框
            _lineEdit_cvlan = QtWidgets.QLineEdit(self.centralWidget)
            horizontalLayout_service.append(_lineEdit_cvlan)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _lineEdit_cvlan.setFont(font)
            _lineEdit_cvlan.setObjectName("lineEdit_cvlan_" + str(i))
            _horizontalLayout_service.addWidget(_lineEdit_cvlan)
            #ServicePort水平布局中添加“用户VLAN模式”
            _label_uservlanmode = QtWidgets.QLabel(self.centralWidget)
            horizontalLayout_service.append(_label_uservlanmode)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _label_uservlanmode.setFont(font)
            _label_uservlanmode.setObjectName("label_uservlanmode_" + str(i))
            _label_uservlanmode.setText(self._translate("MainWindow", "用户VLAN模式"))
            _horizontalLayout_service.addWidget(_label_uservlanmode)
            #ServicePort水平布局中添加“用户VLAN模式”下拉菜单
            _comboBox_uservlanmode = QtWidgets.QComboBox(self.centralWidget)
            horizontalLayout_service.append(_comboBox_uservlanmode)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _comboBox_uservlanmode.setFont(font)
            _comboBox_uservlanmode.setObjectName("comboBox_uservlanmode_" + str(i))
            _comboBox_uservlanmode.addItem("")
            _comboBox_uservlanmode.addItem("")
            _comboBox_uservlanmode.addItem("")
            _comboBox_uservlanmode.addItem("")
            _comboBox_uservlanmode.setItemText(0, self._translate("MainWindow", "Transparent"))
            _comboBox_uservlanmode.setItemText(1, self._translate("MainWindow", "Translate"))
            _comboBox_uservlanmode.setItemText(2, self._translate("MainWindow", "Default"))
            _comboBox_uservlanmode.setItemText(3, self._translate("MainWindow", "Untag"))
            _horizontalLayout_service.addWidget(_comboBox_uservlanmode)
            #ServicePort水平布局中添加“用户VLAN”
            _label_uservlan = QtWidgets.QLabel(self.centralWidget)
            horizontalLayout_service.append(_label_uservlan)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _label_uservlan.setFont(font)
            _label_uservlan.setObjectName("label_uservlan_" + str(i))
            _label_uservlan.setText(self._translate("MainWindow", "用户VLAN"))
            _horizontalLayout_service.addWidget(_label_uservlan)
            #ServicePort水平布局中添加“用户VLAN”文本框
            _lineEdit_usevlan = QtWidgets.QLineEdit(self.centralWidget)
            horizontalLayout_service.append(_lineEdit_usevlan)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _lineEdit_usevlan.setFont(font)
            _lineEdit_usevlan.setObjectName("lineEdit_usevlan_" + str(i))
            _horizontalLayout_service.addWidget(_lineEdit_usevlan)
            #"业务配置”垂直布局中新建的ServicePort水平布局
            self.verticalLayout_service_1.addLayout(_horizontalLayout_service)
            self.horizontalLayout_count += 1
            self.on_pushButton_service_num += 1

    #点击登录OLT按钮
    @pyqtSlot()
    def on_pushButton_login_clicked(self):
        print("登录OLT")
        self.oltInst.loginOLT(self.comboBox_OLTFactory.currentText(),
                      self.comboBox_OLTType.currentText(),
                      self.comboBox_loginMethod.currentText(),
                      self.lineEdit_IPAddr.text())

    #点击退出OLT按钮
    @pyqtSlot()
    def on_pushButton_exit_clicked(self):
        self.oltInst.exitOLT()

    #点击查询ONU按钮
    @pyqtSlot()
    def on_pushButton_query_clicked(self):
        self.oltInst.queryONU()

    #点击ONU注册按钮
    @pyqtSlot()
    def on_pushButton_reg_clicked(self):
        self.oltInst.regONU()

    #点击ONU去注册按钮
    @pyqtSlot()
    def on_pushButton_unreg_clicked(self):
        self.oltInst.unRegONU()


import sys
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
    

