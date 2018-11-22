##kegiatan 1

A = {1 : 'Mutaz Al Farisi', 2 : 'L200180152', 3 : 'Tahunan Jepara', 4 : '59419', 5 : 'laki laki', 6 : '25 Juli 2000', 7 : 'Informaika'}

def data1(nama):
    "menampilkan nama "
    print ('nama', A[1])
    return;
def data2(nim):
    "menampilkan NIM "
    print ('nim', A[2])
    return;
def data3(alamat):
    "menampilkan alamat "
    print ('alamat', A[3])
    return;
def data4(kodepos):
    "menampilkan kode pos "
    print ('kodepos', A[4])
    return;
def data5(jenis):
    "menampilkan jenis kelamin "
    print ('jenis', A[5])
    return;
def data6(lahir):
    "menampilkan tanggal lahir "
    print ('lahir', A[6])
    return;
def data7(prodi):
    "menampilkan nama prodi "
    print ('prodi', A
           [7])
    return;
def data8(awal, belakang):
    "menampilkan pilihan "
    print (awal, 'menampilkan', belakang)
    return;

x = "s"
while x != "k" :
    print ("anda dapat melihat informasi dasar anda")
    print ("Silahkan Memilih. Jika butuh bantuan Masukkan b untuk bantuan.")
    x = str(input("Masukkan Pilihan Anda : "))
    if x == "b":
        print("pilihan yang ada : ")
        data8("b   ", "bantuan ")
        data8("n   ", "nama ")
        data8("N   ", "NIM ")
        data8("A   ", "alamat ")
        data8("K   ", "kodepos ")
        data8("J   ", "jenis kelamin ")
        data8("T   ", "tanggal lahir ")
        data8("U   ", "prodi ")
        data8("k   ", "keluar ")
        
    elif x == "n":
        data1('nama anda adalah ');
    elif x == "N":
        data2('NIM anda adalah ');
    elif x == "A":
        data3('Alamat anda adalah ');
    elif x == "K":
        data4('Kodepos anda adalah ');
    elif x == "J":
        data5('Jenis Kelamin anda adalah ');
    elif x == "T":
        data6('Tanggal lahir anda adalah ');
    elif x == "U":
        data7('Prodi anda adalah ');
        
