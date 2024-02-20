from copy import deepcopy

# Split the dataset into individual sets
def splitList(list):
    listToReturn = []
    for subList in list:
        length = len(subList)
        if length == 1:
            listToReturn.append(subList)
        else:
            LHS = splitList([subList[:len(subList)//2]])
            RHS = splitList([subList[len(subList)//2:]])
            for currentList in LHS: listToReturn.append(currentList)
            for currentList in RHS: listToReturn.append(currentList)
    return listToReturn


# Merge two lists
def merge(list1, list2):
    newList = []
    for _ in range(len(list1) + len(list2)):
        if list1 and list2:
            if list1[0] > list2[0]:
                newList.append(list1.pop(0))
            else:
                newList.append(list2.pop(0))
        elif list1:
            newList.append(list1.pop(0))
        else:
            newList.append(list2.pop(0))
    return newList

# Merge all of the lists in the set merge sort fashion
def fullMerge(importedLists):
    lists = deepcopy(importedLists)
    while len(lists) > 1:
        mergedList = []
        while lists:
            if len(lists) > 1:
                mergedList.append(merge(lists.pop(0), lists.pop(0)))
            else:
                mergedList.append(lists.pop(0))
        for currentList in mergedList: lists.append(currentList)
    return lists

exampleList = [[6,2,9,4,1,5,8,3,7]]

splitLists = splitList(exampleList)

mergeSortedList = fullMerge(splitLists)

print("example list:", exampleList)
print("\nsplit lists:", splitLists)
print("\nmerge sorted list:", mergeSortedList)