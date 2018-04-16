# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5 import QtWidgets, QtGui,  QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from queue import Queue


from Ui_OLTv1_2 import Ui_MainWindow
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

        self.tableWidget_onu.setColumnWidth(0, 20)
        self.tableWidget_onu.setColumnWidth(1, 160)
        self.tableWidget_onu.setColumnWidth(2, 65)
        self.tableWidget_onu.setColumnWidth(3, 55)

        self.on_pushButton_service_num = 2
        self.horizontalLayout_count = 1
        self.logQueue = Queue()
        self.cmdQueue = Queue()
        self.resultQueue = Queue()
        self.login_tag = False
        self.onu_List = []


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
                self.verticalLayout_service.removeItem(horizontalLayout_service[0])
                self.horizontalLayout_count -= 1

                del horizontalLayout_service

                verticalLayoutWidget_height = self.verticalLayoutWidget.height()
                if verticalLayoutWidget_height > 41:
                    self.verticalLayoutWidget.setGeometry(0, 0, 1011, verticalLayoutWidget_height - 30)
                    scrollArea_service_MinSize = self.scrollArea_service.minimumSize()
                    self.scrollArea_service.setMinimumSize(QtCore.QSize(641, scrollArea_service_MinSize.height() - 30))
                    scrollArea_service_MaxSize = self.scrollArea_service.maximumSize()
                    self.scrollArea_service.setMaximumSize(QtCore.QSize(641, scrollArea_service_MaxSize.height() - 30))
                tbBar = self.scrollArea_service.verticalScrollBar()
                tbBar.setSliderPosition(tbBar.minimum())
            except Exception as e:
                print(e)
                print("删除业务配置\"horizontalLayout_service\"失败")

        # print(horizontalLayout_service)
    #添加业务控件
    @pyqtSlot()
    def on_pushButton_add_1_clicked(self):
        print("on_pushButton_add_1_clicked")
        print("on_pushButton_add_num: ", self.horizontalLayout_count)

        horizontalLayout_service = []
        i = self.on_pushButton_service_num
        if 1 <= self.horizontalLayout_count and self.horizontalLayout_count <= 7 :
            #调整scrollArea
            scrollArea_service_MinSize = self.scrollArea_service.minimumSize()
            self.scrollArea_service.setMinimumSize(QtCore.QSize(641, scrollArea_service_MinSize.height() + 30))
            scrollArea_service_MaxSize = self.scrollArea_service.maximumSize()
            self.scrollArea_service.setMaximumSize(QtCore.QSize(641, scrollArea_service_MaxSize.height() + 30))
            self.verticalLayoutWidget.setGeometry(0, 0, 1011, self.verticalLayoutWidget.height() + 30)
            #创建ServicePort水平布局
            _horizontalLayout_service = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
            horizontalLayout_service.append(_horizontalLayout_service)
            _horizontalLayout_service.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
            _horizontalLayout_service.setObjectName("horizontalLayout_service_" + str(i))
            #ServicePort水平布局中添加“删除按钮”
            _pushButton_sub = QtWidgets.QPushButton(self.verticalLayoutWidget)
            horizontalLayout_service.append(_pushButton_sub)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(_pushButton_sub.sizePolicy().hasHeightForWidth())
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
            _label_service = QtWidgets.QLabel(self.verticalLayoutWidget)
            horizontalLayout_service.append(_label_service)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _label_service.setFont(font)
            _label_service.setObjectName("label_service_" + str(i))
            _horizontalLayout_service.addWidget(_label_service)
            _label_service.setText(self._translate("MainWindow", "业务类型"))
            #ServicePort水平布局中添加“业务类型”下拉菜单
            _comboBox_service = QtWidgets.QComboBox(self.verticalLayoutWidget)
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
            _horizontalLayout_service.addWidget(_comboBox_service)
            _comboBox_service.setItemText(0, self._translate("MainWindow", "Internet"))
            _comboBox_service.setItemText(1, self._translate("MainWindow", "IPTV"))
            _comboBox_service.setItemText(2, self._translate("MainWindow", "VOIP"))
            _comboBox_service.setItemText(3, self._translate("MainWindow", "TR069"))
            #ServicePort水平布局中添加“业务VLAN模式”
            _label_servicevlanmode = QtWidgets.QLabel(self.verticalLayoutWidget)
            horizontalLayout_service.append(_label_servicevlanmode)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _label_servicevlanmode.setFont(font)
            _label_servicevlanmode.setObjectName("label_servicevlanmode_" + str(i))
            _horizontalLayout_service.addWidget(_label_servicevlanmode)
            _label_servicevlanmode.setText(self._translate("MainWindow", "业务VLAN模式"))
            #ServicePort水平布局中添加“业务VLAN模式”下拉菜单
            _comboBox_servicevlanmode = QtWidgets.QComboBox(self.verticalLayoutWidget)
            horizontalLayout_service.append(_comboBox_servicevlanmode)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _comboBox_servicevlanmode.setFont(font)
            _comboBox_servicevlanmode.setObjectName("comboBox_servicevlanmode_" + str(i))
            _comboBox_servicevlanmode.addItem("")
            _comboBox_servicevlanmode.addItem("")
            _comboBox_servicevlanmode.addItem("")
            _horizontalLayout_service.addWidget(_comboBox_servicevlanmode)
            _comboBox_servicevlanmode.setItemText(0, self._translate("MainWindow", "Statcked"))
            _comboBox_servicevlanmode.setItemText(1, self._translate("MainWindow", "Tag"))
            _comboBox_servicevlanmode.setItemText(2, self._translate("MainWindow", "Untag"))
            #ServicePort水平布局中添加“SVLAN”
            _label_svlan = QtWidgets.QLabel(self.verticalLayoutWidget)
            horizontalLayout_service.append(_label_svlan)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _label_svlan.setFont(font)
            _label_svlan.setObjectName("label_svlan_" + str(i))
            _horizontalLayout_service.addWidget(_label_svlan)
            _label_svlan.setText(self._translate("MainWindow", "SVLAN"))
            #ServicePort水平布局中添加“SVLAN”文本框
            _lineEdit_svlan = QtWidgets.QLineEdit(self.verticalLayoutWidget)
            horizontalLayout_service.append(_lineEdit_svlan)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _lineEdit_svlan.setFont(font)
            _lineEdit_svlan.setObjectName("lineEdit_svlan_" + str(i))
            _lineEdit_svlan.setMaximumSize(52, 27)
            _horizontalLayout_service.addWidget(_lineEdit_svlan)
            #ServicePort水平布局中添加“CVLAN”
            _label_cvlan = QtWidgets.QLabel(self.verticalLayoutWidget)
            horizontalLayout_service.append(_label_cvlan)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _label_cvlan.setFont(font)
            _label_cvlan.setObjectName("label_cvlan_" + str(i))
            _horizontalLayout_service.addWidget(_label_cvlan)
            _label_cvlan.setText(self._translate("MainWindow", "CVLAN"))
            #ServicePort水平布局中添加“CVLAN”文本框
            _lineEdit_cvlan = QtWidgets.QLineEdit(self.verticalLayoutWidget)
            horizontalLayout_service.append(_lineEdit_cvlan)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _lineEdit_cvlan.setFont(font)
            _lineEdit_cvlan.setObjectName("lineEdit_cvlan_" + str(i))
            _lineEdit_cvlan.setMaximumSize(52, 27)
            _horizontalLayout_service.addWidget(_lineEdit_cvlan)
            #ServicePort水平布局中添加“用户VLAN模式”
            _label_uservlanmode = QtWidgets.QLabel(self.verticalLayoutWidget)
            horizontalLayout_service.append(_label_uservlanmode)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _label_uservlanmode.setFont(font)
            _label_uservlanmode.setObjectName("label_uservlanmode_" + str(i))
            _horizontalLayout_service.addWidget(_label_uservlanmode)
            _label_uservlanmode.setText(self._translate("MainWindow", "用户VLAN模式"))
            #ServicePort水平布局中添加“用户VLAN模式”下拉菜单
            _comboBox_uservlanmode = QtWidgets.QComboBox(self.verticalLayoutWidget)
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
            _horizontalLayout_service.addWidget(_comboBox_uservlanmode)
            _comboBox_uservlanmode.setItemText(0, self._translate("MainWindow", "Transparent"))
            _comboBox_uservlanmode.setItemText(1, self._translate("MainWindow", "Translate"))
            _comboBox_uservlanmode.setItemText(2, self._translate("MainWindow", "Default"))
            _comboBox_uservlanmode.setItemText(3, self._translate("MainWindow", "Untag"))
            #ServicePort水平布局中添加“用户VLAN”
            _label_uservlan = QtWidgets.QLabel(self.verticalLayoutWidget)
            horizontalLayout_service.append(_label_uservlan)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _label_uservlan.setFont(font)
            _label_uservlan.setObjectName("label_uservlan_" + str(i))
            _label_uservlan.setText(self._translate("MainWindow", "用户VLAN"))
            _horizontalLayout_service.addWidget(_label_uservlan)
            #ServicePort水平布局中添加“用户VLAN”文本框
            _lineEdit_usevlan = QtWidgets.QLineEdit(self.verticalLayoutWidget)
            horizontalLayout_service.append(_lineEdit_usevlan)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(12)
            _lineEdit_usevlan.setFont(font)
            _lineEdit_usevlan.setObjectName("lineEdit_usevlan_" + str(i))
            _lineEdit_usevlan.setMaximumSize(52, 27)
            _horizontalLayout_service.addWidget(_lineEdit_usevlan)
            #"业务配置”垂直布局中新建的ServicePort水平布局
            self.verticalLayout_service.addLayout(_horizontalLayout_service)
            self.horizontalLayout_count += 1
            self.on_pushButton_service_num += 1

    #更改控件状态
    def modifyWidgetState(self, check):
        self.pushButton_login.setEnabled(check)
        self.comboBox_OLTFactory.setEnabled(check)
        self.comboBox_OLTType.setEnabled(check)
        self.comboBox_loginMethod.setEnabled(check)
        self.lineEdit_IPAddr.setEnabled(check)
        self.lineEdit_oltUser.setEnabled(check)
        self.lineEdit_oltPasswd.setEnabled(check)
        self.login_tag = not check

        self.pushButton_exit.setEnabled(not check)
        self.pushButton_query.setEnabled(not check)
        self.pushButton_reg.setEnabled(not check)
        self.pushButton_unreg.setEnabled(not check)
        self.pushButton_addService.setEnabled(not check)

    #改变OLT登录默认值
    @pyqtSlot(str)
    def on_comboBox_OLTFactory_currentTextChanged(self, p0):
        print(p0)
        if p0 == "FiberHome":
            self.lineEdit_IPAddr.setText("10.11.104.6")
            self.lineEdit_oltUser.setText("GEPON")
            self.lineEdit_oltPasswd.setText("GEPON")
        elif p0 == "HuaWei":
            self.lineEdit_IPAddr.setText("10.11.104.2")
            self.lineEdit_oltUser.setText("huawei")
            self.lineEdit_oltPasswd.setText("huawei28")
        elif p0 == "ZTE":
            self.lineEdit_IPAddr.setText("10.11.104.4")
            self.lineEdit_oltUser.setText("zte")
            self.lineEdit_oltPasswd.setText("zte")
        elif p0 == "Bell":
            self.lineEdit_IPAddr.setText("")
            self.lineEdit_oltUser.setText("")
            self.lineEdit_oltPasswd.setText("")
        elif p0 == "RHEL":
            self.lineEdit_IPAddr.setText("192.168.72.186")
            self.lineEdit_oltUser.setText("root")
            self.lineEdit_oltPasswd.setText("123456")
        else:
            self.lineEdit_IPAddr.setText("")
            self.lineEdit_oltUser.setText("")
            self.lineEdit_oltPasswd.setText("")

    #点击登录OLT按钮
    @pyqtSlot()
    def on_pushButton_login_clicked(self):
        self.modifyWidgetState(False)
        print("登录OLT")
        self.oltTh = oltThread(self.comboBox_OLTFactory.currentText(), self.comboBox_OLTType.currentText(),
                                      self.comboBox_loginMethod.currentText(), self.lineEdit_IPAddr.text(),
                                      self.lineEdit_oltUser.text(), self.lineEdit_oltPasswd.text(), self.logQueue, self.cmdQueue, self.resultQueue)
        self.oltTh.start()
        self.tbT = TBThread(self.textBrowser, self.logQueue)
        self.tbT.start()
        self.oltTh.sign_to_State.connect(self.modifyWidgetState)
        self.tbT.sign_timeout.connect(self.on_pushButton_exit_clicked)
        self.tbT.sign_displayOnu.connect(self.display_onu)

    #点击退出OLT按钮
    @pyqtSlot()
    def on_pushButton_exit_clicked(self):
        if self.login_tag:
            self.oltTh.stop()
            self.tbT.stop()
            self.modifyWidgetState(True)

    #点击查询ONU按钮
    @pyqtSlot()
    def on_pushButton_query_clicked(self):
        print("点击查询按钮")
        if not self.login_tag:
            self.logQueue.put("OLT未登录,请登录后再操作")
        elif (self.radioButton_unreg.isChecked()) and self.login_tag:
            #查询自动发现未注册的ONU
            self.cmdQueue.put("unregONU_query")
            self.cmdQueue.put(0)
        elif self.radioButton_reg.isChecked() and self.login_tag:
            # 查询已注册的ONU
            self.cmdQueue.put("regONU_query")
            self.cmdQueue.put(1)
            self.cmdQueue.put(self.lineEdit_SN.text())
        else:
            print("radioButton未选中")
            self.logQueue.put("请选择“查看未注册ONU”或“已注册ONU”")


    #点击ONU注册按钮
    @pyqtSlot()
    def on_pushButton_reg_clicked(self):
        if not self.login_tag:
            self.logQueue.put("OLT未登录,请登录后再操作")
        else:
            self.cmdQueue.put("ONUreg")
            self.cmdQueue.put(1)

    #点击ONU去注册按钮
    @pyqtSlot()
    def on_pushButton_unreg_clicked(self):
        if not self.login_tag:
            self.logQueue.put("OLT未登录,请登录后再操作")
        else:
            self.cmdQueue.put("ONUunreg")

    @pyqtSlot()
    def on_pushButton_addService_clicked(self):
        if not self.login_tag:
            self.logQueue.put("OLT未登录,请登录后再操作")
        else:
            self.cmdQueue.put("addService")

    #根据查询按钮显示ONU列表
    def display_onu(self, unregResult):
        print("unregResult", unregResult)
        onu_num = len(unregResult)
        rowCount = self.tableWidget_onu.rowCount()
        for i in range(rowCount-1, -1, -1):
            #清空表格
            self.tableWidget_onu.removeRow(i)
        #添加ONU列表
        self.tableWidget_onu.setRowCount(onu_num)
        for j in range(0, onu_num):
            # print("j:", j)
            temp = unregResult[j]
            k = 0
            _checkBox_onu = QtWidgets.QCheckBox()
            _checkBox_onu.setText("")
            _checkBox_onu.setChecked(False)
            _checkBox_onu.setObjectName("checkBox_onu_" + str(j + 1))
            self.tableWidget_onu.setCellWidget(j, k, _checkBox_onu)
            # _checkBox_onu.click(lambda: self.on_checkBox_sub_clicked(j+1))
            while k < len(temp):
                # print("k:", k)
                item = QtWidgets.QTableWidgetItem(temp[k])
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_onu.setItem(j, k + 1, item)
                k += 1
            temp.append(_checkBox_onu)
        self.onu_List = unregResult

    @pyqtSlot(bool)
    def on_radioButton_reg_clicked(self, checked):
        self.lineEdit_SN.setEnabled(checked)
    @pyqtSlot(bool)
    def on_radioButton_unreg_clicked(self, checked):
        self.lineEdit_SN.setEnabled(not checked)
        self.lineEdit_SN.clear()
    @pyqtSlot()
    def on_textBrowser_textChanged(self):
        self.textBrowser.moveCursor(QtGui.QTextCursor.End)
    # def on_checkBox_sub_clicked(self, num):
    #     print(num)

