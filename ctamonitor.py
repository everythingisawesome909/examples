from xml.etree.ElementTree import parse
import time, os, fnmatch, shutil
doc = parse('rt22.xml')

t = time.localtime()
timestamp = time.strftime('Completed at %H%M on %b-%d-%Y', t)

for bus in doc.findall('bus'): 
    route = bus.findtext('rt')
    busid = bus.findtext('id')
    op = bus.findtext('op')
    direction = bus.findtext('dn')
    print "Route,Bus, Operator, Direction"
    print(route, busid, op, direction)
    
else:
     print(timestamp)
