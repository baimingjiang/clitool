#coding=utf-8

from clitool import utils

from clitool.core.base.BaseTask import BaseTask

class ConfigBaseTask(BaseTask):

    _input_path = None
    _output_path = None

    def __init__(self, options):
        super(ConfigBaseTask, self).__init__(options)

        self._input_path = utils.getConfig("config_path")
        self._project_path = utils.getConfig("project_path")

        self._output_path = utils.getConfig("behavior_out_path")