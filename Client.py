import sys, socket, json

s = socket.socket()
s.connect(("External IP of the Server", 3389))   # need to be replaced

rawData = {"receiver": sys.argv[1], "subject": sys.argv[2], "message": sys.argv[3]}

data = json.dumps(rawData)
s.send(data.encode("utf-8"))
rMsg = s.recv(1024).decode("utf-8")
print(rMsg)
s.close()