#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class LinkedStorage(object):
    class Node(object):
        def __init__(self, element, nex):
            self.element = element
            self.nex = nex

    def __init__(self):

        self.size = 0
        # 头结点
        self.head_node = self.Node(None, None)
        # 头指针
        self.head = self.head_node

    def show_list(self):
        print(self.head_node.nex.element, end=' ')
        print(self.head_node.nex.nex.element, end=' ')

    def get_elem(self, i):
        pass

    def list_insert(self, i, e):

        j = 1
        p = self.head_node
        while (p.nex and (j < i)):
            p = p.nex
            j += 1
        if ((p == None) or (j > i)):
            raise Exception('...')

        s = self.Node(e, p.nex)
        p.nex = s
        self.size += 1

    def list_delete(self, i):
        pass

    def get_length(self):
        return self.size


if __name__ == '__main__':
    l = LinkedStorage()
    l.list_insert(1, 'a')
    l.list_insert(2, 'b')
    l.show_list()
    print(l.get_length())
