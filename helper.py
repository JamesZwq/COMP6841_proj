import datetime
import subprocess as commands

ENDC = '\033[0m'
FAIL = '\033[91m'
SUCCES = '\033[92m'
def run_command(command):
    current_time = datetime.datetime.now()
    print("Running command ", command)
    status, output = commands.getstatusoutput(command)
    print("Time taken to run command: ", datetime.datetime.now() - current_time)
    if status != 0:
        print(FAIL, "Error: " + output, ENDC)
        exit(FAIL)
    else:
        print(SUCCES,"Success", ENDC)
        return True

def run_command_with_return_value(command):
    current_time = datetime.datetime.now()
    print("Running command ", command)
    status, output = commands.getstatusoutput(command)
    print("Time taken to run command: ", datetime.datetime.now() - current_time)
    if status != 0:
        print(FAIL, "Error: " + output, ENDC)
        exit(FAIL)
    else:
        print(SUCCES,"Success", ENDC)
        return output

def run_command_with_error_message(command):
    status, output = commands.getstatusoutput(command)
    return [status, output]


#add “sudo /usr/bin/python3 /home/pi/6841_proj/main.py” brfore “exit 0”
def write_to_rclocal():
    fd = open("/etc/rc.local", "r")
    if fd.read().count('exit 0') != 2:
        print(FAIL, "Error: /etc/rc.local does not contain exit 0", ENDC)
        exit(FAIL)
    fd.close()
    fd = open("/etc/rc.local", "r")
    lines = fd.readlines()
    fd.close()
    fd = open("/etc/rc.local", "w")
    for line in lines:
        if line.find('exit 0') != -1:
            line = line.replace('exit 0', '')
        fd.write(line)
    fd.close()

    fd = open("/etc/rc.local", "a")
    fd.write("sudo /usr/bin/python3 /home/pi/6841_proj/main.py \nexit 0")
    fd.close()
