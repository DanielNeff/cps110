def selectionSort(items: list):

    for lastPlace in range(len(items) - 1, 0, -1):

        maxLoc = 0

        for j in range(1, lastPlace + 1):
            if items[j] > items[maxLoc]:
                maxLoc = j

        temp = items[maxLoc]
        items[maxLoc] = items[lastPlace]
        items[lastPlace] = temp 


items = [3, 2, 6, 4, 1]
selectionSort(items)
print(items)