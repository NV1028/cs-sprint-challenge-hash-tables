def intersection(arrays):

    """
    YOUR CODE HERE
    Goal:
        *given multiple arrays, find all the numbers that are the same in them
    Limits: 
        * There can be up to 10 lists in the list of lists.
        * The lists can contain up to roughly 1,000,000 elements each.
    """

    # create a dictionary with key being the number and the value being the count
    counter = dict()
    # create an array to hold the intersection numbers
    result = []

    #loop through the arrays list
    for i, array in enumerate(arrays):
        # and loop through each list
        for num in array:
        # if the item already has been put in the dictionary and the index is more than one, increase the counter
            if counter.get(num) != None and i > 0:
        # we make num the key, and increase the current value by one
                counter[num] = counter[num] + 1
        # else if there is no entry with that number and index is 1 (meaning we're still looking at the first array)
            elif counter.get(num) is None and i == 0:
        #set the initial count to 1
                counter[num] = 1
            else:
                continue

        # loop over each dictionary entry
        for item in counter:
        # if the number count is equal to the array length
            if counter[item] == len(arrays):
        # we append that to the num
                result.append(item)


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))