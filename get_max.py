from os import listdir
from pyquery import PyQuery as pq
import json
import csv 
from lxml.etree import XMLSyntaxError

all_files = listdir("fetched_data")
all_files.sort()
data = {}


#accuweather_
filenames = [f for f in all_files if "accuweather_" in f and "T123" in f]
for filename in filenames:
    day = filename.split("T")[0].split("_")[-1]
    if not day in data.keys():
        data[day] = {}
    with open("fetched_data/"+filename, "r") as f:
        doc = pq(f.read())
        #import pdb; pdb.set_trace()
        temp = doc("#feed-sml-3 .city-fcast-text .temp")
        temp = int(temp.text().split()[0])
        data[day]["Accuweather"] = temp
        print filename,temp

#la_colline_
filenames = [f for f in all_files if "la_colline_" in f and "T233" in f]
for filename in filenames: 
    day = filename.split("T")[0].split("_")[-1]
    if not day in data.keys():
        data[day] = {}
    with open("fetched_data/"+filename, "r") as f:
        try:
            doc = pq(f.read())
            #import pdb; pdb.set_trace()
            temp = doc("#gpx_content table th font").eq(5).html()
            temp = float(temp)
        except XMLSyntaxError:
	    temp = 0.0
	    print "Could not read ", filename
        data[day]["La Colline"] = temp
        print filename,temp

#yr_no_longterm_
filenames = [f for f in all_files if "yr_no_longterm_" in f and "T123" in f]
for filename in filenames: 
    day = filename.split("T")[0].split("_")[-1]
    if not day in data.keys():
        data[day] = {}
    with open("fetched_data/"+filename, "r") as f:
        doc = pq(f.read())
        #import pdb; pdb.set_trace()
        temp = doc("#ctl00_ctl00_contentBody td.temperature.plus").eq(0).html()
        temp = int(temp[:-1])
        data[day]["Yr.no"] = temp
        print filename,temp


#weather_com_
filenames = [f for f in all_files if "weather_com_" in f and "T123" in f]
for filename in filenames: 
    day = filename.split("T")[0].split("_")[-1]
    if not day in data.keys():
        data[day] = {}
    with open("fetched_data/"+filename, "r") as f:
        doc = pq(f.read())
        #import pdb; pdb.set_trace()
        temp = doc(".mw-temperature").eq(2)
        temp = int(temp.text().split()[0])
        temp = (temp - 32)/1.8
        data[day]["Weather.com"] = temp
        print filename,temp


#maties_measurements
filenames = [f for f in all_files if "maties_" in f and "T230" in f]
#We used an alternative time - find long-term solution
for filename in filenames: 
    day = filename.split("T")[0].split("_")[-1]
    if not day in data.keys():
        data[day] = {}
    with open("fetched_data/"+filename, "r") as f:
        doc = pq(f.read())
        #import pdb; pdb.set_trace()
        temp = doc("#maxTemp")
        temp = float(temp.text().split(u'\xb0')[0])
        data[day]["Maties"] = temp
        print filename,temp


#time_and_date_
filenames = [f for f in all_files if "time_and_date_" in f and "T123" in f]
for filename in filenames: 
    day = filename.split("T")[0].split("_")[-1]
    if not day in data.keys():
        data[day] = {}
    with open("fetched_data/"+filename, "r") as f:
        doc = pq(f.read())
        #import pdb; pdb.set_trace()
        temp = doc("#qlook p").eq(1).html().split(u'<br/>')[1]
        temp = int(temp.split(u'\xa0')[0].split()[-1])
        data[day]["Time and Date"] = temp
        print filename,temp


#weather_underground
filenames = [f for f in all_files if "weather_underground_" in f and "T123" in f]
for filename in filenames: 
    day = filename.split("T")[0].split("_")[-1]
    if not day in data.keys():
        data[day] = {}
    with open("fetched_data/"+filename, "r") as f:
        doc = json.loads(f.read())
        #import pdb; pdb.set_trace()
        temp = doc[u'forecast'][u'simpleforecast'][u'forecastday'][1][u'high'][u'celsius']
        temp = int(temp)
        data[day]["Weather Underground"] = temp
        print filename,temp


with open('raw_data.csv', 'w') as csvfile:
    fieldnames = ['Date', 'La Colline', 'Maties', 'Accuweather', 'Yr.no', 'Weather.com', 'Time and Date', 'Weather Underground']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for day in sorted(data.keys()):
        data[day]["Date"] = day
        writer.writerow(data[day])

