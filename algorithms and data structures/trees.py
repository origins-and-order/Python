class BinaryTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.l = None
            self.r = None

    def __init__(self):
        self.root = None

    def add_node(self, data):
        if self.root is None:
            self.root = self.Node(data)
        else:
            self.__add_aid__(data, self.root)

    def __add_aid__(self, data, node):
        if data < node.data:
            if node.l is None:
                node.l = self.Node(data)
            else:
                self.__add_aid__(data, node.l)
        else:
            if node.r is None:
                node.r = self.Node(data)
            else:
                self.__add_aid__(data, node.r)

    def get_root(self):
        return self.root

    def prefix_print(self):
        print 'printing prefix...'
        def _print(node):
            if node is not None:
                print node.data
                _print(node.l)
                _print(node.r)
        _print(self.root)

    def infix_print(self):
        print 'printing infix...'
        def _print(node):
            if node is not None:
                _print(node.l)
                print node.data
                _print(node.r)
        _print(self.root)

    def postfix_print(self):
        print 'printing postfix...'
        def _print(node):
            if node is not None:
                _print(node.l)
                _print(node.r)
                print node.data
        _print(self.root)


class Trie:
    class Node:
        def __init__(self):
            self.children = dict()
            self.is_word = False

        def __str__(self):
            return str(self.children) + ' %d' % self.is_word

    def __init__(self):
        self.root = self.Node()

    def add(self, word):
        current_node = self.root
        for i in xrange(len(word)):
            if word[i] not in current_node.children.keys():
                current_node.children[word[i]] = self.Node()
            current_node = current_node.children[word[i]]
        current_node.is_word = True

    def contains_word(self, word):
        current = self.root
        for i in xrange(len(word)):
            if word[i] not in current.children.keys():
                return False
            current = current.children[word[i]]
        return current.is_word

    def remove(self, word):
        current = self.root
        for i in xrange(len(word)):
            current = current.children[word[i]]
        current.is_word = False
