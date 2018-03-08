import csv

produceFile = open("produceSalesAltered.csv")
csvReader = csv.reader(produceFile)

produceData = list(csvReader) # Get a list of lists

produceTotals = {}
for csvLine in produceData[1:]:
    # Extract data from current line
    [produceType, costPerPound, poundsSold, total] = csvLine
    if produceType in produceTotals:
        produceTotals[produceType] = produceTotals[produceType] + float(total)
    else:
        produceTotals[produceType] = float(total)

for produceType in sorted(produceTotals):
    print('{0} - ${1:.2f}'.format(produceType, produceTotals[produceType]))

  
