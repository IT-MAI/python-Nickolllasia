from random import randint

# Узел связного списка
class Node:
    def __init__(self, data = None):
        # Ссылка на предыдущего соседа
        self.prev = None
        # Ссылка на последующего соседа
        self.next = None
        # Содержимое узла
        self.data = data


# Двунаправленный связный список
class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.current = None

    def is_empty(self):
        return self.first is None

    # Добавить узел в конец списка
    def push_back(self, data):
        # Шаг 1: Создаём узел списка
        node = Node(data)
        # Шаг 2: Добавляем узел к списку
        # Шаг 2.1: Если узлов нету, то создаём его
        if self.is_empty():
            self.first = node
            self.last = node
        # Шаг 2.2: Если хотя бы один узел есть, то привязываем к последнему
        else:
            # Записываем в последний узел ссылку на новый (в качестве следующего)
            self.last.next = node
            # Записываем в новый узел ссылку на последний (в качестве предыдущего)
            node.prev = self.last
            # Обновляем ссылку на последний узел
            self.last = node
    
    # Добавляем узел в начало списка (по аналогии с добавлением в конец)
    def push_front(self, data):
        node = Node(data)
        if self.is_empty():
            self.first = node
            self.last = node
        else:
            self.first.prev = node
            node.next = self.first
            self.first = node

    # Добавляем узел по индексу
    def index_push(self, index, data, counter = 0):
        # Шаг 1: создаём узел
        node = Node(data)
        # Шаг 2: Если начинается с нуля, то ссылку на текущий узел берем с ссылки на первый узел (счёт с первого элемента)
        if counter == 0:
            self.current = self.first
        # Рекурсивно двигаясь по соседм, однажды мы придем к ссылке на None
        if self.current is None:
            return
        else:
            # Шаг 3: с помощью счётчика фиксируем как далеко мы ушли от начала (на какой индекс)
            # и вызываем следующего соседа по рекурсии
            if counter < index:
                counter += 1
                self.current = self.current.next
                return self.index_push(index, data, counter)
            elif counter > index:
                counter -= 1
                self.current = self.current.prev
                return self.index_push(index, data, counter)
            # Шаг 4: Если мы на подходящем индексе, то меняем ссылки на соседей
            else:
                prev = self.current.prev
                next = self.current
                node.prev = prev
                prev.next = node
                node.next = next
                next.prev = node

    # Используя встроенный метод измерения длины находим длину списка
    def len(self):
        return len(self.list([]))

    # Удаляем поледний элемент списка
    def back_remove(self):
        # Записываем ссылку на последний элемент
        last = self.last.data
        # Обновляем ссылку на последний элемент
        self.last = self.last.prev
        # Удалям ссылки с последнего на предыдущий и с предыдущего на последний элементы
        self.last.next.prev = None
        self.last.next = None
        return last

    # Удаляем узел с начала списка
    # По аналогии удаляем связи и обновляем ссылку, только уже на первый узел
    def front_remove(self):
        first = self.first.data
        self.first = self.first.next
        self.first.prev.next = None
        self.first.prev = None
        return first

    # Очищаем элементы
    # Для этого нужно, чтобы к списку нельзя было бы обратиться.
    def clear(self):
        # Значит, удаляем ссылки
        self.first.next = None
        self.last.prev = None
        self.last = None
        self.first = None

    # Функция, которая нужна для перевод цепи из соседей в удобный для чтения список
    def list(self, l=[]):
        if self.is_empty():
            return []
        else:
            pass
            # Если это начало списка, то давайте сошлём указатель текущего элемента на первый
        if l == []:
            self.current = self.first
            # И запишем значеие в список
            l += [self.first.data]
        # Если последующий узел - None (ничего), то пора заканчивать функцию и выводить список
        if self.current.next is None:
            return l
        else:
            # Иначе, перейдём к последующему члену и добавим его
            self.current = self.current.next
            l += [self.current.data]
            # И вызовем функцию от изменённого списка "l"
            return self.list(l)

    # Чтобы перевернуть список, воспользуюсь срезом, изменив шаг
    def reverse(self):
        return self.list([])[::-1]
    
    # Функция для получения инекса списка
    def __getitem__(self, item):
        # Перевожу список в обычный питоновский список
        arr = self.list([])
        # И возвращаю индекс этого списка
        return arr[item]

    # Быстрая сортировка, которую использует компьютер
    def quick_sort_for_computer(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[-1]
        left = [i for i in arr[:-1] if i < pivot]
        right = [i for i in arr[:-1] if i >= pivot]
        return self.quick_sort_for_computer(left) + [pivot] + self.quick_sort_for_computer(right)

    # Сортировка, которую вызывает пользователь
    def sort(self):
        return self.quick_sort_for_computer(self.list([]))

    # Возвратим читаемый для пользователя список
    def __str__(self):
        return f"{self.list([])}"


l1 = DoublyLinkedList()
l1.push_back(10)
l1.push_back(2)
l1.push_back(4)
l1.push_back(7)
l1.push_front(1)
print(l1)
l1.index_push(2,3)
print(l1.len())
print(l1)
print(l1.back_remove())
print(l1)
print(l1.front_remove())
print(l1)
l1.clear()
print(l1)

l1.push_back(10)
l1.push_back(8)
l1.push_back(9)
print(l1.reverse())
print(l1[2])
print(l1.sort())