import csv

produceFile = open("produceSalesAltered.csv")
produceFile.readline()  # discard first line

csvReader = csv.reader(produceFile)

produceTotals = {}
for csvLine in csvReader:
    [produceType, costPerPound, poundsSold, total] = csvLine
    if produceType in produceTotals:
        produceTotals[produceType] = produceTotals[produceType] + float(total)
    else:
        produceTotals[produceType] = float(total)

for produceType in sorted(produceTotals):
    print('{0} - ${1:.2f}'.format(produceType, produceTotals[produceType]))

  
