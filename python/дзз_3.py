class Cell:
    def __init__(self, data = None):
        self.prev = None
        self.next = None
        self.data = data

class List:
    def __init__(self):
        self.first = None
        self.last = None
        self.current = None

    def append(self, data):
        cell = Cell(data)
        if self.last == self.first is None:
            self.first = cell
            self.last = cell
        elif self.first is not None:
            self.last.next = cell
            cell.prev = self.last
            self.last = cell

    def l_append(self, data):
        cell = Cell(data)
        if self.first == self.last is None:
            self.first = cell
            self.last = cell
        elif self.last is not None:
            self.first.prev = cell
            cell.next = self.first
            self.first = cell

    # def index_append(self, index, data, counter = 0):
    #     cell = Cell(data)
    #     if self.current is None:
    #         return
    #     else:
    #         if counter < index:
    #             counter += 1
    #             self.current = self.current.next
    #             return self.index_append(index, data, counter)
    #         elif counter > index:
    #             counter -= 1
    #             self.current = self.current.prev
    #             return self.index_append(index, data, counter)
    #         else: # Ошибка тут
    #             cell.prev = self.current.prev
    #             cell.next = self.current
    #             self.current.prev.next = cell
    #             self.current.prev = cell

    def len(self):
        return len(self.list())

    # def r_remove(self):
    #     last = self.last.data
    #     self.last = self.last.prev
    #     self.last.next.prev = None
    #     self.last.next = None
    #     # self.current = self.last
    #     return last
    #
    # def l_remove(self):
    #     first = self.first.data
    #     self.first = self.first.next
    #     self.first.prev.next = None
    #     self.first.prev = None
    #     # self.current = self.first
    #     return first

    # def clear(self):
    #     self.first.next = None
    #     self.last.prev = None
    #     self.last = None
    #     self.first = None

    def list(self, l = []):
        if self.current is None:
            self.current = self.first
            l += [self.first.data]
        else:
            pass
        if self.current.next is None:
            return l
        else:
            self.current = self.current.next
            l += [self.current.data]
            return self.list(l)

    def reverse(self):
        return self.list()[::-1]

    def __getitem__(self, item):
        arr = self.list()
        return arr[item]

    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[-1]
        left = [i for i in arr[:-1] if i < pivot]
        right = [i for i in arr[:-1] if i >= pivot]
        return self.quick_sort(left) + [pivot] + self.quick_sort(right)

    def sort(self):
        return self.quick_sort(self.list())

    def __str__(self):
        return f"{self.list()}"


l1 = List()
l1.append(10)
l1.append(2)
l1.append(4)
l1.l_append(7)
l1.l_append(1)
#l1.index_append(2,3)
print(l1.len())
print(l1)
# print(l1.r_remove())
# print(l1.l_remove())
# print(l1.last.next)
# l1.clear()
print(l1)
print(l1.reverse())
print(l1[2])
print(l1.sort())