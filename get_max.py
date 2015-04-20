#site = open("fetched_data/accuweather_
from os import listdir
filenames = listdir("fetched_data")
filenames = [f for f in filenames if "accuweather_" in f and "T123" in f]
print filenames
for filename in filenames: 
    f = open("fetched_data/"+filename, "r")
    print filename
    print "fetched_data/"+filename
