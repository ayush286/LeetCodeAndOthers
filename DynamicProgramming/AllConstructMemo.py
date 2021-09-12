
# O(n^m) Time | O(m) Space, where m is length of target and n is length of wordBank
# Since output is too large, we don't include it into our complexity for Space
def allConstruct(target, wordBank, memo={}):
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]
    combinations = None
    for word in wordBank:
        if isPrefixWord(word, target):
            newTarget = target[len(word):]
            suffixWays = allConstruct(newTarget, wordBank)
            targetWays = suffixWays.copy()  # save yourself tears of joy
            targetWays = [combo + [word] for combo in targetWays]
            if combinations is None:
                combinations = targetWays
            else:
                combinations += targetWays
    if combinations is None:
        memo[target] = []
        return []
    memo[target] = combinations
    return combinations


def isPrefixWord(word, target):
    if len(word) > len(target):
        return False
    prefix = target[:len(word)]
    return prefix == word

if __name__ == '__main__':
    # print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
    # print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
    # print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]))
