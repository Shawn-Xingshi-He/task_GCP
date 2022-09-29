import socket, json, requests

s = socket.socket()        
print ("Socket successfully created")
port = 3389
s.bind(('', port))        
print ("socket binded to %s" %(port))
s.listen(5)    
print ("socket is listening")           
while True:
  c, addr = s.accept()    
  print ('Got connection from', addr )
  rawData = c.recv(1024).decode("utf-8")
  data = json.loads(rawData)
  url = f'(HTTP trigger)?receiver={data["receiver"]}\
  &subject={data["subject"]}&message{data["message"]}' # HTTP trigger need to be replaced

  print(url)

  x = requests.get(url)
  print(x.status_code)

  c.send('Thank you for connecting'.encode("utf-8"))
  c.close()


