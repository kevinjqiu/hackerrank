#!/bin/python3
import array


class Heap:
    @staticmethod
    def copy(heap):
        h = Heap(0)
        h.arr = array.array('i', heap.arr)
        h.size = heap.size
        return h

    def __init__(self, max_size):
        self.arr = array.array('i', [-1] * max_size)
        self.size = 0

    def parent_index(self, i):
        if i == 0:
            return None  # root node
        return int((i - 1) / 2)

    def left_child_index(self, i):
        return 2 * i + 1

    def right_child_index(self, i):
        return 2 * i + 2

    def add(self, data):
        self.arr[self.size] = data
        self.size += 1
        self.heapify(self.size-1)

    def pop(self):
        retval = self.arr[0]
        self.arr[0] = -1
        self.arr[0], self.arr[self.size-1] = self.arr[self.size-1], self.arr[0]
        self.size -= 1
        self.heapify_down(0)
        return retval

    def swap(self, i, j):
        """Swap arr at i and j
        """
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def min(self, a, b):
        idx_a, val_a = a
        idx_b, val_b = b
        if val_a > val_b:
            return idx_b, val_b
        else:
            return idx_a, val_a

    def heapify_down(self, i):
        lci = self.left_child_index(i)
        rci = self.right_child_index(i)

        lcv = -1 if lci >= self.size else self.arr[lci]
        rcv = -1 if rci >= self.size else self.arr[rci]

        cnv = self.arr[i]  # curent node value
        if rcv != -1:
            # both left child and right child exist
            min_idx, min_val = self.min((lci, lcv), (rci, rcv))
            if min_val < cnv:
                self.swap(i, min_idx)
                return self.heapify_down(min_idx)
        else:
            if lcv != -1:
                if lcv < cnv:
                    self.swap(i, lci)
                    return self.heapify_down(lci)

    def heapify(self, i):
        parent_idx = self.parent_index(i)
        if parent_idx is None:
            return  # top of the heap. we're done

        if self.arr[i] < self.arr[parent_idx]:
            self.swap(i, parent_idx)
            return self.heapify(parent_idx)


n = int(input().strip())
heap = Heap(n)
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)
    heap.add(a_t)

    new_heap = Heap.copy(heap)
    if heap.size % 2 == 1:
        steps = int(heap.size / 2)
        for _ in range(steps):
            new_heap.pop()
        median = new_heap.pop()
    else:
        steps = int(heap.size / 2) - 1
        for _ in range(steps):
            new_heap.pop()
        left = new_heap.pop()
        right = new_heap.pop()
        median = (left + right) / 2
    print('%.1f' % median)
