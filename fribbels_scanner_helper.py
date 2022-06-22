import re
import subprocess

import win32service
import win32serviceutil

if __name__ == '__main__':
    try:
        win32serviceutil.StartService('Wired AutoConfig')
    except:
        pass
    win32serviceutil.WaitForServiceStatus('Wired AutoConfig', win32service.SERVICE_RUNNING, 30)

    output = subprocess.check_output('netsh lan show interfaces')
    lines = [re.sub(r'\s+', ' ', x).strip() for x in output.decode().strip().split('\r\n')][2:]

    interfaces = []
    interface = {}
    for line in lines:
        if line:
            k, v = line.split(' : ')
            if k == 'GUID':
                v = v.upper()
            interface[k] = v
        else:
            interfaces.append(interface)
            interface = {}

    #import json
    #print(json.dumps(interfaces, indent=2, sort_keys=True))

    for interface in interfaces:
        if interface['Name'] == 'vEthernet (BluestacksNxt)':
            print(interface['GUID'])

    input()