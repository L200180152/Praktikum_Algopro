a = str(input('masukkan password: '))
b = 'mutaz'
for i in range(2):
    if a == b:
        print ('Anda berhasil login')
        break
    elif a != b:
        a = str(input('Maaf, anda salah memasukkan password,masukkan password: '))
else:
    print('Anda telah mencoba 3 kali, Akses di tolak')
