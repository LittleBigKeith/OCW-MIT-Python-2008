def countSubStringMatch(target,key):
    start, count = -1, 0
    while True:
        start = target.find(key, start + 1)
        if start == -1:
            return count
        count += 1

def countSubStringMatchRecursive (target, key):
    if target.find(key) > -1 and len(target) > 0:
        count = countSubStringMatchRecursive(target[target.find(key) + 1:], key)
        return count + 1
    return target.find(key) + 1