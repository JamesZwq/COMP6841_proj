from helper import *
import time

def phase_out_wifi():
    print("phase out interfaces")
    run_command("sudo cp /home/pi/6841_proj/original_wifi_file/interfaces /etc/network/interfaces")
    print(SUCCES,"Success", ENDC)

    print("phase out hostapd")
    open("/etc/hostapd/hostapd.conf","w").close()
    print(SUCCES,"Success", ENDC)

    print("seting hostapd reading file")
    run_command("sudo cp /home/pi/6841_proj/original_wifi_file/hostapd /etc/default/hostapd")
    print(SUCCES,"Success", ENDC)

    print("phase out dnsmasq")
    run_command("sudo cp /home/pi/6841_proj/original_wifi_file/dnsmasq.conf /etc/dnsmasq.conf")
    print(SUCCES,"Success", ENDC)

    run_command("sudo cp /home/pi/6841_proj/original_wifi_file/lighttpd.conf /etc/lighttpd/lighttpd.conf ")
    try:
        run_command("sudo rm /var/www/html/index.html")
        run_command("sudo rm /var/www/html/unswico.png")
        run_command("sudo rm /var/www/html/unswbackground.jpg")
    except:
        pass

    print("reboot in 3 seconds")
    time.sleep(1)
    print("reboot in 2 seconds")
    time.sleep(1)
    print("reboot in 1 seconds")
    time.sleep(1)
    run_command("sudo reboot")

if __name__ == "__main__":
    phase_out_wifi()