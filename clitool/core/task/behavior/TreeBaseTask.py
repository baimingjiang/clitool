#coding=utf-8

import sys
import os
import io

if sys.version_info.major == 2:
    from clitool.utils.xmind_sdk.xmind import xmind
else:
    import xmind

from clitool import utils

from clitool.core.base.BaseTask import BaseTask

class TreeBaseTask(BaseTask):

    _project_path = None
    _input_path = None
    _output_path = None

    def __init__(self, options):
        super(TreeBaseTask, self).__init__(options)
        print("TreeBaseTask")
        self._project_path = utils.getConfig('project.path')
        self._input_path = utils.getConfig('unit_design_path')
        self._output_path = utils.getConfig('project.unit_out')

    def _save_target_file(self, file_name, sub_folder, lua_content):
        out_name = os.path.splitext(file_name)[0]
        out_ext = ".lua"

        out_folder = os.path.join(self._project_path, self._output_path, sub_folder, "script")

        # 去除首位空格
        out_folder = out_folder.strip()
        # 去除尾部 \ 符号
        out_folder = out_folder.rstrip("\\")

        if not os.path.exists(out_folder):
            os.makedirs(out_folder)

        out_full_path = os.path.join(out_folder, out_name + out_ext)

        with io.open(out_full_path, "w", encoding = "utf-8") as f:
            f.write(lua_content)

