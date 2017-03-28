##Find the Second Largest Number in a List
##https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arrToList = list(arr)
    arrToList.sort()
    largestElement = arrToList[arrToList.__len__()-1]
    returnVal = largestElement
    for secondLargestElement in arrToList:
        if(secondLargestElement < largestElement):
            returnVal = secondLargestElement
    print(returnVal)


