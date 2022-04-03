from setup_wifi import *
from helper import *

run_command("sudo apt-get --yes update")
run_command("sudo apt-get --yes upgrade")
# install hostapd dnsmasq lighttpd
run_command("sudo apt-get --yes install hostapd dnsmasq lighttpd")

#set up grovepi
#curl -kL dexterindustries.com/update_grovepi | bash

#auto Start the application when booted
run_command("sudo cp /etc/rc.local /home/pi/6841_proj/original_wifi_file/rc.local")
print("seting auto start")
write_to_rclocal()
print(SUCCES,"Success", ENDC)

#open Phishing
setup_wifi()