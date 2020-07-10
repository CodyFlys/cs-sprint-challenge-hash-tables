def has_negatives(a):
    cache = {}
    result = []

    # loop over all nums in a
    for num in a:
        # check if num is greater than 0
        if num > 0:
            # if it is we cache it and set the value = None
            cache[num]=None
    # loop over all nums in a
    for num in a:
        # check if num is less than 0
        if num < 0:
            # if it's less than 0 let's check if num-num-num aka the negative number
            # but positive is IN the cache we cached earlier.
            if num - num - num in cache:
                # if it is we can set the VALUE to True
                cache[num - num - num] = True
                # print(cache)
    # loop over all items in the cache
    for item in cache:
        # check if the item's VALUE is TRUE
        if cache[item] == True:
            # if it is true we append it to the result array and return it
            result.append(item)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
