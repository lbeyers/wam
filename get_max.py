from os import listdir
from pyquery import PyQuery as pq
import json
all_files = listdir("fetched_data")
all_files.sort()

#accuweather_
filenames = [f for f in all_files if "accuweather_" in f and "T123" in f]
for filename in filenames: 
    with open("fetched_data/"+filename, "r") as f:
        doc = pq(f.read())
        #import pdb; pdb.set_trace()
        temp = doc("#feed-sml-3 .city-fcast-text .temp")
        temp = int(temp.text().split()[0])
        print filename,temp

#la_colline_
filenames = [f for f in all_files if "la_colline_" in f and "T233" in f]
for filename in filenames: 
    with open("fetched_data/"+filename, "r") as f:
        doc = pq(f.read())
        #import pdb; pdb.set_trace()
        temp = doc("#gpx_content table th font").eq(11).html()
        temp = float(temp)
        print filename,temp

#yr_no_longterm_
filenames = [f for f in all_files if "yr_no_longterm_" in f and "T123" in f]
for filename in filenames: 
    with open("fetched_data/"+filename, "r") as f:
        doc = pq(f.read())
        #import pdb; pdb.set_trace()
        temp = doc("#ctl00_ctl00_contentBody td.temperature.plus").eq(0).html()
        temp = int(temp[:-1])
        print filename,temp


#weather_com_
filenames = [f for f in all_files if "weather_com_" in f and "T123" in f]
for filename in filenames: 
    with open("fetched_data/"+filename, "r") as f:
        doc = pq(f.read())
        #import pdb; pdb.set_trace()
        temp = doc(".mw-temperature").eq(2)
        temp = int(temp.text().split()[0])
        temp = (temp - 32)/1.8
        print filename,temp


#maties_measurements
filenames = [f for f in all_files if "maties_" in f and "T230" in f]
#We used an alternative time - find long-term solution
for filename in filenames: 
    with open("fetched_data/"+filename, "r") as f:
        doc = pq(f.read())
        #import pdb; pdb.set_trace()
        temp = doc("#maxTemp")
        temp = float(temp.text().split(u'\xb0')[0])
        print filename,temp


#time_and_date_
filenames = [f for f in all_files if "time_and_date_" in f and "T123" in f]
for filename in filenames: 
    with open("fetched_data/"+filename, "r") as f:
        doc = pq(f.read())
        #import pdb; pdb.set_trace()
        temp = doc("#qlook p").eq(1).html().split(u'<br/>')[1]
        temp = int(temp.split(u'\xa0')[0].split()[-1])
        print filename,temp


#weather_underground
filenames = [f for f in all_files if "weather_underground_" in f and "T123" in f]
for filename in filenames: 
    with open("fetched_data/"+filename, "r") as f:
        doc = json.loads(f.read())
        #import pdb; pdb.set_trace()
        temp = doc[u'forecast'][u'simpleforecast'][u'forecastday'][1][u'high'][u'celsius']
        temp = int(temp)
        print filename,temp
