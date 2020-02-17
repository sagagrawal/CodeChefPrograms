# Link to School of Geometry: https://www.codechef.com/problems/SNUG_FIT
Testcases = int(input())
DiameterTotalArray = list()
DiameterTotal = 0

for index in range(0, Testcases):
    NInputs = int(input())

    LengthInput = input()
    LengthArray = list()
    LengthArray = [int(i) for i in LengthInput.split(' ')]

    WidthInput = input()
    WidthArray = list()
    WidthArray = [int(i) for i in WidthInput.split(' ')]

    LengthArray.sort()
    WidthArray.sort()

    DiameterTotal = 0

    for i in range(0, NInputs):
        if LengthArray[i] < WidthArray[i]:
            DiameterTotal += LengthArray[i]
        else:
            DiameterTotal += WidthArray[i]

    DiameterTotalArray.append(DiameterTotal)

for item in DiameterTotalArray:
    print(item)
