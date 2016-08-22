import csv
f = open('311_Service_Requests_-_Pot_Holes_Reported.csv')
for row in csv.DictReader(f):
    addr = row['STREET ADDRESS']
    num = row['NUMBER OF POTHOLES FILLED ON BLOCK']
