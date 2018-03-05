

file = open('produceSales.csv')
file.readline()

produceDict = {}

line = file.readline()
for line in file:
    line = line.strip()
    [produce, costPerPound, poundsSold, total] = line.split(',')
    if produce in produceDict:
        produceDict[produce] += float(total)
    else:
        produceDict[produce] = float(total)

file.close()

for item in sorted(produceDict):
    print(item, produceDict[item])
    

