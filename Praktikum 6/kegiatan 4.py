Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = "Mu'taz Al Farisi"
>>> NIM = 152
>>> Tinggi = 1.70
>>> Berat = 52
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> 
>>> type(Aku)
<class 'tuple'>
>>> Aku[0]
2000
>>> a = NIM % 4; Aku[a]
2000
>>> type(Aku[a])
<class 'int'>
>>> Aku[a:4]
(2000, 52, 1.7, 152)
>>> type(Aku[4])
<class 'str'>
>>> Aku[0] = "ok"
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    Aku[0] = "ok"
TypeError: 'tuple' object does not support item assignment
>>> 
>>> type(Data)
<class 'tuple'>
>>> type(Data[4])
<class 'str'>
>>> Data[4][5]
'z'
>>> Data[4][a:6]
"Mu'taz"
>>> Data[0] = "ok"; Data
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    Data[0] = "ok"; Data
TypeError: 'tuple' object does not support item assignment
>>> Data[-a]
2000
>>> range(a)
range(0, 0)
>>> 
