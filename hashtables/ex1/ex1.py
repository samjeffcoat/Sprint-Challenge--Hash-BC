#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    #weight is going to be our weights at i
    # weigh_limit is limit_weight
    # retrieve our weight_limit and set it as index_pair
    # if index_pair is  not none and higher than i it will be  index_pair first else it will be i first.  Return our blob once we get order correct
    insert into hash table.
    """
    for i in range(length):
        weight = weights[i]
        weight_limit = limit - weight
        index_pair = hash_table_retrieve(ht, weight_limit)
        if index_pair is not None:
            blob = (index_pair, i) if i < index_pair else(i, index_pair)
            return blob
        hash_table_insert(ht, weight, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
