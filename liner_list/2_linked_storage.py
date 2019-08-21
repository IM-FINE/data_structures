#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class LinkedStorage(object):
    class Node(object):
        def __init__(self, data, next):
            self.data = data
            self.next = next

    def __init__(self):

        self.size = 0
        # 头结点
        self.head_node = self.Node(None, None)
        # 头指针(头节点的内存地址)
        # self.head_pointer = self.head_node

    def show_list(self):
        for i in range(1, self.size + 1):
            if i == self.size:
                print(self.get_elem(i))
            else:
                print(self.get_elem(i), end=' ')

    def get_elem(self, i):
        p = self.head_node.next
        j = 1
        while p and (j < i):
            p = p.next
            j += 1
        if (p is None) or (j > i):
            return f'{i}位置节点不存在'
        return p.data

    def list_insert(self, i, e):

        j = 1
        p = self.head_node
        while (p.next and (j < i)):
            p = p.next
            j += 1
        if (p is None) or (j > i):
            raise Exception('...')

        s = self.Node(e, p.next)
        p.next = s
        self.size += 1

    def list_delete(self, i):
        p = self.head_node
        j = 1
        while (p.next) and (j < i):
            p = p.next
            j += 1
        if (not p.next) or (j > i):
            return f'{i}位置节点不存在'
        q = p.next
        p.next = q.next
        self.size -= 1
        return q.data

    def get_length(self):
        return self.size


if __name__ == '__main__':
    l = LinkedStorage()
    l.list_insert(1, 'a')
    l.list_insert(2, 'b')
    l.list_insert(3, 'c')
    l.show_list()
    print(l.get_elem(3))
    print(l.list_delete(2))
    l.show_list()
