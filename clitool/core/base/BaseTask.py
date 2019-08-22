#coding=utf-8

import time
import logging

from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer, AdaptiveETA, AbsoluteETA, AdaptiveTransferSpeed

from clitool.core.base.BaseObject import BaseObject

class BaseTask(BaseObject):

    _pbar = None
    _log = None

    def __init__(self, options):
        super(BaseTask, self).__init__(options)
        logging.basicConfig(level=logging.DEBUG)

        self._log = logging.getLogger()

    def __start(self):
        pass

    def __finish(self, error):
        pass

    def __run(self):
        pass

    def run(self):
        self.__start()
        try:
            self.__run()
            self.__finish(0)
        except Exception:
            self.__finish(-1)

    def startProcess(self, total):
        widgets = [
            'Process ', Bar(),
            ' ', Percentage(),
            ' ', Timer()
        ]
        self._pbar = ProgressBar(widgets = widgets, max_value = total, redirect_stderr = True, redirect_stdout = True).start()
        
    def updateProcess(self, cur, msg):
        # self._log.info(msg)
        print(msg)
        self._pbar.update(cur + 1)
        time.sleep(0.5)

    def finishProcess(self):
        self._pbar.finish()
