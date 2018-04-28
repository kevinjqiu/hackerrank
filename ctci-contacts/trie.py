class Node:
    def __init__(self, ch=None, parent=None):
        self.parent = parent
        self.ch = ch
        self.size = 0
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
        node.size += 1
        if len(chars) == 0:
            node.children.append(Node("*"))
            return
        first_char, rest_chars = chars[0], chars[1:]
        child_node = self._find_node_with_ch(first_char, node.children)
        if child_node is None:
            child_node = Node(first_char, parent=node)
            node.children.append(child_node)
        return self._add(rest_chars, child_node)

    def add(self, name):
        self._add(name, self.root)

    def _find(self, chars, nodes):
        if len(nodes) == 0:
            return 0
        if len(chars) == 0:
            return nodes[0].parent.size
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
