#site = open("fetched_data/accuweather_
from os import listdir
from pyquery import PyQuery as pq
filenames = listdir("fetched_data")
filenames = [f for f in filenames if "accuweather_" in f and "T123" in f]
#print filenames
for filename in filenames: 
    #print filename
    #print "fetched_data/"+filename
    with open("fetched_data/"+filename, "r") as f:
        print filename
        doc = pq(f.read())
        #import pdb; pdb.set_trace()
        temp = doc("#feed-sml-3 .city-fcast-text .temp")
        temp = int(temp.text().split()[0])
        print temp
        #print f.read()
