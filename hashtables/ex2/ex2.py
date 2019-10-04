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
    #we need our linked pairs to matchup in a way that values always connect to each other, else it will be the first or last stop on our trip
    #loop through ticket
    #check for source= none
     #if yes then this is where our trip will start
     #if not none insert our source and destination to ht
     #loop through the route
     #next route will start with dest from last one(-1)

    """
    for t in tickets:
        if t.source == "NONE":
            route[0] = t.destination
        else:
            hash_table_insert(hashtable, t.source, t.destination)
    for i in range(1, len(tickets)):
        route[i] = hash_table_retrieve(hashtable, route[i-1])
    return route
