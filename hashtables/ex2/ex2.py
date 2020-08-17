#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    # make a dictionary to hold routes
    routes_dict = dict()
    # make a list to store the route
    route = list()

    #loop through the tickets
    for ticket in tickets:
    # and make the source be the key in the dict and the destination the value
        routes_dict[ticket.source] = ticket.destination
    # make and set and index to 0
    index = 0
    # set the current destination to be None to get started
    cur_dest = "NONE"

    # while there are tickets
    while index < length:
    # set the cur destination to the new source for the next loop
        cur_dest = routes_dict.get(cur_dest)
    # on each loop through append the ordered routes from first to last
        route.append(cur_dest)
    # move on to the next loop through
        index += 1

    return route