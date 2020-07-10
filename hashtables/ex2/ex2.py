#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length, cache={}):
    # set route to be empty * length for quicker run time
    route = [None] * length
    # loop through the tickets inside of the tickets
    for ticket in tickets:
        # for each ticket cache the ticket.source as the key and the destination as the value
        # [None, PDX] for example key, value
        cache[ticket.source] = ticket.destination
    # Set nextlocation to the DESTINATION of the starting point.
    nextLocation = cache["NONE"]
    # loop over the length and get each index of the tickets
    for index in range(0, length):
        # for each index set the route at that index to be the nextLocation variable
        route[index] = nextLocation
        # Set the next location to the VALUE of the current airport, which is the next one.
        nextLocation = cache[nextLocation]
        # again basically Key, value
    return route