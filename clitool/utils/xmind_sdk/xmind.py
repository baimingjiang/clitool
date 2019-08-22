#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .core.loader import WorkbookLoader
from .core.saver import WorkbookSaver

class xmind(object):
    @classmethod
    def load(self, path):
        loader = WorkbookLoader(path)
        return loader.get_workbook()

    @classmethod
    def save(self, workbook, path=None):
        saver = WorkbookSaver(workbook)
        saver.save(path)
