def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weight_dict = {}
    one = None
    two = None
    if length < 2:
        return None
    for i in range(length):
        weight_dict[weights[i]] = i
        print("weights", weights)
        print("length", length)
        print("limit", limit)
        print("weight_dict", weight_dict)
        print("weight_dict[weights[i]]", weight_dict[weights[i]])
        print("i", i)
    for i in range(length):
        answer = limit - weights[i]
        print("weights[i]", weights[i])
        # the limit minus the weight at index i is assigned to the variable answer
        if answer in weight_dict:
            # if the difference between the limit and the weights at index i exists as an element of the array weight_dict then we have a match that would inversely make weight_j + weight_k = limit
            one = weight_dict[answer]
            two = i
            result = [one, two]
            print("result", result)
            # result.sort(reverse=True)
            return result[0], result[1]
    return None
