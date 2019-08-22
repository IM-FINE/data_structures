#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class LinkedStorage(object):
    class Node(object):
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.size = 0
        # 头结点self.Node(None, None) 、头指针(头节点的内存地址)self.head_node
        self.head_node = self.Node()

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

    def create_list_head(self, n):
        # 单链表的整表创建(头插法)
        for i in range(n):
            p = self.Node()  # 生成一个新的节点
            p.data = round(random.random(), 2)
            p.next = self.head_node.next  # 将新节点指向头节点的下一个节点(即指向第一个节点)
            self.head_node.next = p  # 将头节点指向新节点
            self.size += 1

    def create_list_tail(self, n):
        # 单链表的整表创建(尾插法)
        r = self.head_node  # r指向尾结点
        for i in range(n):
            p = self.Node()  # 生成一个新节点
            p.data = round(random.random(), 2)
            r.next = p  # 将新节点位于尾结点之后
            r = p  # r指向新的尾结点
            self.size += 1


if __name__ == '__main__':
    l = LinkedStorage()
    # l.list_insert(1, 'a')
    # l.list_insert(2, 'b')
    # l.list_insert(3, 'c')
    # l.show_list()
    # print(l.get_elem(3))
    # print(l.list_delete(2))
    # l.show_list()
    l.create_list_tail(20)
    l.show_list()
