import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 5228))
s.send("<stream>")
#s.flush()
s.send("<test/>")
s.send("<test/>")
s.send("<test/>")
s.send("</stream>")
#s.flush()
s.close()
