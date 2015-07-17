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


import numpy

#get the differences
fieldnames = ['Date', 'La Colline', 'Maties', 'Accuweather', 'Yr.no', 'Weather.com', 'Time and Date', 'Weather Underground', 'Accuweather Difference', 'Yr.no Difference', 'Weather.com Difference', 'Time and Date Difference', 'Weather Underground Difference']
dates = ['%s' % day for day in sorted([int(date) for date in data.keys()])]
print dates
#import pdb; pdb.set_trace()
acc_diffs = []
yr_diffs = []
com_diffs = []
tad_diffs = []
wu_diffs = []
for i in range(1,len(dates)-1):
    this_day = dates[i]
    next_day = dates[i+1]
    difference = data[next_day]["Maties"] - data[this_day]["Accuweather"]
    data[this_day]["Accuweather Difference"] = difference
    acc_diffs.append(difference)
    #print this_day, next_day, difference
    difference = data[next_day]["Maties"] - data[this_day]["Yr.no"]
    data[this_day]["Yr.no Difference"] = difference
    yr_diffs.append(difference)
    #print this_day, next_day, difference    
    difference = data[next_day]["Maties"] - data[this_day]["Weather.com"]
    data[this_day]["Weather.com Difference"] = difference
    com_diffs.append(difference)
    #print this_day, next_day, difference
    difference = data[next_day]["Maties"] - data[this_day]["Time and Date"]
    data[this_day]["Time and Date Difference"] = difference
    tad_diffs.append(difference)
    #print this_day, next_day, difference
    difference = data[next_day]["Maties"] - data[this_day]["Weather Underground"]
    data[this_day]["Weather Underground Difference"] = difference
    wu_diffs.append(difference)
    #print this_day, next_day, difference
averages = []


print averages

#acc_ave = numpy.mean(acc_diffs)
#print acc_ave
#print numpy.std(acc_diffs)
#print numpy.mean(yr_diffs)
#print numpy.std(yr_diffs)
#print numpy.mean(com_diffs)
#print numpy.std(com_diffs)
#print numpy.mean(tad_diffs)
#print numpy.std(tad_diffs)
#print numpy.mean(wu_diffs)
#print numpy.std( wu_diffs)

#print acc_diffs, yr_diffs, com_diffs, tad_diffs, wu_diffs


with open('raw_data.csv', 'w') as csvfile:
    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for day in dates:
        data[day]["Date"] = day
        writer.writerow(data[day])
        print data[day]
    
    writer.writerow({
        'Date': 'Average',
	'Accuweather Difference': numpy.mean(acc_diffs),
	'Yr.no Difference': numpy.mean(yr_diffs),
	'Weather.com Difference': numpy.mean(com_diffs), 
	'Time and Date Difference': numpy.mean(tad_diffs), 
	'Weather Underground Difference': numpy.mean(wu_diffs)
        })

    writer.writerow({
        'Date': 'Standard Deviation',
	'Accuweather Difference': numpy.std(acc_diffs),
	'Yr.no Difference': numpy.std(yr_diffs),
	'Weather.com Difference': numpy.std(com_diffs), 
	'Time and Date Difference': numpy.std(tad_diffs), 
	'Weather Underground Difference': numpy.std(wu_diffs)
        })

        
