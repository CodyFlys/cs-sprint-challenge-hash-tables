def get_indices_of_item_weights(weights, length, limit, cache={}):
    # Count through the length of weights and get the index
    for index in range(len(weights)):
        # for every index we're caching the weight and index of that weight as index.
        cache[weights[index]] = index
    # Count through the length of weights and get the index
    for index in range(len(weights)):
        # set a variable called lw as the limit - the weights index
        lw = limit-weights[index]
        # and then we check if that is in the cache
        if lw in cache:
            # if it is we're going to return the max index and cached lw along with the min
            return (max(index, cache[lw]), min(index, cache[lw]))
    return None