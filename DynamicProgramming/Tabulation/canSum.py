# O(m*n) Time | O(m)Space where m is length of memo and n is length of array
def canSum(array, target):
    canSums = [False for number in range(target + 1)]
    canSums[0] = True
    for index in range(len(canSums)):
        if canSums[index]:
            for number in array:
                indexToModify = index + number
                if indexToModify < len(canSums):
                    canSums[indexToModify] = True
    return canSums[target]


if __name__ == '__main__':
    array = [14, 7]
    target = 300
    print(canSum(array, target))
