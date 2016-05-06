import urllib

u = urllib.urlopen('http://bit.ly/22lJJ5V')
data = u.read()
f = open('rt22.xml', 'wb')
f.write(data)
f.close()
