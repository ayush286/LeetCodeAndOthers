def canSum(array, target):
    if target == 0:
        return False
    memo = canSumHelper(array, target, {}, 0)
    print(memo)
    return memo.get(target)


# O(m*n) Time | O(m)Space where m is length of memo and n is length of array
def canSumHelper(array, target, memo, elem):
    if target in memo or target < 0:
        return memo
    if target == 0:
        memo[elem] = True
        return memo
    for number in array:
        newTarget = target - number
        memo = canSumHelper(array, newTarget, memo, number)
        if newTarget in memo and memo[newTarget]:
            memo[target] = True
            return memo
    if target not in memo:
        memo[target] = False
    return memo


if __name__ == '__main__':
    array = [14, 7]
    target = 300
    print(canSum(array, target))
