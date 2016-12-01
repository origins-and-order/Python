# cycle detection
def cyclic(g):

    # create table to store incoming edge count
    incoming_degree = {vertex: 0 for vertex in g.keys()}

    for vertex in g.keys():
        for neighbor in g[vertex]:
            incoming_degree[neighbor] += 1
            # since neighbor is in vertex's neighbors list,
            # neighbor must have a incoming edge

    # if there are no 0 incoming degree edges, then the graph is cyclic
    return 0 not in incoming_degree.values()


# sort nodes based on incoming degree
def topological_sort(g):

    # create table to store incoming edge count
    incoming_degree = {vertex: 0 for vertex in g.keys()}

    # O(|V| + |E|)
    for vertex in g.keys():
        for neighbor in g[vertex]:
            incoming_degree[neighbor] += 1
            # since neighbor is in vertex's neighbors list,
            # neighbor must have a incoming edge

    # store order of how vertices are visited
    visited = list()

    # O(|V| + |E|)
    while incoming_degree:

        # get smallest value
        smallest_in_degree = min(incoming_degree.values())

        # find key from value
        vertex = incoming_degree.keys()[incoming_degree.values().index(smallest_in_degree)]

        # add to list of visited
        visited.append(vertex)

        # update incoming edge degrees for vertex's neighbors
        for neighbor in g[vertex]:
            incoming_degree[neighbor] -= 1

        # remove vertex from the table
        del incoming_degree[vertex]

    return visited


# calculate shortest path distance from source to all other nodes in the graph
def dijkstra(g, source):

    # assume the cost to each node other than the source is infinity
    costs = {v: float('inf') for v in g.keys()}

    # the cost to the source from the source is 0
    costs[source] = 0

    # for visited nodes in the graph
    visited = set()

    # while there are unknown nodes left in the graph, -1 because the source is known
    while len(visited) < len(g.keys()) - 1:
        # select the unknown node N with the lowest cost, first iteration source
        vertex = costs.keys()[costs.values().index(min(costs[key] for key in costs.keys() if key not in visited))]
        visited.add(vertex)

        for neighbor in g[vertex].keys():
            # If N's cost + cost of(N, X)) < X's cost
            if costs[vertex] + g[vertex][neighbor] < costs[neighbor]:
                # X's cost = N's cost + cost of(N, X)
                costs[neighbor] = costs[vertex] + g[vertex][neighbor]

    return costs


# O(|V| + |E|)
def breadth_first_search(g, source):

    # create queue
    q = list()

    # enqueue source
    q.append(source)

    # create set of visited nodes
    visited = set()

    # while Q not empty
    while q:

        # get first node from the queue
        vertex = q.pop(0)

        # visit vertex's neighbors
        for neighbor in g[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)


# O(|V| + |E|)
def depth_first_search(g, source):

    # create stack
    s = list()

    # push source
    s.append(source)

    # create set of visited nodes
    visited = set()

    # while S not empty
    while s:
        # get last node from the stack
        vertex = s.pop(-1)
        # visit vertex's neighbors
        for neighbor in g[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                s.append(neighbor)
