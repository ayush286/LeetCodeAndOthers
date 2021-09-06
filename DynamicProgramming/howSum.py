def howSum(targetSum, numbers):
    memo = {}
    return howSumHelper(targetSum, numbers, memo)


def howSumHelper(targetSum, numbers, memo):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for number in numbers:
        remainder = targetSum - number
        remainderResult = howSumHelper(remainder, numbers, memo)
        if remainderResult is not None:
            targetReached = remainderResult
            targetReached.append(number)
            memo[targetSum] = targetReached
            return memo[targetSum]

    memo[targetSum] = None
    return None

if __name__ == '__main__':
    print(howSum(7, [2, 3]))
    print(howSum(7, [2, 4]))
    print(howSum(7, [5, 3, 4, 7]))
    print(howSum(8, [2, 3, 5]))
    print(howSum(300, [7, 14]))
