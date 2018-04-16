# -*- coding: utf-8 -*-
import time
import paramiko
import paramiko.ssh_exception
import subprocess
import telnetlib
from PyQt5 import QtCore
import re

class SSHOLT(object):

    def __init__(self):
        self.client = paramiko.SSHClient()

    def auth(self, host, port, usr, pwd):
        # key = paramiko.RSAKey.from_private_key_file(pkeyFile, password=pkeyPwd)
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 通过公共方式进行认证 (不需要在known_hosts 文件中存在)
        # self.client.connect(host, port, username=usr, password=pwd, pkey=key)
        self.client.connect(host, port, username=usr, password=pwd)

    def exec_cmd(self, cmd):
        return self.client.exec_command(cmd)

    def close(self):
        self.client.close()

class TelnetOLT(object):

    def __init__(self):
        self.shell_prompts = ('#', '$', ':~$' )

    def auth(self, host, port, usr, pwd, login_prompt):
        print("开始登陆")
        self.tl = telnetlib.Telnet(host, port)
        self.tl.set_debuglevel(2)
        print("正在加载文件，请稍等……")
        time.sleep(0.5)
        self.tl.read_until(bytes(login_prompt[0],encoding="ascii"))
        self.tl.write(usr.encode("ascii"))
        self.tl.read_until(bytes(login_prompt[1],encoding="ascii"))
        self.tl.write(pwd.encode("ascii"))
        print("登陆成功")

    def exec_cmd(self, cmd):
        self.tl.write(cmd.encode("ascii"))
        time.sleep(1)
    def read_until(self,prompt):
        msg = self.tl.read_until(bytes(prompt, encoding="ascii")).decode("utf-8")
        print("返回msg", msg)
        return msg
    def read_some(self):
        msg = self.tl.read_some().decode("utf-8")
        print("返回msg", msg)
        return msg
    def read_very_eager(self):
        msg = self.tl.read_very_eager().decode("utf-8")
        print("返回msg", msg)
        return msg
    def read_very_lazy(self):
        msg = self.tl.read_very_lazy().decode("utf-8")
        print("返回msg", msg)
        return msg
    def read_all(self):
        msg = self.tl.read_all().decode("utf-8")
        print("返回msg", msg)
        return msg
    def close(self, cmd):
        self.tl.write(cmd.encode("ascii"))


class GEPON_OLT(object):

    def __init__(self):
        self.ssh_OLT = SSHOLT()
        self.telnet_OLT = TelnetOLT()
        self.olt_LinkState = False
        self.stopBool = False
        self.dictOLT = {}

    # 获取链路状态
    def getLinkState(self,ip):
        ping_True = False
        sTime = time.time()
        # 运行ping程序
        while not self.stopBool:
            time.sleep(1)
            if time.time() - sTime > 180:
                break
            p = subprocess.Popen("ping %s -w 100 -n 1" % (ip),
                                 stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 shell=True)

            # 得到ping的结果
            # print(p.stdout.read())
            out = str(p.stdout.read(), encoding="gb2312", errors="ignore")
            print('ont:', out)

            # #找出丢包率，这里通过‘%’匹配
            # regex = re.compile(r'\w*%\w*')
            # packetLossRateList = regex.findall()
            if 'Request timed out' in out:
                print('Request timed out')
            elif 'General failure' in out:
                print('General failure')
            elif "Destination host unreachable" in out:
                print("Destination host unreachable")
            elif "Destination net unreachable" in out:
                print("Destination net unreachable")
            elif "丢失 = 1 " in out:
                print("丢失 = 1 ")
            elif "字节=32" in out:
                print("字节=32")
                ping_True = True
                break
            elif 'bytes=32' in out:
                print('bytes=32')
                ping_True = True
                break
        print(ping_True)
        return ping_True
    # 登录OLT
    def loginOLT(self):
        pass
    # 退出OLT
    def exitOLT(self):
        pass
    # 查询ONU
    def query_unRegONU(self):
        pass
    def query_regONU(self, SN):
        pass
    # 注册ONU
    def regONU(self, SN):
        pass
    #去注册ONU
    def unRegONU(self):
        pass
    #添加业务
    def addService(self):
        pass
    # 执行命令
    def exec_cmd(self, cmd):
        pass
    def telnetView(self,view_prompt):
        pass

