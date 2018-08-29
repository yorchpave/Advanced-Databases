import csv
import json
import glob
import os

for filename in glob.glob('/home/yorchpave/Dropbox/ITESM/Bases de Datos Avanzadas/Oracle.csv'):
    csvfile = os.path.splitext(filename)[0]
    jsonfile = csvfile + '.json'

    with open(csvfile+'.csv') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open(jsonfile, 'w') as f:
        json.dump(rows, f, indent = 4)