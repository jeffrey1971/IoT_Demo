
#!/usr/bin/python
# create by Jeffrey
import sys, getopt
import urllib
import os
import time
import datetime
#from datetime import *
from xml.dom import minidom

WEATHER_URL = 'http://query.yahooapis.com/v1/public/yql?q=select%20%2A%20from%20weather.forecast%20where%20u=%22c%22%20and%20woeid='
WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'

def weather_for_zip():
    url = WEATHER_URL + zipcode
    dom = minidom.parse(urllib.urlopen(url))
    forecasts = ""
    ycondition = dom.getElementsByTagNameNS(WEATHER_NS, 'condition')[0]
    n= ycondition.getAttribute('text')
    t= ycondition.getAttribute('temp')
    return n+" "+t+"C"


city='Others City'

if(len(sys.argv)>1):
    zipcode=sys.argv[1]
else:
    zipcode=2306179

print zipcode
if(zipcode=='2306179'):
    city='Taipei City'
elif(zipcode=='2306180'):
    city='Kaohsiung City'
elif(zipcode=='2306181'):
    city='Taichung City'

print city


str2='python lcdv2.py '

citystr=str2+"'"+city+"'"
os.system(citystr)

current_time=time.strftime("%Y-%m-%d %H:%M")
#current_time=time.strftime("%H:%M:%S")
current_time_str=str2+"'"+current_time+"'"
print current_time_str
os.system(current_time_str)

str1=weather_for_zip()
print str1
newstr=str2+"'"+str1+"'"
print newstr
os.system(newstr)
