from math import *
import urllib
import urllib.request
import time
import webbrowser
from xml.etree.ElementTree import parse

office_lat = 41.980262
office_lon = -87.668452
s = []


class Bus:
    def __init__(self, bid, lat, lon):
        self.bid = bid
        self.lat = lat
        self.lon = lon

    def update(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def distance(self, lat1, lat2):
        'Return approx miles between lat1 and lat2'
        return 69 * abs(lat1 - lat2)

    def distancefromoffice(self, office_lat, office_lon):
        distlat = self.distance(self.lat, office_lat)
        distlon = self.distance(self.lon, office_lon)
        return sqrt(pow(distlat, 2) + pow(distlon, 2))

    def checkbid(self, s):
        return self.bid in s

    def printbus(self):
        print('%s  %s  %s' % (self.bid, self.lat, self.lon))


def fetch():
    u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    data = u.read()
    f = open('rt22.xml', 'wb')
    f.write(data)
    f.close()
    print('fetched')


def find_north():
    doc = parse('rt22.xml')
    for bus in doc.findall('bus'):
        lat = float(bus.findtext('lat'))
        if lat >= office_lat:
            busid = bus.findtext('id')
            direction = bus.findtext('d')
            if direction.startswith('North'):
                s.append(busid)


def find_buses():
    doc = parse('rt22.xml')
    for bus in doc.findall('bus'):
        busid = bus.findtext('id')
        lat = float(bus.findtext('lat'))
        lon = float(bus.findtext('lon'))
        b = Bus(busid, lat, lon)
        b.lat = lat
        b.lon = lon
        if b.bid in s:
            direction = bus.findtext('d')
            if b.distancefromoffice(office_lat, office_lon) <= 0.5:
                print('%s %s %0.2f miles' % (busid, direction, b.distancefromoffice(office_lat, office_lon)))
                popup_map(b.lat, b.lon)


def popup_map(lat, lon):
    url = 'http://maps.googleapis.com/maps/api/staticmap?center=41.980262,+-87.668452&zoom=15&scale=1&size=500x500&maptype=roadmap&format=png&visual_refresh=true&markers=color:red%7Clabel:O%7C41.980262,+-87.668452&markers=color:blue%7Clabel:B%7C' + str(
        lat) + ',+' + str(lon)
    webbrowser.open(url)


while True:
    s.clear()
    fetch()
    find_north()
    find_buses()
    time.sleep(15)
