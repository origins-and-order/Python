# Hw 4 - implement Adaboost
# Machine Learning
# Dustin Ramsey Torres

from functions import *


x = [0, 1, 2,  3,  4,  5, 6, 7, 8,  9]
y = [1, 1, 1, -1, -1, -1, 1, 1, 1, -1]

# initialize starting probabilities
probabilities = [[1/float(len(x)) for _ in xrange(len(x))]]

M = 3

for i in xrange(M):

    ts = thresholds(x, y)
    t = find_best_threshold(ts, y, probabilities[i])
    e = calculate_threshold_error(t, y, probabilities[i])
    cw = classifier_weight(e[0])

    print 'E' + str(i+1) + ': ' + str(e[0])
    print 'a' + str(i+1) + ': ' + str(cw)
    print 'qi = {} for wrong, {} for right'.format(exp(cw), exp(-cw))

    update_probabilities = list()

    for t, j in enumerate(calculate_mislabeled_indices(t, y, e[1])):

        pre_p = None

        if j is 0:  # for correct
            pre_p = exp(-cw) * probabilities[i][t]
        else:
            pre_p = exp(cw) * probabilities[i][t]

        update_probabilities.append(pre_p)

    z = sum(update_probabilities)

    print update_probabilities

    # new probabilities
    for j in enumerate(update_probabilities):
        update_probabilities[j[0]] /= float(z)

    print 'Z' + str(i+1) + ': ' + str(z)
    
    print update_probabilities

    probabilities.append(update_probabilities)

    print
