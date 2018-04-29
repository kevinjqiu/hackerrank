#!/bin/python3


class Heap:
    @staticmethod
    def copy(heap):
        h = Heap(0)
        h.arr = list(heap.arr)
        h.size = heap.size
        return h

    def __init__(self, max_size):
        self.arr = [None] * max_size
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
        self.arr[0] = None
        self.arr[0], self.arr[self.size-1] = self.arr[self.size-1], self.arr[0]
        self.size -= 1
        self.heapify_down(0)
        return retval

    def heapify_down(self, i):
        left_child_index = self.left_child_index(i)
        right_child_index = self.right_child_index(i)

        lcv = None if left_child_index >= self.size else self.arr[left_child_index]
        rcv = None if right_child_index >= self.size else self.arr[right_child_index]

        print(lcv, rcv)
        if lcv is None and rcv is None:
            return

        cnv = self.arr[i]  # current node value
        if lcv is not None and rcv is None:
            if cnv > lcv:
                self.arr[i], self.arr[left_child_index] = self.arr[left_child_index], self.arr[i]
                return self.heapify_down(left_child_index)

        if cnv < lcv and cnv < rcv:
            return

        if lcv > rcv:
            self.arr[i], self.arr[right_child_index] = self.arr[right_child_index], self.arr[i]
            return self.heapify_down(right_child_index)
        else:
            self.arr[i], self.arr[left_child_index] = self.arr[left_child_index], self.arr[i]
            return self.heapify_down(left_child_index)

    def heapify(self, i):
        parent_idx = self.parent_index(i)
        if parent_idx is None:
            return  # top of the heap. we're done

        if self.arr[i] < self.arr[parent_idx]:
            self.arr[i], self.arr[parent_idx] = self.arr[parent_idx], self.arr[i]
            return self.heapify(parent_idx)

        return


heap = Heap(10)
heap.add(1)
heap.add(2)
heap.add(3)

# new_heap = Heap.copy(heap)
# import pdb; pdb.set_trace()  # XXX BREAKPOINT
# if heap.size % 2 == 1:
#     steps = int(heap.size / 2)
#     for _ in range(steps):
#         new_heap.pop()
#     median = new_heap.pop()
# else:
#     steps = int(heap.size / 2) - 1
#     for _ in range(steps):
#         new_heap.pop()
#     left = new_heap.pop()
#     right = new_heap.pop()
#     median = (left + right) / 2
# print('%.1f' % median)

n = int(input().strip())
heap = Heap(n)
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    a.append(a_t)
    heap.add(a_t)

    print(heap.arr)
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
