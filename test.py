
import re

# msg = """
#   [gpon]
#   <gpon-0/0>
#  interface gpon 0/0
#  port 0 ont-auto-find enable
#  ont add 0 1 sn-auth "4A5A4F4768FFFFEB" omci ont-lineprofile-id 10
# ont-srvprofile-id 10 desc "ONT_NO_DESCRIPTION"
#  ont add 0 2 sn-auth "4A5A484768CCCCCC" omci ont-lineprofile-id 11
# ont-srvprofile-id 11 desc "ONT_NO_DESCRIPTION"
#  ont add 0 10 sn-auth "4A5A4F4704101111" omci ont-lineprofile-id 50
# ont-srvprofile-id 50 desc "ONT_NO_DESCRIPTION"
#  ont add 0 20 sn-auth "4A5A4F4704102020" omci ont-lineprofile-id 40
# ont-srvprofile-id 40 desc "ONT_NO_DESCRIPTION"
#  ont port vlan 0 20 eth 1 translation 1001 user-vlan 101
#  ont port vlan 0 20 eth 1 translation 1001 user-vlan 102
#  ont port vlan 0 20 eth 1 translation 1001 user-vlan 103
#  ont port vlan 0 20 eth 1 translation 1001 user-vlan 104
#  ont port vlan 0 20 eth 1 translation 1001 user-vlan 105
#  ont port vlan 0 20 eth 1 translation 1001 user-vlan 106
#  ont port vlan 0 20 eth 1 translation 1001 user-vlan 107
#  ont port vlan 0 20 eth 1 translation 1001 user-vlan 108
#  ont port vlan 0 20 eth 2 translation 2001 user-vlan 101
#  ont port vlan 0 20 eth 2 translation 2001 user-vlan 102
#  ont port vlan 0 20 eth 2 translation 2001 user-vlan 103
#  ont port vlan 0 20 eth 2 translation 2001 user-vlan 104
#  ont port vlan 0 20 eth 2 translation 2001 user-vlan 105
#  ont port vlan 0 20 eth 2 translation 2001 user-vlan 106
#  ont port vlan 0 20 eth 2 translation 2001 user-vlan 107
#  ont port vlan 0 20 eth 2 translation 2001 user-vlan 108
#  ont port vlan 0 20 eth 3 translation 3001 user-vlan 101
#  ont port vlan 0 20 eth 3 translation 3001 user-vlan 102
#  ont port vlan 0 20 eth 3 translation 3001 user-vlan 103
#  ont port vlan 0 20 eth 3 translation 3001 user-vlan 104
#  ont port vlan 0 20 eth 3 translation 3001 user-vlan 105
#  ont port vlan 0 20 eth 3 translation 3001 user-vlan 106
#  ont port vlan 0 20 eth 3 translation 3001 user-vlan 107
#  ont port vlan 0 20 eth 3 translation 3001 user-vlan 108
# #
# [bbs-config]
#   <bbs-config>
#  service-port 11 vlan 101 gpon 0/0/0 ont 10 gemport 1 multi-service user-vlan
# 101 tag-transform translate
#  service-port 12 vlan 102 gpon 0/0/0 ont 10 gemport 1 multi-service user-vlan
# 102 tag-transform translate
#  service-port 13 vlan 103 gpon 0/0/0 ont 10 gemport 1 multi-service user-vlan
# 103 tag-transform translate
#  service-port 14 vlan 104 gpon 0/0/0 ont 10 gemport 1 multi-service user-vlan
# 104 tag-transform translate
#  service-port 15 vlan 105 gpon 0/0/0 ont 10 gemport 1 multi-service user-vlan
# 105 tag-transform translate
#  service-port 16 vlan 106 gpon 0/0/0 ont 10 gemport 1 multi-service user-vlan
# 106 tag-transform translate
#  service-port 17 vlan 1001 gpon 0/0/0 ont 20 gemport 1 multi-service user-vlan  1001 tag-transform translate
#  service-port 18 vlan 2001 gpon 0/0/0 ont 20 gemport 1 multi-service user-vlan  2001 tag-transform translate
#  service-port 19 vlan 3001 gpon 0/0/0 ont 20 gemport 1 multi-service user-vlan  3001 tag-transform translate
#  service-port 20 vlan 107 gpon 0/0/0 ont 10 gemport 1 multi-service user-vlan
# 107 tag-transform translate
#  service-port 21 vlan 108 gpon 0/0/0 ont 10 gemport 1 multi-service user-vlan
# 108 tag-transform translate
#  service-port 85 vlan 44 gpon 0/0/0 ont 2 gemport 1 multi-service user-vlan 44  tag-transform transparent
#  service-port 86 vlan 45 gpon 0/0/0 ont 2 gemport 1 multi-service user-vlan 45  tag-transform transparent
#  service-port 87 vlan 46 gpon 0/0/0 ont 2 gemport 1 multi-service user-vlan 46  tag-transform transparent
#  service-port 88 vlan 999 gpon 0/0/0 ont 2 gemport 1 multi-service user-vlan 999 tag-transform transparent
#  service-port 90 vlan 999 gpon 0/0/0 ont 1 gemport 1 multi-service user-vlan 999 tag-transform transparent
#  service-port 91 vlan 45 gpon 0/0/0 ont 1 gemport 1 multi-service user-vlan 45  tag-transform transparent
#  service-port 92 vlan 46 gpon 0/0/0 ont 1 gemport 1 multi-service user-vlan 46  tag-transform transparent
# #
# [btv-config]
#   <btv-config>
#  btv
#  igmp user add service-port 86 no-auth
#  multicast-vlan 45
#   igmp multicast-vlan member service-port-list 86
# #
# return
#   """
#
#
# def parseMsg(msg):
#     # lines = msg.split("\n")
#     # print(re.findall(r'The number of GPON autofind ONT is \d{1,2}', msg, flags=re.MULTILINE))
#
#     # onuSlot = re.findall(r'\d{1,2}/\d{1,2}/\d{1,2}', msg, flags=re.MULTILINE)[0]
#     tempId = re.findall(r'ont add.*sn-auth', msg, flags=re.MULTILINE)
#     onuId = tempId[-1].split(" ")[3]
#     # tempSN = re.findall(r'SN .*', msg, flags=re.MULTILINE)
#     # tempState = re.findall(r'Run state.*', msg, flags=re.MULTILINE)
    #
    # onuId = (tempId[0].split(':')[1])[1:]
    # onuSN = (re.findall(r'\([\w-]*\)', tempSN[0], flags=re.MULTILINE)[0][1:])[:-1]
    # onuState = (tempState[0].split(':')[1])[1:]


    # tempList = re.findall(r'\([\w-]*\)', tempList)
    # print(tempSN)
    # # print(onuSlot)
    # print(tempId)
    # print(onuId)
    # print(onuSN)
    # print(onuState)

    # i = 0
    # tmpList = []
    # while i < len(tempList):
    #     temp = []
    #     temp.append(slotList[i])
    #     tempList[i] = ((tempList[i])[1:])[:-1]
    #     temp.append(tempList[i])
    #     tmpList.append(temp)
