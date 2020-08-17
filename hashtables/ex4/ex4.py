def has_negatives(a):
    #initialize a dict to hold all the numbers
    all_the_nums = dict()
    # init a list to return results
    result = list()
    # for each number in the array
    for num in a:
    # check if the number has a matching number in the dictionary
        if all_the_nums.get(abs(num)):
    # and check if the sum of the two is 0
            if (all_the_nums.get(abs(num)) + num) == 0:
    # if it is append it to the results list
                result.append(abs(num))
    # if no matching number is found make that number the new key
        else:
            all_the_nums[abs(num)] = num

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))