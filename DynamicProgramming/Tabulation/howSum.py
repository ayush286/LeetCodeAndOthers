def howSum(targetSum, numbers):
    howSums = [None for number in range(targetSum + 1)]
    howSums[0] = []
    for index in range(len(howSums)):
        if howSums[index] is not None:
            for number in numbers:
                if index + number < len(howSums):
                    currentHowSum = howSums[index] + number


if __name__ == '__main__':
    print(howSum(7, [2, 3]))
    print(howSum(7, [2, 4]))
    print(howSum(7, [5, 3, 4, 7]))
    print(howSum(8, [2, 3, 5]))
    print(howSum(300, [7, 14]))