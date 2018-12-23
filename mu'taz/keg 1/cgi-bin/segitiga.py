a=5
b=6
def hitung_segitiga(a=0,t=0):
    return (a*t)/2
print "<!DOCTYPE html>"
print
print """<html>
	<head>
		<title>Saya Noob</title>
		<style>
		body, table {
			font-family: arial;
			font-weight: bold;
		}
		.judul {
			font-size: 2rem;
			margin: 0;
		}
		img {
			padding-right: 1rem;
		}
		</style>
	</head>"""
	
print """<body>
		<img src="../segitiga.png" style="width:200px;float:left;">
		<p class="judul">Data Diri<p>"""


print                   "<table>"
print			"""<tr>
				<td>Nama Bangun</td>
				<td>:</td>
				<td>Segitiga</td>
			</tr>

			<tr>
				<td>Dimensi(2D/3D)</td>
				<td>:</td>
				<td>2D</td>
			</tr>

			<tr>
				<td>Rumus Luas</td>
				<td>:</td>
				<td>a x t / 2</td>
			</tr>"""

print			"""<tr>
				<td>parameter 1</td>
				<td>:</td>"""
print				"<td>"
print (a)
print                           "</td>"
print			"</tr>"

print			"""<tr>
				<td>parameter 2</td>
				<td>:</td>"""
print				"<td>"
print (b)
print                           "</td>"
print			"</tr>"
			
print			"<tr>"
print				"""<td>luas</td>
				<td>:</td>"""
print				"<td>"
print hitung_segitiga(a,b)
print                           "</td>"
print			"</tr>"

print		"</table>"
		
print	"""</body></html>"""
