import csv
f = open('311_Service_Requests_-_Pot_Holes_Reported.csv', 'r')

potholes_by_zip = {}

for row in csv.DictReader(f):
    status = row['STATUS']
    zipcode = row['ZIP']
    num = row['NUMBER OF POTHOLES FILLED ON BLOCK']
    if num != '':
        if zipcode not in potholes_by_zip:
            potholes_by_zip[zipcode] = float(num)
        else:
            potholes_by_zip[zipcode] += float(num)


print('#\tZIP code\tNUM_HOLES')

i = 1
for key in sorted(potholes_by_zip, key=potholes_by_zip.get, reverse=True)[0:5]:
    print('#' + str(i) + '\t' + key + '\t\t' + str(potholes_by_zip[key]))
    i += 1
