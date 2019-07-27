#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class SeqStorage(object):

    def __init__(self, MAXSIZE):
        """
        初始化线性表
        :param MAXSIZE:
        """
        self.MAXSIZE = MAXSIZE
        self.data = [None] * self.MAXSIZE
        self.length = 0

    def show_list(self):
        print(self.data)

    def get_elem(self, i):
        """
        获取对应位置的元素
        :param i:
        :return:
        """
        if self.length == 0 or i < 1 or i > self.length:
            raise Exception('请输入正确的index或检查线性表是否为空')
        e = self.data[i - 1]
        return e

    def list_insert(self, i, e):
        """
        在i位置插入元素e
        :param i:
        :param e:
        :return:
        """
        if self.length == self.MAXSIZE:
            raise Exception('线性表长度已达到最大')
        if i < 1 or i > self.length + 1:
            raise Exception('请输入正确的index')
        if i <= self.length:
            for k in range(self.length - 1, i - 2, -1):
                self.data[k + 1] = self.data[k]
        self.data[i - 1] = e
        self.length += 1

    def list_delete(self, i):
        """
        删除i位置元素并返回
        :param i:
        :return:
        """
        e = self.data[i - 1]
        if self.length == 0:
            raise Exception('线性表为空')
        if i < 1 or i > self.length:
            raise Exception('请输入正确的index')
        if i == self.length:
            self.data[i - 1] = None
        if i < self.length:
            for k in range(i, self.length):
                self.data[k - 1] = self.data[k]
            self.data[self.length - 1] = None
        self.length -= 1
        return e


if __name__ == '__main__':
    s = SeqStorage(20)
    s.list_insert(1, 10)
    s.list_insert(2, 11)
    s.list_insert(2, 12)
    s.list_insert(3, 14)

    print(s.length)
    s.show_list()

    s.list_delete(3)
    s.show_list()
    s.list_delete(3)
    s.show_list()