class FH_OLT(GEPON_OLT):


    def __init__(self, olt_fact,olt_type,login_method,olt_ipaddr,olt_user,olt_passwd, queue):
        super(FH_OLT, self).__init__()
        self.dictOLT = {}
        self.olt_Fact = olt_fact
        self.olt_Type = olt_type
        self.login_Method = login_method
        self.olt_Ipaddr = olt_ipaddr
        self.olt_User = olt_user
        self.olt_Passwd = olt_passwd
        self.olt_PrintInfo = ""
        self.logQueue = queue
        self.dictOLT = {}

    def exitOLT(self):
        if self.olt_LinkState:
            self.logQueue.put(self.login_Method + "未登陆，无需退出")
        if self.login_Method == "SSH2":
            self.ssh_OLT.exec_cmd("exit\n")
            self.ssh_OLT.close()
            self.logQueue.put("SSH2成功退出")
        elif self.login_Method == "Telnet":
            self.telnet_OLT.close("exit" + "\n")
            self.logQueue.put("Telnet成功退出")
    def regONU(self, SN):
        if self.olt_LinkState:
            return("OLT未登陆，请重新登陆后注册")
        return SN

    def unRegONU(self):
        if self.olt_LinkState:
            pass

        else:
            self.logQueue.put("OLT未登陆，请重新登陆后注册")

    def addService(self):
        pass

    def exec_cmd(self, cmd):
        pass

class ZTE_OLT(GEPON_OLT):
    def __init__(self, olt_fact,olt_type,login_method,olt_ipaddr,olt_user,olt_passwd, queue):
        super(ZTE_OLT, self).__init__()
        self.dictOLT = {}
        self.olt_Fact = olt_fact
        self.olt_Type = olt_type
        self.login_Method = login_method
        self.olt_Ipaddr = olt_ipaddr
        self.olt_User = olt_user
        self.olt_Passwd = olt_passwd
        self.olt_PrintInfo = ""
        self.logQueue = queue


