from random import randint
import math
from io import StringIO


class MyPriorityQueue:
    """
        Max Heap
        Use List as the underlying data structure
        for node i in the List, the 2i+1 is the left child, and 2i+2 is the right child
        
        Bineray Tree: parent is the max(min) among its children
    """

    def __init__(self, arr: list[int] = None):
        if arr is None:
            self.arr = []
        else:
            self.arr = arr
        self.build_heap()

    def __len__(self):
        return len(self.arr)

    def heapify(self, idx):
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < len(self) and self.arr[left] > self.arr[largest]:
            largest = left
        if right < len(self) and self.arr[largest] < self.arr[right]:
            largest = right

        if largest != idx:  # need to swap
            self.arr[idx], self.arr[largest] = self.arr[largest], self.arr[idx]
            self.heapify(largest)

    def build_heap(self):
        for i in range(len(self) // 2 - 1, -1, -1):  # from leaf node to root
            self.heapify(i)

    def insert(self, n: int):
        self.arr.append(n)
        self.build_heap()

    def get_max(self):
        return self.arr[0]

    def extract_max(self):
        max_val = self.arr[0]

        self.arr = self.arr[1:]
        self.arr[0], self.arr[len(self) - 1] = self.arr[len(self) -
                                                        1], self.arr[0]
        self.heapify(0)

        return max_val

    def increase_key(self, idx: int, new_val: int):
        if new_val < self.arr[idx]:
            raise ValueError("new_val must be greater than current value")
        self.arr[idx] = new_val

        while idx > 0 and self.arr[idx] > self.arr[
            (idx - 1) // 2]:  # remain the max heap to the root
            self.arr[idx], self.arr[(idx - 1) // 2] = \
            self.arr[(idx - 1) // 2], self.arr[idx] # swap
            idx = (idx - 1) // 2

    def insert(self, new_val: int):
        self.arr.append(new_val - 1)
        self.increase_key(len(self) - 1, new_val)

    def delete(self, num):
        idx = 0
        for idx in range(len(self)):
            if self.arr[idx] == num:
                break
        if self.arr[idx] != num:
            raise ValueError("num not found")

        self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
        self.arr = self.arr[:-1]
        self.build_heap()

    def show_tree(self, total_width=80, fill=' '):
        """
        Pretty-print a tree.
        total_width depends on your input size
        source https://bit.ly/38HXSoU  
        """
        output = StringIO()
        last_row = -1
        for i, n in enumerate(self.arr):
            if i:
                row = int(math.floor(math.log(i + 1, 2)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = 2**row
            col_width = int(math.floor((total_width * 1.0) / columns))
            output.write(str(n).center(col_width, fill))
            last_row = row
        print(output.getvalue())
        print('-' * total_width)
        return


if __name__ == "__main__":

    p_queue = MyPriorityQueue()
    for i in range(10):
        p_queue.insert(randint(-100, 100))
    p_queue.insert(11)
    p_queue.show_tree()

    p_queue.delete(11)
    p_queue.show_tree()

    q1 = MyPriorityQueue([1, 2, 4, 0, -1, 2, 1])
    q1.show_tree()
