import csv

with open('BaseVarejo.csv', mode='r') as arquivo_csv:
    csv_reader = csv.reader(arquivo_csv,delimiter=';')
    for row in csv_reader:
        print(row)