# 开启子线程
class oltThread(QtCore.QThread):
    sign_to_State = QtCore.pyqtSignal(bool)

    def __init__(self, olt_fact, olt_type, login_method, olt_ipaddr, olt_user, olt_passwd, logqueue, cmdqueue, resultqueue, parent=None):
        super(oltThread, self).__init__(parent)
        self.olt_fact = olt_fact
        self.olt_type = olt_type
        self.login_method = login_method
        self.olt_ipaddr = olt_ipaddr
        self.olt_user = olt_user
        self.olt_passwd = olt_passwd
        self.logQueue = logqueue
        self.cmdQueue = cmdqueue
        self.resultQueue = resultqueue
        self.oltInst = OLT.GEPON_OLT()
        self.stopBool = False



    def run(self):
        # olt_fact, olt_type, login_method, olt_ipaddr, olt_user, olt_passwd
        if self.olt_fact:
            if self.olt_fact == "FiberHome":
                self.oltInst = OLT.FH_OLT(self.olt_fact, self.olt_type, self.login_method, self.olt_ipaddr, self.olt_user, self.olt_passwd, self.logQueue)
            elif self.olt_fact == "ZTE":
                self.oltInst = OLT.ZTE_OLT(self.olt_fact, self.olt_type, self.login_method, self.olt_ipaddr, self.olt_user, self.olt_passwd, self.logQueue)
            elif self.olt_fact == "HuaWei" or self.olt_fact == "RHEL":
                self.oltInst = OLT.HW_OLT(self.olt_fact, self.olt_type, self.login_method, self.olt_ipaddr, self.olt_user, self.olt_passwd, self.logQueue)
            elif self.olt_fact == "Bell":
                pass
            else:
                print("OLT厂家获取错误")

            self.logQueue.put("开始登录OLT")
            if self.oltInst.loginOLT():
                if self.olt_fact == "HuaWei":
                    self.oltInst.consoleView("enable \r")
                while not self.stopBool:
                    cmd_prompt = self.cmdQueue.get()
                    if cmd_prompt == "unregONU_query":
                        print("unreg")
                        self.parseCmdQuue()
                        self.oltInst.query_unRegONU()
                    elif cmd_prompt == "regONU_query":
                        print("reg")
                        para_List = self.parseCmdQuue()
                        self.oltInst.query_regONU(para_List[0])
                    elif cmd_prompt == "ONUreg":
                        print("ONUreg")
                        para_List = self.parseCmdQuue()
                    elif cmd_prompt == "ONUunreg":
                        print("unONUreg")
                        para_List = self.parseCmdQuue()
                    elif cmd_prompt == "addService":
                        print("addService")
                        para_List = self.parseCmdQuue()
                    else:
                        print("获取到错误参数", cmd_prompt)
        else:
            self.logQueue.put("请选择OLT厂家")

        self.sign_to_State.emit(True)

    def stop(self):
        print("OLTThread线程停止")
        self.stopBool = True
        self.oltInst.exitOLT()
    def parseCmdQuue(self):
        # print(self.cmdQueue.get())
        # print(self.cmdQueue.get())
        para_list = []
        num = self.cmdQueue.get()
        count = 1
        while count <= num:
            para_list.append(self.cmdQueue.get())
            print(para_list[count-1])
            count += 1
        return para_list


# textBrowser 打印
class TBThread(QtCore.QThread):
    sign_timeout = QtCore.pyqtSignal(bool)
    sign_displayOnu = QtCore.pyqtSignal(list)
    def __init__(self, textBrowser, queue, parent=None):
        super(TBThread, self).__init__(parent)
        self.logQueue = queue
        self.textBrowser = ui.textBrowser
        self.tbThreadStop = False

    def run(self):
        logStr = ""
        while  not self.tbThreadStop:
            logStr = self.logQueue.get()
            if logStr == "console time out!":                      #OLT远程连接超时，传递"console time out!"
                self.sign_timeout.emit(False)
            elif logStr == "unreg_Return":
                unregResult = self.logQueue.get()
                self.sign_displayOnu.emit(unregResult)
            elif logStr != "\t" or logStr == "\n" and logStr == "":
                self.textBrowser.append(logStr)

    def stop(self):
        print("TBThread线程停止")
        self.tbThreadStop = True


class log():
    pass

import sys
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("pic/logo.jpg"))
    splash.show()
    ui = MainWindow()
    ui.show()
    splash.finish(ui)
    sys.exit(app.exec_())
