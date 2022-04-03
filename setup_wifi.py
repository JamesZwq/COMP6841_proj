import time
from helper import *

def setup_wifi():

    print("seting interfaces")
    fp = open("/etc/network/interfaces","a")
# allow-hotplug wlan0: Start wlan0 sending wifi signal
# Router ip address
# Router netmask
    fp.write(
"""
allow-hotplug wlan0
iface wlan0 inet static
    address 192.168.0.1
    netmask 255.255.255.0
"""
    )
    fp.close()
    print(SUCCES,"Success", ENDC)



    print("seting hostapd")
    fp = open("/etc/hostapd/hostapd.conf","a")
#ssid is wifi name
#hw_mode=g 2.4 giga herz
#channel=1-6  2.4 giga herz
#wmm_enabled=0 turn off wmm, we do not need that
#auth_algs=1 open wpa 
    fp.write(
"""
interface=wlan0
ssid=uniwide
hw_mode=g
channel=1
wmm_enabled=0
auth_algs=1
"""
    )
    fp.close()
    print(SUCCES,"Success", ENDC)

    print("seting hostapd reading file")
    fp = open("/etc/default/hostapd","a")
#let hostapd read /etc/hostapd/hostapd.conf
    fp.write(
"""
DAEMON_CONF="/etc/hostapd/hostapd.conf"
"""
    )
    fp.close()

    print("seting dnsmasq")
    fp = open("/etc/dnsmasq.conf","a")
#set the range of ip that router allocates to each device
#set the ip of captive portal
    fp.write(
"""
interface=wlan0 
dhcp-range=192.168.0.2,192.168.0.30,12h 
address=/#/192.168.0.1
"""
    )
    fp.close()
    print(SUCCES,"Success", ENDC)

    #restart dnsmasq and hostapd to make the change take effect
    run_command("sudo systemctl unmask hostapd")
    run_command("sudo service hostapd restart")
    run_command("sudo service dnsmasq restart")

    #setup lighttpd
    run_command("sudo cp /home/pi/6841_proj/setup_wifi_file/lighttpd.conf /etc/lighttpd/lighttpd.conf")

    #setup frontend
    run_command("sudo cp /home/pi/6841_proj/setup_wifi_file/index.html /var/www/html/index.html")
    run_command("sudo cp /home/pi/6841_proj/setup_wifi_file/unswico.png /var/www/html/unswico.png")
    run_command("sudo cp /home/pi/6841_proj/setup_wifi_file/unswbackground.jpg /var/www/html/unswbackground.jpg")

    print("reboot in 3 seconds")
    time.sleep(1)
    print("reboot in 2 seconds")
    time.sleep(1)
    print("reboot in 1 seconds")
    time.sleep(1)
    run_command("sudo reboot")

if __name__ == "__main__":
    setup_wifi()
