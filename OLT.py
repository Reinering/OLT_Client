# -*- coding: utf-8 -*-


import os
import time
import paramiko
import paramiko.ssh_exception
import subprocess

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


class OLT(object):
    def __init__(self):
        self. olt_Fact = ""
        self.olt_Type =  ""
        self.login_Method = ""
        self.olt_Ipaddr = ""
        self.olt_LinkState = False
        self.olt_PrintInfo = ""
        self.ssh_OLT = SSHOLT()

    # 获取链路状态
    def getLinkState(self,ip):
        ping_True = False
        num = 5
        #运行ping程序
        while num:
            p = subprocess.Popen("ping %s -w 10 -n %c" %(ip, num),
                 stdin = subprocess.PIPE,
                 stdout = subprocess.PIPE,
                 stderr = subprocess.PIPE,
                 shell = True)

            #得到ping的结果
            out = str(p.stdout.read(), encoding="utf-8")
            # print out
            print('ont:',out)

            # #找出丢包率，这里通过‘%’匹配
            # regex = re.compile(r'\w*%\w*')
            # packetLossRateList = regex.findall()
            if 'Request timed out' in out:
                pass
            elif 'General failure' in out:
                pass
            elif "Destination host unreachable" in out:
                pass
            elif "Destination net unreachable" in out:
                pass
            elif 'bytes=32' in out:
                ping_True = False
            num -= 1
        print("ping完成")
        return ping_True

    # 登录OLT
    def loginOLT(self, olt_fact, olt_type, login_method, olt_ipaddr):
        print(olt_fact, olt_type, login_method, olt_ipaddr)
        if self.getLinkState(olt_ipaddr):
            if login_method == "Telnet":
                pass
            elif login_method == "SSH2":
                pass
            elif login_method == "SSH":
                pass
            else:
                print("login_method值传递错误")
            return ""
        else:
            return "登录失败，请检查配置网络是否连接正常，IP地址，用户名密码是否正确，确认无误后请重新登录"


    # 退出OLT
    def exitOLT(self):
        print("退出")

    # 查询ONU
    def queryONU(self):
        print("查询ONU")

    # 注册ONU
    def regONU(self):
        print("注册ONU")

    #去注册ONU
    def unRegONU(self):
        print("去注册ONU")

    #添加业务
    def addService(self):
        print("添加业务")
