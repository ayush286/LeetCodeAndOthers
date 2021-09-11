def isWordInTarget(word, target):
    if len(word) > len(target):
        return False
    subTarget = target[:len(word)]
    return subTarget == word


# Brute force without memo
# O(n^m * m) Time | O(m^2) Space where m is length of target and n is length of wordBank
# After memoization
# O(n*m * m) Time | O(m^2) Space where m is length of target and n is length of wordBank
def canConstructHelper(target, wordBank, memo):
    if target in memo:
        return
    if len(target) == 0:
        return True
    else:
        for word in wordBank:
            if isWordInTarget(word, target):
                newTarget = target[len(word):]
                isConstructable = canConstructHelper(newTarget, wordBank, memo)
                if isConstructable:
                    memo[target] = True
                    return True
                else:
                    memo[target] = False
    memo[target] = False
    return


def canConstruct(target, wordBank):
    memo = {}
    canConstructHelper(target, wordBank, memo)
    return memo[target]


if __name__ == '__main__':
    print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))
