#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    index = 0

    if length == 1:
        return None

    while index < length:
        hash_table_insert(ht, weights[index], index)
        # print('weights index', weights[index], index)
        index += 1

    """
    YOUR CODE HERE
    """
    for w1 in weights:
        w2 = limit - w1

        w1_idx = hash_table_retrieve(ht, w1)
        w2_idx = hash_table_retrieve(ht, w2)
        if w2_idx:
            if w1 == w2:
                answer = (1, 0)
            else:
                answer = (w2_idx, w1_idx)

            return answer

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