class HW_OLT(GEPON_OLT):


    def __init__(self, olt_fact,olt_type,login_method,olt_ipaddr,olt_user,olt_passwd, queue):
        super(HW_OLT, self).__init__()
        self.dictOLT = {}
        self.olt_Fact = olt_fact
        self.olt_Type = olt_type
        self.login_Method = login_method
        self.olt_Ipaddr = olt_ipaddr
        self.olt_User = olt_user
        self.olt_Passwd = olt_passwd
        self.olt_PrintInfo = ""
        self.logQueue = queue
        self.dictOLT = {}
        self.liveTh = liveThread(self.login_Method, self.telnet_OLT, self.ssh_OLT, self.logQueue)

        self.telnet_prompt = [">>User name:", ">>User password:"]



    def loginOLT(self):
        if not self.getLinkState(self.olt_Ipaddr):
            self.olt_LinkState = False
            self.logQueue.put("登录失败，请检查配置网络是否连接正常，确认无误后请重新登录")
            return False

        if self.login_Method == "Telnet":
            try:
                self.telnet_OLT.auth(self.olt_Ipaddr, 23, self.olt_User+"\r\n", self.olt_Passwd+"\r\n", self.telnet_prompt)
                self.olt_LinkState = True
                self.logQueue.put(self.olt_Fact + " OLT IP地址：" + self.olt_Ipaddr + " Telnet登陆\n")
                return True
            except Exception as e:
                print("Telnet登陆错误：", e)
                self.olt_LinkState = False
                self.logQueue.put("Telnet登录失败,请检查IP地址，用户名密码是否正确，确认无误后请重新登录")
                return False

        elif self.login_Method == "SSH2":
            try:
                self.ssh_OLT.auth(self.olt_Ipaddr, 22, self.olt_User, self.olt_Passwd)
                self.olt_LinkState = True
                self.logQueue.put(self.olt_Fact + " OLT IP地址：" + self.olt_Ipaddr + " SSH2 已登陆")
                return True
            except Exception as e:
                print("SSH2登陆错误：", e)
                self.olt_LinkState = False
                self.logQueue.put("SSH2登录失败,请检查IP地址，用户名密码是否正确，确认无误后请重新登录")
                return False
        elif self.login_Method == "SSH":
            return False
        else:
            print("login_method值传递错误")
            self.logQueue.put("请选择登录方式")
            self.olt_LinkState = False
            return False

    def exitOLT(self):
        self.liveTh.stop()
        self.stopBool = True
        if self.olt_LinkState:
            if self.login_Method == "SSH2":
                self.ssh_OLT.exec_cmd("exit\r\n")
                self.ssh_OLT.close()
                self.logQueue.put("SSH2成功退出")
            elif self.login_Method == "Telnet":
                self.telnet_OLT.close("exit \r\n")
                self.logQueue.put("Telnet成功退出")
        else:
            self.logQueue.put(self.login_Method + "未登陆，无需退出")
        self.olt_LinkState = False

    def query_unRegONU(self):
        #解析查询ONU返回的结果
        def parseResult(msg):
            # 匹配ONU所在槽位
            slotList = re.findall(r'\d{1,2}/\d{1,2}/\d{1,2}', msg, flags=re.MULTILINE)
            # 匹配ONU上报SN
            snList = re.findall(r'\([\w-]*\)', msg, flags=re.MULTILINE)
            # 生成result数组
            i = 0
            resultList = []
            while i < len(snList):
                tmp = []
                tmp.append(((snList[i])[1:])[:-1])
                tmp.append(slotList[i])
                resultList.append(tmp)
                i += 1
            return resultList
        #递归确认返回的结果是否已全部返回完成
        def recMsg(msg):
            if "More ( Press " in msg:
                print("More ( Press存在")
                self.telnet_OLT.exec_cmd(chr(32) + "\r\n")
                tmp = self.telnet_OLT.read_very_eager()
                msg += recMsg(tmp)
            return msg

        msg = ""
        try:
            if self.olt_Type == "GPON":
                self.telnet_OLT.exec_cmd("display ont autofind all \r\n")
                msg = self.telnet_OLT.read_very_eager()
                print("msg:", msg)
            if "Failure: The automatically found ONTs do not exist" in msg:
                self.logQueue.put(msg)
            elif not msg:
                pass
            else:
                msg = recMsg(msg)
                self.logQueue.put(msg)
                result = parseResult(msg)
                self.logQueue.put("unreg_Return")
                self.logQueue.put(result)
        except Exception as e:
            print(e)
            self.olt_LinkState = False
            self.liveTh.stop()
            print("telnet连接中断")

    def query_regONU(self, SN):
        try:
            if self.olt_Type == "GPON":
                msg = self.telnet_OLT.exec_cmd("display ont info by-sn " + SN + "\r\n")
                print(msg)
        except Exception as e:
            print(e)
            self.olt_LinkState=False
            self.liveTh.stop()
            print("telnet连接中断")

    def consoleView(self,view_prompt):
        if self.login_Method == "Telnet":
            msg = self.telnet_OLT.exec_cmd(view_prompt)
            self.logQueue.put(msg)
        self.liveTh.start()

class liveThread(QtCore.QThread):

    def __init__(self, login_Method, telnetOLT, sshOLT, queue):
        super(liveThread, self).__init__()
        self.login_Method = login_Method
        self.telnet_OLT = telnetOLT
        self.ssh_OLT = sshOLT
        self.logQueue = queue
        self.stopBool = True

    def run(self):
        if self.login_Method == "Telnet":
            while self.stopBool:
                self.telnet_OLT.exec_cmd("\r\n")
                msg = self.telnet_OLT.read_until("#")
                self.logQueue.put(msg)
                if "Configuration console time out, please retry to log on" in msg:
                    self.logQueue.put("console time out!")
                    self.stopBool = False
                    break
                time.sleep(60)

    def stop(self):
        self.stopBool = False



if __name__ == "__main__":
    pass