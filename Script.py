#needs only jpg in directory, inlcuding hidden folders/files
#assume lat is postive, long negative


import os
import pyexiv2
import glob
import pickle
import string 

os.chdir('C:\Users\Marsh\Documents\Aptana Studio 3 Workspace\PhotoGPSscraper\\2012-12-02')


    
    
for filename in os.listdir('C:\Users\Marsh\Documents\Aptana Studio 3 Workspace\PhotoGPSscraper\\2012-12-02'):
    metadata = pyexiv2.ImageMetadata(filename)
    metadata.read()
    lat = metadata['Exif.GPSInfo.GPSLatitude']
    long = metadata['Exif.GPSInfo.GPSLongitude']
    s = pickle.dumps((lat.key, lat.raw_value))
    (key, raw_value) = pickle.loads(s)
    lat = pyexiv2.ExifTag(key)
    lat.raw_value = raw_value
    x = lat.raw_value
    hours = x[0:2]
    mins = x[5]
    secs= x[9:]
    hours = float(hours)
    minsd = float(mins)/60
    xs = secs.split('/')
    xs2 = map(float,xs)
    secreal= xs2[0]/xs2[1]
    secreald = secreal/3600
    LatD=hours+minsd+secreald
    #Repeat for Long
    s = pickle.dumps((long.key, long.raw_value))
    (key, raw_value) = pickle.loads(s)
    long = pyexiv2.ExifTag(key)
    long.raw_value = raw_value
    x = long.raw_value
    hours = x[0]
    mins = x[4:6]
    secs= x[9:]
    hours = float(hours)
    minsd = float(mins)/60
    xs = secs.split('/')
    xs2 = map(float,xs)
    secreal= xs2[0]/xs2[1]
    secreald = secreal/3600
    LongD=(hours+minsd+secreald)*-1 #Flip side of meridain
    print LatD,',',LongD