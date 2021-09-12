
# purple [purp, p, ur, le, purpl] -> [[purp, le], [p, ur, p, le]]
def allConstruct(target, wordBank):
    if target == "":
        return [[]]
    combinations = None
    for word in wordBank:
        if isPrefixWord(word, target):
            newTarget = target[len(word):]
            suffixWays = allConstruct(newTarget, wordBank)
            targetWays = suffixWays.copy()
            targetWays = [combo + [word] for combo in suffixWays]
            if combinations is None:
                combinations = targetWays
            else:
                combinations += targetWays
    if combinations is None:
        return []
    return combinations


def isPrefixWord(word, target):
    if len(word) > len(target):
        return False
    prefix = target[:len(word)]
    return prefix == word

if __name__ == '__main__':
    # print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
    print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))