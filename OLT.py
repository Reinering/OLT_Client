# -*- coding: utf-8 -*-
import time
import paramiko
import paramiko.ssh_exception
import subprocess
import telnetlib

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

    def auth(self, host, port, usr, pwd):
        print("开始登陆")
        self.tl = telnetlib.Telnet(host, port)
        self.tl.set_debuglevel(2)
        print("正在加载文件，请稍等……");
        time.sleep(0.5)
        self.tl.read_until(b"\n")
        self.tl.write(usr.encode("ascii") + '\r\n'.encode("ascii"))
        self.tl.read_until(b"\n")
        self.tl.write(pwd.encode("ascii") + '\r\n'.encode("ascii"))
        print("登陆成功")

    def exec_cmd(self, cmd):
            pass

    def close(self, cmd):
        self.tl.write(cmd.encode("ascii"))


class GEPON_OLT(object):

    def __init__(self):
        self.ssh_OLT = SSHOLT()
        self.telnet_OLT = TelnetOLT()
        self.olt_LinkState = False

    # 获取链路状态
    def getLinkState(self,ip):
        ping_True = True
        num = 5
        #运行ping程序
        while num:
            p = subprocess.Popen("ping %s -w 100 -n 1" %(ip),
                 stdin = subprocess.PIPE,
                 stdout = subprocess.PIPE,
                 stderr = subprocess.PIPE,
                 shell = True)

            #得到ping的结果
            # print(p.stdout.read())
            out = str(p.stdout.read(), encoding="gb2312", errors="ignore")
            print('ont:',out)

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
                ping_True = False
            elif 'bytes=32' in out:
                print('bytes=32')
                ping_True = False
            num -= 1
        print(ping_True)
        return ping_True

    # 登录OLT
    def loginOLT(self):
        pass
    # 退出OLT
    def exitOLT(self):
        pass
    # 查询ONU
    def queryONU(self):
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


class FH_OLT(GEPON_OLT):

    def __init__(self,olt_fact,olt_type,login_method,olt_ipaddr,olt_user,olt_passwd):
        super().__init__()
        self.olt_Fact = olt_fact
        self.olt_Type = olt_type
        self.login_Method = login_method
        self.olt_Ipaddr = olt_ipaddr
        self.olt_User = olt_user
        self.olt_Passwd = olt_passwd
        self.olt_PrintInfo = ""
        self.finish_cmd = ""

    def loginOLT(self):
        if self.getLinkState(self.olt_Ipaddr) is False:
            if self.login_Method == "Telnet":
                try:
                    return_str = self.telnet_OLT.auth(self.login_Method, 23, self.olt_User, self.olt_Passwd)
                    self.olt_LinkState = True
                    return (self.olt_Fact + " OLT IP地址：" + self.olt_Ipaddr + " Telnet 已登陆\n")
                except Exception as e:
                    print("Telnet登陆错误：", e)
                    return "Telnet登录失败,请检查IP地址，用户名密码是否正确，确认无误后请重新登录"

            elif self.login_Method == "SSH2":
                try:
                    self.ssh_OLT.auth(self.olt_Ipaddr, 22, self.olt_User, self.olt_Passwd)
                    self.olt_LinkState = True
                    return self.olt_Fact + " OLT IP地址：" + self.olt_Ipaddr + " SSH2 已登陆"
                except Exception as e:
                    print("SSH2登陆错误：", e)
                    self.olt_LinkState = False
                    return "SSH2登录失败,请检查IP地址，用户名密码是否正确，确认无误后请重新登录"

            elif self.login_Method == "SSH":
                pass
            else:
                print("login_method值传递错误")
            return ""
        else:
            self.olt_LinkState = False
            return "登录失败，请检查配置网络是否连接正常，确认无误后请重新登录"

    def exitOLT(self):
        if self.olt_LinkState == False:
            return(self.login_Method + "未登陆，无需退出")
        if self.login_Method == "SSH2":
            self.ssh_OLT.exec_cmd("exit\n")
            self.ssh_OLT.close()
        elif self.login_Method == "Telnet":
            self.telnet_OLT.close("exit" + "\n")
        return ("成功退出")

    def regONU(self, SN):
        if self.olt_LinkState == False:
            return("OLT未登陆，请重新登陆后注册")
        return SN

    def unRegONU(self):
        pass

    def addService(self):
        pass

    def exec_cmd(self, cmd):
        pass

class ZTE_OLT(GEPON_OLT):
    pass

class HW_OLT(GEPON_OLT):
    pass


if __name__ == "__main__":
    FH_OLT("1", "2")