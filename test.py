
import re

msg = """display ont autofind all
   ----------------------------------------------------------------------------
   Number              : 1
   F/S/P               : 0/0/0
   Ont SN              : 424C4B4768EEFF21 (BLKG-68EEFF21)
   Password            : 0x20202020202020202020(          )
   Loid                :
   Checkcode           :
   VendorID            : 0x00000000
   Ont Version         :
   Ont SoftwareVersion :
   Ont EquipmentID     :
   Ont autofind time   : 2018-04-16 08:49:31+08:00
   ----------------------------------------------------------------------------
   ----------------------------------------------------------------------------
   Number              : 2
   F/S/P               : 0/0/0
   Ont SN              : 424C4B4768EEFF22 (BLKG-68EEFF22)
   Password            : 0x20202020202020202020(          )
   Loid                :
   Checkcode           :
   VendorID            : 0x00000000
   Ont Version         :
   Ont SoftwareVersion :
   Ont EquipmentID     :
   Ont autofind time   : 2018-04-16 08:49:31+08:00
   ----------------------------------------------------------------------------

   The number of GPON autofind ONT is 2"""


def parseMsg(msg):
    # lines = msg.split("\n")
    print(re.findall(r'The number of GPON autofind ONT is \d{1,2}', msg, flags=re.MULTILINE))

    slotList = re.findall(r'\d{1,2}/\d{1,2}/\d{1,2}', msg, flags=re.MULTILINE)
    tempList = re.findall(r'\([\w-]*\)', msg, flags=re.MULTILINE)

    # tempList = re.findall(r'\([\w-]*\)', tempList)
    print(tempList)
    i = 0
    tmpList = []
    while i < len(tempList):
        temp = []
        temp.append(slotList[i])
        tempList[i] = ((tempList[i])[1:])[:-1]
        temp.append(tempList[i])
        tmpList.append(temp)
        i += 1
    print(tmpList)






parseMsg(msg)