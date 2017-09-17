from graphs import *


# unweighted graphs

g = {'a': ['b','f'],
     'f': ['a'],
     'b': ['a','e','c'],
     'c': ['b','d'],
     'd': ['c', 'e'],
     'e': ['b', 'd']}


f = {'a': ['b','f'],
     'f': ['a'],
     'b': ['a','e'],
     'c': ['d'],
     'd': ['c', 'e'],
     'e': ['b', 'd']}


h = {'a': ['b'],
     'f': ['b'],
     'b': ['a','e','f','c'],
     'c': ['b'],
     'e': ['b']}


j = {'a': 'b',
     'b': 'c',
     'c': 'a'}


k = {'a': ['b'],
     'b': ['c','d'],
     'c': ['d'],
     'd': []}

m = {'a': ['b'],
     'b': ['a']}


unweighted_graphs = {'g': g,
                     'f': f,
                     'h': h,
                     'j': j,
                     'k': k,
                     'm': m}

# g is cyclic
# f is cyclic
# h is cyclic
# k is not cyclic
# j is cyclic
# m is cyclic

for graph in unweighted_graphs:

    if cyclic(unweighted_graphs[graph]):
        print graph + ' is cyclic'
    else:
        print graph + ' is not cyclic'


weighted_g = {'a': {'b': 2, 'c': 1},
              'b': {'c': 1},
              'c': {'a': 9, 'd': 8, 'e': 2},
              'd': {'a': 3},
              'e': {'d': 3}}
