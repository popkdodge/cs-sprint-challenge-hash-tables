def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    #store a key value parie of weight and index
    wi_dic = {}
    #create a list of combindation of weight subtract from limit
    possible_combination = [[limit-weight, index] for index, weight in enumerate(weights)]
    #add weight and index key value pairs
    for index, weight in enumerate(weights):
        wi_dic[weight] = index
    for combination in possible_combination:
        if combination[0] in wi_dic:
            return [wi_dic[combination[0]], combination[1]]

