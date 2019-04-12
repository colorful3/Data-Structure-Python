# -*- coding: utf8 -*-
"""
从底层自己实现的动态数组
"""
__author__ = 'Colorful'
__date__ = '2018/11/3 下午5:22'


class Array:

    def __init__(self, lst=None, capacity=10):
        if isinstance(lst, list):
            self._data = lst[:]
            self._size = len(lst)
            return
        self._data = [None] * capacity
        self._size = 0

    """
    获取数组中的元素个数
    """
    def get_size(self):
        return self._size

    """
    获取数组的容量
    """
    def get_capacity(self):
        return len(self._data)

    """
    返回数组是否为空
    """
    def is_empty(self):
        return self._size == 0

    """
    向所有元素后添加一个新的元素
    """
    def add_last(self, e):
        self.add(self._size, e)

    """
    向所有元素后前添加一个新的元素
    """
    def add_first(self, e):
        self.add(0, e)

    """
    在第index个元素插入一个新元素e
    :param index int 插入位置
    :param e 要插入的元素
    """
    def add(self, index, e):
        if index < 0 or index > self._size:
            raise ValueError('Add failed. Require index >=0 and index <= size.')
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        for i in range(self._size - 1, index - 1, -1):
            self._data[i + 1] = self._data[i]
        self._data[index] = e
        self._size += 1

    """
    获取index索引位置的元素
    :param index 索引位置
    """
    def get(self, index):
        if index < 0 or index >= self._size:
            raise ValueError("Get failed. Index is illegal.")
        return self._data[index]

    """
    获取数组中最后一个索引位置的元素
    """
    def get_last(self):
        return self.get(self._size - 1)

    """
    获取数组中第一个索引位置的元素
    """
    def get_first(self):
        return self.get(0)

    """
    修改index索引位置的元素为e
    :param index int 索引位置
    :param e 要修改的元素
    """
    def set(self, index: int, e):
        if index < 0 or index >= self._size:
            raise ValueError("Get failed. Index is illegal.")
        self._data[index] = e

    """
    查找数组中是否有元素e
    :param e 要查找的元素
    :return boolean
    """
    def contains(self, e):
        for index in range(self._size):
            if self._data[index] == e:
                return True
        return False

    """
    查找数组中元素e所在的索引，如果不存在元素e，则返回-1
    :param e 要查询的元素
    """
    def find(self, e):
        for index in range(self._size):
            if self._data[index] == e:
                return index
        return -1

    """
    从数组中删除index位置的元素，返回删除的元素
    :param index int 要删除的位置索引
    """
    def remove(self, index: int):
        if index < 0 or index >= self._size:
            raise ValueError("remove failed. Index is illegal.")

        ret = self._data[index]
        for pos in range(index + 1, self._size):
            self._data[pos - 1] = self._data[pos]
        self._size -= 1
        self._data[self._size] = None
        if self._size == len(self._data) // 4 and len(self._data) // 2 != 0:
            self._resize(len(self._data) // 2)
        return ret

    """
    删除数组中的第一个元素
    """
    def remove_first(self):
        return self.remove(0)

    """
    删除数组中的最后一个元素
    """
    def remove_last(self):
        return self.remove(self._size - 1)

    """
    从数组中删除元素e(删除一个)
    :param e 要删除的元素
    """
    def remove_element(self, e):
        index = self.find(e)
        if index != -1:
            self.remove(index)

    """
    动态增加或减少数组容量
    :param new_capacity int 新数组的容量
    """
    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data

    def __str__(self):
        return "Array: size = {}, capacity = {} \n {}".format(self._size, self.get_capacity(), self._data[:self._size])

    __repr__ = __str__


if __name__ == "__main__":
    arr = Array()
    for x in range(10):
        arr.add_last(x)
    print(arr)

    arr.add(1, 100)
    print("use function add")
    print(arr)

    arr.add_first(-1)
    print("use function addFirst")
    print(arr)

    print("use function get")
    print(arr.get(5))

    arr.set(1, 1)
    print("use function set")
    print(arr)

    print("Use function contains\n", arr.contains(1))

    print("use function find\n", arr.find(101))

    arr.remove(2)
    print("use function remove\n", arr)

    arr.remove_first()
    print("use function removeFirst\n", arr)

    arr.remove_last()
    print("use function removeLast\n", arr)

    print(arr)

    arr.remove_element(4)
    print("use function removeElement\n", arr)

    arr.remove_last()
    arr.remove_last()
    arr.remove_last()
    print("Test resize Array\n", arr)

    arr.add_first(500)
    arr.add_first(501)
    arr.add_first(502)
    arr.add_first(503)
    arr.add_first(504)
    arr.add_first(505)
    print("Test resize Array\n", arr)
