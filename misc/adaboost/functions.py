from math import log, exp


def thresholds(x, y):
    for i in xrange(len(y) - 1):
        if y[i] is not y[i+1]:
            yield [x[i], x[i+1]]


def calculate_threshold_error(threshold, y, weight):
    d = dict()
    d[calculate_threshold_error_left(threshold, y, weight)] = 0
    d[calculate_threshold_error_right(threshold, y, weight)] = 1
    return [min(d.keys()), d[min(d.keys())]]


def calculate_threshold_error_left(threshold, y, weight):
    error = 0
    for i in xrange(len(y)):
        if i < sum(threshold)/float(2):
            if y[i] is not 1:
                error += weight[i]
        else:
            if y[i] is not -1:
                error += weight[i]

    return error


def calculate_threshold_error_right(threshold, y, weight):
    error = 0
    for i in xrange(len(y)):
        if i > sum(threshold)/float(2):
            if y[i] is not 1:
                error += weight[i]
        else:
            if y[i] is not -1:
                error += weight[i]

    return error


def find_best_threshold(ts, y, weight):
    d = dict()
    for threshold in ts:
        if calculate_threshold_error(threshold, y, weight) not in d.keys():
            d[calculate_threshold_error(threshold, y, weight)[0]] = threshold

    return d[min(d.keys())]


def calculate_mislabeled_indices(threshold, y, side):
    if side is 0:
        return calculate_mislabeled_indices_left(threshold, y)
    else:
        return calculate_mislabeled_indices_right(threshold, y)


def calculate_mislabeled_indices_left(threshold, y):
    l = list()
    print 'threshold: ' + str(sum(threshold)/float(2))
    for i in xrange(len(y)):
        if i < sum(threshold)/float(2):
            if y[i] is not 1:
                l.append(1)
            else:
                l.append(0)
        else:
            if y[i] is not -1:
                l.append(1)
            else:
                l.append(0)
    return l


def calculate_mislabeled_indices_right(threshold, y):
    l = list()
    print 'threshold: ' + str(sum(threshold)/float(2))
    for i in xrange(len(y)):
        if i > sum(threshold)/float(2):
            if y[i] is not 1:
                l.append(1)
            else:
                l.append(0)
        else:
            if y[i] is not -1:
                l.append(1)
            else:
                l.append(0)
    return l


def classifier_weight(e):
    return log((1-e)/e)/2
