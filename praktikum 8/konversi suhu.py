def konversisuhu (C = 0, F = 0):
    print('menampilkan suhu')
    if C != 0:
        y = ((9*C/5) + 32)
        print ("Suhu", C ,"celcius setara dengan", y ,"fahenheit")
    elif F != 0:
        b = ((F - 32)* 5/9)
        print ("Suhu", F ,"fahrenheit setara dengan", b ,"celcius")
    else :
        print ("Suhu 0 celcius setara dengan 32 fahrenheit")