#     #     i += 1
#     # print(tmpList)
#
# parseMsg(msg)
#

# import xml.dom.minidom
# import xml.dom.minicompat
# import lxml
#
# def parseConfXML():  # 初始化、读取XML
#     configList = []
#     onuList = {}
#     doc = xml.dom.minidom.parse("config.xml")
#     root = doc.documentElement
#     oltNodes = root.getElementsByTagName("OLT")
#     for node in oltNodes:
#         tempList = []
#         tempList.append(node.getAttribute("name"))
#         childNodes = node.getElementsByTagName("onuType")
#         for childNode in childNodes:
#             tempMap = {}
#             tempMap["onuType"] = childNode.getAttribute("name")
#             for para in childNode.childNodes:
#                 for paraChild in para.childNodes:
#                     if paraChild.nodeType == xml.dom.minidom.Node.TEXT_NODE:
#                             if para.nodeName == "#text":
#                                 tempMap[para.nodeName] = ''
#                             else:
#                                 tempMap[para.nodeName] = paraChild.data
#             tempList.append(tempMap)
#         configList.append(tempList)
#     print(configList)
#
# parseConfXML()



#
# msg = """ont add 0 21 sn-auth BLKG-68EEFF21 omci  ont-linepro mand:
#           ont add 0 21 sn-auth BLKG-68EEFF21 omci  ont-lineprofile-id 10 ont-srvprofile-id 10
#   Failure: The bandwidth is not enough
#
# MA5608T(config-if-gpon-0/0)#
# """
#
#
# print("Failure: The bandwidth is not enough" in msg)
#
#
# print(re.findall(r"\d{1,2}/\d{1,2}/\d{1,2}", "0/0/0", flags=re.MULTILINE))



msg = """
MA5608T#display ont info 0 0 0 all
  -----------------------------------------------------------------------------
  F/S/P   ONT         SN         Control     Run      Config   Match    Protect
          ID                     flag        state    state    state    side
  -----------------------------------------------------------------------------
  0/ 0/0    1  4A5A4F4768FFFFEB  active      offline  initial  initial  no
  0/ 0/0    2  474C475004A1FFFF  active      online   normal   match    no
  0/ 0/0    3  4A5A484768FFFF87  active      offline  initial  initial  no
  0/ 0/0    4  4A5A484768C35930  active      offline  initial  initial  no
  0/ 0/0   10  4A5A4F4704101111  active      offline  initial  initial  no
  0/ 0/0   20  4A5A4F4704102020  active      offline  initial  initial  no
  -----------------------------------------------------------------------------
  F/S/P   ONT-ID   Description
  -----------------------------------------------------------------------------
  0/ 0/0       1   ONT_NO_DESCRIPTION
  0/ 0/0       2   ONT_NO_DESCRIPTION
  0/ 0/0       3   ONT_NO_DESCRIPTION
  0/ 0/0       4   ONT_NO_DESCRIPTION
  0/ 0/0      10   ONT_NO_DESCRIPTION
  0/ 0/0      20   ONT_NO_DESCRIPTION
  -----------------------------------------------------------------------------
  In port 0/ 0/0 , the total of ONTs are: 6, online: 1
  -----------------------------------------------------------------------------
"""
tempList = re.findall(r'0/ \d{1,2}/\d{1,2} *\d{1,3} *\w* *\w* *(?:offline|online)', msg, flags=re.MULTILINE)
# tempList = iter([])
#tempList = re.match(r'0/ \d{1,2}/\d{1,2} *\d{1,3} *\w* *\w* *(offline|online)', msg)

# pattern = re.compile(r'0/ \d{1,2}/\d{1,2} *\d{1,3} *\w* *\w* *(offline|online)')
# tempList = pattern.match(msg)
print(tempList)
for temp in tempList:
    tempL = temp.split(" ")
    print(tempL)
    l = []
    for i in tempL:
        # print(i)
        if i != '':
            l.append(i)
    tempL = l

    print(tempL)

