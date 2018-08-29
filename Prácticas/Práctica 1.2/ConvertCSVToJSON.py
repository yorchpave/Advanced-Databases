# Para esta práctica, se trabajó con los datos de la página de Facebook de Oracle 
# con profundidad 1, para así poder cargar todos los datos del archivo JSON.

import csv
import json
import glob
import os

def CSVtoJSON():

    for filename in glob.glob('Oracle.csv'):
        csvfile = os.path.splitext(filename)[0]
        jsonfile = csvfile + '.json'

        with open(csvfile+'.csv') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        with open(jsonfile, 'w') as f:
            json.dump(rows, f, indent=4)

def loadJSON():

    with open('Oracle.json') as f:

        data = json.load(f)

        print("\nJSON cargado. Ordenados por:\n")
        print("Node, Source, Target, Type, Id, Label, timeset, Weight\n")

        for data_block in range(0, len(data) - 1):
            
            print(str (data_block), data[data_block]["Source"], data[data_block]["Target"], 
            data[data_block]["Type"], data[data_block]["Id"], data[data_block]["Label"], 
            data[data_block]["timeset"], data[data_block]["Weight"])

CSVtoJSON() # Lee el archivo CSV y lo escribe en un archivo JSON

loadJSON() # Lee el archivo JSON generado y carga en memoria los datos