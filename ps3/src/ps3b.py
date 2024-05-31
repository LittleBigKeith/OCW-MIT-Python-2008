def subStringMatchExact(target, key, offset = 0): 
    if target.find(key, offset) > -1:
        offset = target.find(key, offset)
        start_indices = subStringMatchExact(target, key, offset + 1)
        start_indices = (target.find(key, offset),) + start_indices
        return start_indices
    return ()