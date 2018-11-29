#KEG 2
berkas = open("L200180152", "w")
berkas.write("NIM saudara L200180152.""\n")
berkas.write("25/07/2000.""\n")
berkas.write("MU'TAZ AL FARISI""\n")
berkas.write("Kota Kelahiran Jepara")
berkas.close()

berkas = open("L200180152", "r")
a = berkas.readlines()
print (a[2])
print (a[3], a[1])
print (a[0])
berkas.close()

#KEG 3
import shelve

berkas = open("L200180152", "r")
NIM = berkas.readline()
TTL = berkas.readline()
NAMA = berkas.readline()
KOTA = berkas.readline()

berkas = shelve.open ("MU'TAZ")
berkas["biodata"]= [NIM,TTL,NAMA,KOTA]
berkas.close()


#KEG 4
berkas = shelve.open("MU'TAZ")
print (berkas["biodata"][0])
print (berkas["biodata"][1])
print (berkas["biodata"][2])
print (berkas["biodata"][3])
berkas.close()

