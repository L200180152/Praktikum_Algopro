def hitungLuas(p, l):
    "fungsi menghitung luas dari Segi empat"
    L = p * l
    return L

print "<!DOCTYPE html>"
print
print"""<html>
        <head>
            <title>Kegiatan 3</title>
        </head>
        <body>
                <table>
                        <tr>
                                <th colspan=2>Bangun Geometri</th>
                        </tr>
                        <tr>
                                <td rowspan=6><img src="segiempat.png" width=500 height=300></td>
                                <td>Nama Bangun : Segi Empat</td>
                        </tr>
                        <tr>
                                <td>Dimensi : 2D</td>
                        </tr>
                        <tr>
                                <td>Rumus Luas : p x l</td>
                        </tr>
                        <tr>
                                <td>Parameter 1 : 10 cm</td>
                        </tr>
                        <tr>
                                <td>Parameter 2 : 20 cm</td>
                        </tr>
                        <tr>
                                <td>Luas : """
print hitungLuas(10,20)
print """ cm</td>
                        </tr>
                </table>
        </body>
</html>"""


                                
                                
