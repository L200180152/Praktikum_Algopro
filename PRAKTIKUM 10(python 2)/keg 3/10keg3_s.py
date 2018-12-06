import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50007))
s.listen(5)
print "Server sudah siap"
perintah = ''
p=0
l=0
while perintah != 'keluar':
    komm, addr = s.accept()
    while perintah != 'keluar':
        data = komm.recv(1024).lower().split("=")
        perintah = data[0]
        if perintah == 'keluar':
            s.close()
            break
        print 'Pesan:', perintah
        if len(data) == 2:
            if perintah == 'lebar':
                l = int(data[1])
                respon = "lebar dicatat"
                komm.send(respon)
            elif perintah == 'panjang':
                p = int(data[1])
                respon = "panjang dicatat"
                komm.send(respon)
            else:
                komm.send('pesan tidak diketahui')
        elif perintah == 'hitung':
            L = float(p*l)
            respon = "Luas segi empat dengan panjang {} dan lebar {} adalah {}".format(p,l,L)
            komm.send(respon)
        else:
            komm.send('pesan tidak diketahui')
