
import re

msg = """
  F/S/P                   : 0/0/2
  ONT-ID                  : 0
  Control flag            : active
  Run state               : offline
  Config state            : initial
  Match state             : initial
  DBA type                : SR
  ONT distance(m)         : -
  ONT battery state       : -
  Memory occupation       : -
  CPU occupation          : -
  Temperature             : -
  Authentic type          : SN-auth
  SN                      : 4A5A484768C31A10 (JZHG-68C31A10)
  Management mode         : OMCI
  Software work mode      : normal
  Isolation state         : normal
  Description             : ONT_NO_DESCRIPTION
  Last down cause         : LOS
  Last up time            : 2018-04-09 14:39:35+08:00
  Last down time          : 2018-04-09 14:41:48+08:00
  Last dying gasp time    : 2018-04-08 17:35:49+08:00
  """


def parseMsg(msg):
    # lines = msg.split("\n")
    # print(re.findall(r'The number of GPON autofind ONT is \d{1,2}', msg, flags=re.MULTILINE))

    onuSlot = re.findall(r'\d{1,2}/\d{1,2}/\d{1,2}', msg, flags=re.MULTILINE)[0]
    tempId = re.findall(r'ONT-ID.*', msg, flags=re.MULTILINE)
    tempSN = re.findall(r'SN .*', msg, flags=re.MULTILINE)
    tempState = re.findall(r'Run state.*', msg, flags=re.MULTILINE)

    onuId = (tempId[0].split(':')[1])[1:]
    onuSN = (re.findall(r'\([\w-]*\)', tempSN[0], flags=re.MULTILINE)[0][1:])[:-1]
    onuState = (tempState[0].split(':')[1])[1:]


    # tempList = re.findall(r'\([\w-]*\)', tempList)
    print(tempSN)
    print(onuSlot)
    print(onuId)
    print(onuSN)
    print(onuState)

    # i = 0
    # tmpList = []
    # while i < len(tempList):
    #     temp = []
    #     temp.append(slotList[i])
    #     tempList[i] = ((tempList[i])[1:])[:-1]
    #     temp.append(tempList[i])
    #     tmpList.append(temp)
    #     i += 1
    # print(tmpList)






parseMsg(msg)