Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = "Mu'taz Al Farisi"
>>> NIM = "L200180152"
>>> X = "1" + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> 
>>> type(a)
<class 'int'>
>>> type(b)
<class 'int'>
>>> a / b
72.0
>>> a // b
72
>>> 10 * (a - 999)
1530
>>> b ** 2
256
>>> a % b
0
>>> 
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> a / c
92.16
>>> a // c
92.0
>>> a % c
2.0
>>> 
>>> c > b
False
>>> type(c > b)
<class 'bool'>
>>> a > b and b > c
True
>>> a > 1100 or b < 10
True
>>> 
