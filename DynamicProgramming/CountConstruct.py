def isWordInTarget(word, target):
    if len(word) > len(target):
        return False
    subTarget = target[:len(word)]
    return subTarget == word

# O(n*m * m) Time | O(m^2) Space where m is length of target and n is length of wordBank
def countConstruct(target, wordBank, memo={}):
    if target in memo:
        return memo[target]
    if len(target) == 0:
        return 1
    count = 0
    for word in wordBank:
        if isWordInTarget(word, target):
            newTarget = target[len(word):]
            numberOfWays = countConstruct(newTarget, wordBank, memo)
            count += numberOfWays
    memo[target] = count
    return count
if __name__ == '__main__':
    # print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef"]))
    # print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    # print(countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))
