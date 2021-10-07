def bestSum(target, numbers):
    memo = {}
    return bestSumHelper(target, numbers, memo)


# O(n*m^2) Time | O(m^2) Space where n is target value and m is length of numbers array
def bestSumHelper(target, numbers, memo):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    shortestCombination = None
    for number in numbers:
        remainder = target - number
        # remainderResult returns array or None
        remainderResult = bestSumHelper(remainder, numbers, memo)
        if remainderResult is not None:
            # if you don't use copy, python makes it point to the same list, which messes the whole code and my 4 hours
            combination = remainderResult.copy()
            combination.append(number)
            if shortestCombination is not None:
                if len(shortestCombination) > len(combination):
                    shortestCombination = combination
            else:
                shortestCombination = combination
    memo[target] = shortestCombination
    return shortestCombination


if __name__ == '__main__':
    print(bestSum(7, [5, 3, 4, 7]))
    print(bestSum(8, [2, 3, 5]))
    print(bestSum(2, [1]))
    print(bestSum(100, [1, 2, 5, 25]))
