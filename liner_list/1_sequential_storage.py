#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class seq_storage(object):

    def __init__(self):
        self.data = []
        self.length = 0

    def get_elem(self, i):
        if len(self.data) == 0 or i < 1 or i > len(self.data):
            raise Exception('请输入正确的index或检查线性表是否为空')
        e = self.data[i - 1]
        return e

    def list_insert(self, i, e):
        if i < 1 or i > len(self.data) + 1:
            raise Exception('请输入正确的index')
        if i <= len(self.data):
            for k in range(len(self.data) - 1, i - 2, -1):
                self.data[k + 1] = self.data[k]
        self.data[i - 1] = e
        self.length += 1

    def list_delete(self, i):
        if len(self.data) == 0:
            raise Exception('线性表为空')
        if i < 1 or i > len(self.data):
            raise Exception('请输入正确的index')
        e = self.data[i - 1]
        if i < len(self.data):
            for k in range(i, len(self.data)):
                self.data[k - 1] = self.data[k]
        self.length -= 1
        return e
