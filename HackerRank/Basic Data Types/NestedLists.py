##Given the names and grades for each student in a Physics class of  students,
##store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
##https://www.hackerrank.com/challenges/nested-list

if __name__ == '__main__':
    nameScoreList = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nameScoreList.append([score, name])

    nameScoreList.sort()
    firstKey = nameScoreList[0]
    minVal = firstKey[0]
    secondMinVal = minVal
    for sublist in nameScoreList:
        if(sublist[0] > minVal):
            secondMinVal = sublist[0]
            break

    nameList = list()
    for sublist in nameScoreList:
        if (sublist[0] == secondMinVal):
            nameList.append(sublist[1])

    nameList.sort()
    for name in nameList:
        print(name)


