#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    ticket_hm = {}
    for ticket in tickets:
        ticket_hm[ticket.source] = ticket.destination

    route = []
    for i in range(length):
        if i == 0:
            route.append(ticket_hm["NONE"])
        else:
            route.append(ticket_hm[route[i-1]])
    return route
