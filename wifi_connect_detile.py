import json

from helper import *


def get_number_of_connected():
    connect_detl = run_command_with_return_value("arp -a")
    if connect_detl is None or connect_detl == "":
        return 0
    return connect_detl.count("\n")+1

def get_number_of_zid_password():
	try:
		fp = open("/home/pi/data.json","r")
		data = json.load(fp)
		fp.close()
		return data["num_user"]
	except:
		return "0"

def get_wifi_status():
    fp = open("/etc/hostapd/hostapd.conf","r")
    if(fp.read().count('wlan0') == 0):
        fp.close()
        return 0
    else:
        fp.close()
        return 1
