def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    b = {}
    result = []
    for number in a:
        b[number] = -number
    for number in a:
        if -number in b:
            if number > 0:
                result.append(number)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
