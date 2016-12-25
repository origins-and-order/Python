# this is the dictionary container
words = set(word.strip() for word in open('new_dictionary.txt').readlines())


def neighbors(word):
    """
        This function returns a list of words that differ by one letter from the
        word given and that are from the dictionary (words).
        e.g. neighbors('zero') => ['aero', 'hero']
    """

    # we must construct a new word from our given word,
    # for each character in the word you will replace it with each letter
    # in the alphabet and check if that new word exists in your 'words' set
    # and note that it must not be the same word you passed in
    for index in range(len(word)):

        # create a temporary word here to replace a letter at a time with
        # all letters of the alphabet

        # convert the word you passed in to a list of characters and set that
        # to your temporary variable each time before the inner for loop iteration
        # note, strings are immutable which means you can not assign a
        # character to a specific index.
        # e.g. list('Hello') => ['H', 'e', 'l', 'l', 'o']
        # now 'word' is a list of characters and this is mutable or "assignable"

        tmp_word = list(word)

        # now to iterate through the alphabet with ascii values
        for i in range(26):
            tmp_word = list(tmp_word)
            # lowercase a's ascii value is 97
            # replace the current index of the temporary word with each letter

            # 'chr()' takes in a int and maps it to the ascii character
            # associated with that value
            # e.g. chr(97) => 'a'
            tmp_word[index] = chr(97+i)

            # now we must convert the list of characters back to a string
            # we can do so by using the join method from the string class
            # e.g ''.join(['H', 'e', 'l', 'l', 'o']) => 'Hello'
            tmp_word = ''.join(tmp_word)

            # now we must check if the new constructed word is in our
            # dictionary we read in and also check if the new word is not the
            # original word we passed in, if so add it to your neighboring words
            # list

            if tmp_word in words and tmp_word != word:
                yield tmp_word


def find_path(start, end):
    """
    This function returns the path from start to end.
    e.g. find_path('zero', 'five') => ['zero', 'hero', 'here', 'fere', 'fire', 'five']
    """
    # return empty list if word sizes dont match
    if len(start) != len(end):
        return []

    # implement breadth first search O(|V| + |E|)
    # create queue (list) and enqueue starting word (append)
    q = list()
    q.append(start)

    # keep track of "parent" words, start has not parent since its our starting
    # word
    visited = {start: ''}

    # keep track if we found "end"
    found = False

    # while there are elements in the queue
    while q and not found:
        # "pop" the first word from the queue and set equal a variable called word
        word = q.pop(0)

        # for each of the neighboring words of word
        for neighbor in neighbors(word):

            # check if neighbor has been visited if not,
            # keep track of its parent and add it to the queue
            if neighbor not in visited:
                visited[neighbor] = word
                q.append(neighbor)
                # we found end, break the outer loop
                if neighbor == end:
                    found = True
                    break

    # there exists a path between start and end
    # now to backtrack to starting word
    if found:
        path = [end]
        while path[-1] is not start:
            path.append(visited[path[-1]])
        return path[::-1]  # reversed from end to start
    else:
        return []  # no path was found

print ' => '.join(find_path('feather', 'compute'))
