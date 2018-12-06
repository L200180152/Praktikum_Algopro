#keg 1
import socket

hostname = "localhost"
pesan = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50003))
print "program komunikasi data diri"
while pesan.lower() != "keluar":
    pesan = raw_input("pertanyaan: ")
    s.send(pesan)
    if pesan.lower() != "keluar":
        response = s.recv(1024)
        print "jawab: ", response
    else:
        print "siap!!"
        s.close()
