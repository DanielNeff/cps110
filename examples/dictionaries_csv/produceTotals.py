

produceFile = open("produceSales.csv")
exit()
produceFile.readline()  # discard first line

produceTotals = {}
for line in produceFile:
  [produceType, costPerPound, poundsSold, total] = line.split(',')
  if produceType in produceTotals:
    produceTotals[produceType] = produceTotals[produceType] + float(total)
  else:
    produceTotals[produceType] = float(total)

for produceType in sorted(produceTotals):
  print('{0} - ${1:.2f}'.format(produceType, produceTotals[produceType]))

  
