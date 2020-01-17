#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    num = 0
    source = ""
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
        # find the first source
        if ticket.source is "NONE":
            source = ticket.destination

    while num < length-1:
        route[num] = source
        num = num+1
        route[num] = hash_table_retrieve(hashtable, source)
        source = route[num]

    return route
