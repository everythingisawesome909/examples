import urllib2
from bs4 import BeautifulSoup
from HTMLParser import HTMLParser
from datetime import datetime, time

W  = '\033[0m'  # white
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan

url = "https://spacexstats.com/missions/jcsat-14"
page = urllib2.urlopen(url)

soup = BeautifulSoup(page)
mydivs = soup.find("div", { "class" : "container values" })

class HTML_tag_stripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = HTML_tag_stripper()
    s.feed(html)
    return s.get_data()

print ''+G+''
print 'Tasked Completion Window, L.O.T.Y., Vehicle, Destination, Pad, Probability'
print strip_tags( str(mydivs) ).replace('24th', '')
print 'Payload: JCSAT-14 Geosynchronous Communication Satellite'
print 'Manufacturer: JSAT Corporation, Japan'
print ''

def dateDiffinSeconds(date1, date2): 
  timedelta = date2 - date1
  return timedelta.days * 24 * 3600 + timedelta.seconds

def daysHoursMinutesSecondsFromSeconds(seconds): 
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        return (days, hours, minutes, seconds)

start_date = datetime.strptime('2016-05-06 00:21:00', '%Y-%m-%d %H:%M:%S')
end_date = datetime.strptime('2016-05-06 01:21:00', '%Y-%m-%d %H:%M:%S')
now = datetime.now()

print ''+R+'%d Days, %d Hours, %d Minutes, and %d Seconds until launch window closes' % daysHoursMinutesSecondsFromSeconds(dateDiffinSeconds(now, end_date))
print ''+W+'%d Days, %d Hours, %d Minutes, and %d Seconds until launch window opens' % daysHoursMinutesSecondsFromSeconds(dateDiffinSeconds(now, start_date))
