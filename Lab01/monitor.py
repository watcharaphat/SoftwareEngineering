# monitor.py
#
# Periodically monitor the bus system and see whether an identified
# bus returns to within a half-mile of Dave's office

import urllib
from xml.etree.ElementTree import parse
import time
import webbrowser
from math import sqrt
# Latitude of Dave's office.
office_lat = 41.980262
office_lon = -87.668452

# Set of bus ids that you want to monitor.  Change to match
# the output of the find_north.py script
busids = {''}


def distance(lat1, lat2):
    'Return approx miles between lat1 and lat2'
    return 69 * abs(lat1 - lat2)


def check():
    u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    doc = parse(u)
    data = u.read()
    f = open('rt22.xml', 'wb')
    f.write(data)
    f.close()
    print('Wrote rt22.xml')
    for bus in doc.findall('bus'):
        busid = bus.findtext('id')
        # if busid in busids:
        lat = float(bus.findtext('lat'))
        lon = float(bus.findtext('lon'))
        distLat = distance(lat, office_lat)
        distLon = distance(lon, office_lon)
        dist = sqrt(distLat*distLat + distLon*distLon)
        direction = bus.findtext('d')
        print('%s %s %0.2f miles' % (busid, direction, dist))

        if dist <= 2:  # < 0.5
            # Launch a browser to see on a map
            webbrowser.open(
                'http://maps.googleapis.com/maps/api/staticmap?size=500x500&sensor=false&markers=|%f,%f' % (
                    lat, lon))


# Launch a browser to see on a map
#webbrowser.open('http://maps.googleapis.com/maps/api/staticmap?size=500x500&sensor=false&markers=|%f,%f' % (office_lat, office_lon))


while True:
    check()
    time.sleep(60)
