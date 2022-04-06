# COMP6841_proj
## **Introduction**
This is a fishing wifi modeled on unsw's wifi running on raspberry pi, can do some operations on other hardware through grovepi+.

## **Video**
YouTube link:

https://www.youtube.com/watch?v=wCiVEr4_N0E

## **Setup**

`
curl -kL dexterindustries.com/update_grovepi | bash
`
to setup grovepi

`
sudo python3 frist_time_setup.py
`
to setup the project

## **Tested version**
+ raspberrypi v5.10.103
+ Python 3.7.3
+ hostapd v2.8
+ lighttpd v1.4.53
+ Dnsmasq v2.80

## **Handware**
+ Raspberry Pi 4 Model B 4GB
+ Grovepi+
+ Grove - Button(P)
+ Grove - Switch(P)
+ Grove - LCD RGB backlight v4
+ Grove - Rotary Angle Sensor

## **Ability**
+ Redirect newly connect user to a Captive Portal
+ There is screen that can display some menu option, and select some actions.
+ Attacker will have direct access to this information by simple operations after inserting a usb drive
+ This Hotspot can be turned to a harmless device with one single press on the button.
+ The screen changes colors through RGB cycling.
+ Screen can be easily closed

## **Functionalities**
### **menu**:
  + #### push button to turn on/off Phishing:
  Fishing can be easily turned on and off
  + #### Num connecting:
  View  the total number of devices connected to this hotspot in real—time
  + #### Num zid received:
  View the total number of Zid and passwords that have been received in real-time
  + #### Get data:
  Insert the usb device into the usb port on the side, and then you can use this option to write the obtained zid and password to the usb device. If the usb device cannot be written or the usb device is not detected, the screen will display "no device", if The number of zid and password that have been obtained is 0, the screen will display "No data", if the writing is successful, it will display "success", data.txt and data.json will be written to the usb device, and the usb device will be ejected safely.
  + #### Clear Acquired Data:
  Delete all zid and password that have been acquired, The screen displays "success" if the cleanup is successful, and "error, no data" if there is currently no data
  + #### poweroff ? :
  Basic function, shutdown

## **File introduction**:
  + #### frist_time_setup.py:
  For first time setup, install hostapd, dnsmasq and lighttpd, and add main.py to boot.
  + #### hardware.py:
  For reading sensor data
  + #### helper.py:
  Some helper functions, including running command line commands and writing to rc.local
  + #### main.py:
  The implementation of the menu will also use multithreading to run the backend of the Login page.
  + #### phase_out_wifi.py:
  Turn off phishing by changing all changed files to what they were before and reboot.
  + #### rgbscreen.py:
  Control the color and text displayed on the screen.
  + #### server.py:
  The back-end of the login page, to accept the submitted table by the front-end and store the data.
  + #### setup_wifi.py:
  Enabling fishing is the core of the entire project. Change the settings of interfaces, hostapd, dnsmasq and lighttpd to enable fishing. The function of each step is mentioned in the comments of this file.
  + #### wifi_connect_detile.py:
  Get the current number of device connected this hot spot, the currently acquired zid and password, and the current phishing status.
  
## **What I learn**:
+ Basic understanding on Rospberry Pi.
+ Basic understanding on Phsihing WIFI/Hotspot
+ Operations of Rospberry Pi.
+ Practices into Embedded Programming.
+ Fundemental Principal of Online Phising.

## **Reference**

File: rgbscreen.py

grovepi official github library

https://github.com/DexterInd/GrovePi/blob/master/Software/Python/grove_rgb_lcd/grove_rgb_lcd.py
