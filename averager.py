import math

def findMean(list):
    sum = 0
    for i in list:
        sum += i
    mean = sum/len(list)
    return mean

list1 = [1,6,3,8,5,2,7]
# print('mean', findMean(list1))

def findRange(list):
    highest, lowest = list[1], list[1]
    for i in list:
        if i > highest:
            highest = i
        elif i < lowest:
            lowest = i
    range = highest - lowest
    return range

list2 = [5,6,3,8,5,2,7]
# print('range', findRange(list2))

def findMode(list):
    dict = { }
    for i in list:
        try:
            dict[i] += 1
        except:
            dict[i] = 1
    highest = [next(iter(dict))]
    for i in dict:
        if dict[i] > dict[highest[0]]:
            highest = [i]
        elif dict[i] == dict[highest[0]] and i != highest[0]:
            highest.append(i)
    return highest

list3 = [5,6,5,6,6,3,3]
# print('mode', findMode(list3))

def findMedian(list):
    sorted = 0
    listLen = len(list) - 1
    while sorted == 0:
        correct = 0
        for i in range(listLen):
            if list[i] <= list[i + 1]:
                correct += 1
            else:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
        if correct == listLen:
            sorted = 1
    if len(list) % 2 == 1:
        return list[math.floor(len(list)/2)]
    else:
        return (list[int(len(list)/2)-1] + list[int(len(list)/2)])/2

list4 = [6,3,8,5,2,7,9]
# print('median', findMedian(list4))


list5 = [6,3,8,5,2,7,9,1,6,3,8,5,2,7]
# print(list5)
# print('mean', findMean(list5))
# print('range', findRange(list5))
# print('mode', findMode(list5))
# print('median', findMedian(list5))
