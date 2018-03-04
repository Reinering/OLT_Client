# -*- coding: utf-8 -*-


import os
import time
import paramiko
import paramiko.ssh_exception
import subprocess

class SSH_OLT(object):
    def __init__(self, host, port, usr, pwd):
        self.client = paramiko.SSHClient()
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

    # 获取链路状态
    def getLinkState(self,ip):
        ping_True = True
        #运行ping程序
        while ping_True:
            p = subprocess.Popen("ping %s -w 10 -n 1 "%ip,
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

        print("ping完成")

    def loginOLT(self, olt_fact, olt_type, login_method, olt_ipaddr):
        print(olt_fact, olt_type, login_method, olt_ipaddr)

    def exitOLT(self):
        print("退出")

    def queryONU(self):
        print("查询ONU")

    def regONU(self):
        print("注册ONU")

    def unRegONU(self):
        print("去注册ONU")
