from multiprocessing import Pool


class Node:
    def __init__(self, ch=None):
        self.ch = ch
        self.children = []

    def __str__(self):
        return '<ch=%s, children=%s>' % (self.ch, self.children)

    __repr__ = __str__


class Trie:
    def __init__(self):
        self.root = Node()

    def __str__(self):
        return str(self.root)

    def _find_node_with_ch(self, ch, nodes):
        for child_node in nodes:
            if ch == child_node.ch:
                return child_node
        return None

    def _add(self, chars, node):
        if len(chars) == 0:
            node.children.append(Node("*"))
            return
        first_char, rest_chars = chars[0], chars[1:]
        child_node = self._find_node_with_ch(first_char, node.children)
        if child_node is None:
            child_node = Node(first_char)
            node.children.append(child_node)
        return self._add(rest_chars, child_node)

    def add(self, name):
        self._add(name, self.root)

    def _num_words_at_node(self, node):
        if node is None:
            return 0

        if node.ch == '*':
            return 1

        return sum(map(self._num_words_at_node, node.children))

    def _find(self, chars, nodes):
        if len(nodes) == 0:
            return 0
        if len(chars) == 0:
            return sum(map(self._num_words_at_node, nodes))
        first_char, rest_chars = chars[0], chars[1:]
        node = self._find_node_with_ch(first_char, nodes)
        if node is None:
            return 0
        return self._find(rest_chars, node.children)

    def find(self, partial):
        return self._find(partial, self.root.children)


t = Trie()


n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        t.add(contact)
        continue
    if op == 'find':
        result = t.find(partial=contact)
        print(result)
        continue
    else:
        break
