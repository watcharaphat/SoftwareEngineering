from math import *


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
        print('%s  %s  %s cop noob' % (self.bid, self.lat, self.lon))


b = Bus(0, 0, 0)

b.printbus()

b = Bus(10, 20, 30)

b.printbus()
