def intersection(arrays):
    # make a empty cache
    cache={}
    # set length to be the length of the arrays so 3
    length = len(arrays)
    # empty var for result
    result = []
    # set a counter at 1
    counter = 1
    # for each list in the arrays list
    for eachList in arrays:
        # (dive deeper) for each ITEM in eachList (we're now in each list)
        for item in eachList:
            # check if the item is not in cache
            if item not in cache:
                # if it's not in cache, cache item as counter
                cache[item] = counter
            # else we count up if it is already in the cache
            else:
                cache[item] += 1
    # loop over each number in cache
    for each in cache:
        # check if the number == length because if it does we know 
        # it's occured the requested amount of times
        if cache[each] == length:
            # append to results since we know it's our number
            result.append(each)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
