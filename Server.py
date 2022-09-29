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
  url = f'https://us-central1-stellar-cipher-364002.cloudfunctions.net/Email-sender?receiver={data["receiver"]}&subject={data["subject"]}&message{data["message"]}'

  print(url)

  x = requests.get(url)
  print(x.status_code)

  c.send('Thank you for connecting'.encode("utf-8"))
  c.close()


