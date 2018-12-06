#KEG 1
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50003))
s.listen(5)
print "program komunikasi data diri"
data = ""
kamus = {"nama" : "MU'TAZ AL FARISI",
         "nim" : "L200180152",
         "angkatan" : "2018"}
while data.lower() != "keluar":
    komm, addr = s.accept()
    while data.lower() != "keluar":
        data = komm.recv(1024)
        if data.lower() == "keluar":
            s.close()
            break
        print "perintah:", data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send("maaf, perintah tidak dimengerti")
