#coding=utf-8

import io
import os
import sys
import json

import sys 


if sys.version_info.major == 2:
    from clitool.utils.xmind_sdk.xmind import xmind

    reload(sys) 
    sys.setdefaultencoding('utf-8')
else:
    import xmind
    import importlib 
    importlib.reload(sys)
    sys.setdefaultencoding('utf-8')

from clitool.core.task.behavior.TreeBaseTask import TreeBaseTask

class ExportLuaTreeTask(TreeBaseTask):

    def __init__(self, options):
        super(ExportLuaTreeTask, self).__init__(options)

    def run(self):
        print self._input_path

        all_files = []
        for sub_folder in os.listdir(self._input_path):
            full_path = os.path.join(self._input_path, sub_folder)
            if os.path.isfile(full_path):
                all_files.append({'sub_folder':'', 'full_path':full_path, 'file_name':sub_folder})
            else:
                for file in os.listdir(full_path):
                    full_name = os.path.join(full_path, file)
                    if os.path.isfile(full_name):
                        all_files.append({'sub_folder':sub_folder, 'full_path':full_name, 'file_name':file})
                    else:
                        pass
        
        total = len(all_files)
        self.startProcess(total)
        for i in range(0, total):
            file_dict = all_files[i]

            self.updateProcess(i, 'export ' + file_dict['full_path'])
            lua_content = self._parse_xmind_to_lua_str(file_dict['full_path'])


            self._save_target_file(file_dict['file_name'], file_dict['sub_folder'], lua_content)

        self.finishProcess()

    def _parse_xmind_to_lua_str(self, full_path):
        xmind_obj = xmind.load(full_path)
        json_str = xmind_obj.to_prettify_json()
        json_obj = json.loads(json_str)
        lua_str = self._json_to_lua_str(json_obj[0]['topic'])

        # print lua_str

        lua_content = "local _M = " + lua_str
        lua_content += "\n\n"
        lua_content += "return _M"

        return lua_content

    # 换行跳格
    def _add_tab_str(self, tab):
        lua_str = ''
        for i in range(0,tab):
            lua_str += '    '
        return lua_str

    # 解析note参数转换json对象
    def _str_to_json_data(self, note):
        note = note.replace(' ', '').replace('\r\n', '').replace('\n', '').replace('\r', '').replace('\t', '')

        json_str = '{'
        paramsList = note.split(',')
        data_count = 0
        for i in range(0, len(paramsList)):
            params = paramsList[i].split('=')
            
            if len(params) == 2:
                if data_count > 0:
                    json_str += ','
                
                json_str += '"'
                json_str += params[0]
                json_str += '":'
                json_str += params[1]
                data_count += 1

        json_str += '}'

        # print(json_str)
        # return json.loads('{"args1":1,"args2":2,"args3":"three"}')
        return json.loads(json_str)

    def _json_to_lua_str(self, data, tab = 0):

        if isinstance(data, str) or isinstance(data, bytes) or isinstance(data, unicode):
            data = data.decode('utf-8')
            data = data.lstrip()
            if data[0] == '{':
                data = data.split('//')[0]
                data = data.replace(' ', '').replace('\r\n', '').replace('\n', '').replace('\r', '').replace('\t', '')
                data = data.replace('“', '\'').replace('”', '\'')
                return data
            else:
                return "'" + data + "'"
        elif isinstance(data, bool):
            if data:
                return 'true'
            else:
                return 'false'
        elif isinstance(data, int) or isinstance(data, float):
            return str(data)
        elif isinstance(data, list):
            lua_str = '{'
            for i in range(0, len(data)):
                lua_str += self._json_to_lua_str(data[i], tab + 1)
                lua_str += ','
            lua_str += '\n'
            lua_str += self._add_tab_str(tab)
            lua_str +=  '}'
            return lua_str
        elif isinstance(data, dict):
            lua_str = ''
            lua_str += '\n'
            lua_str += self._add_tab_str(tab)
            lua_str += '{\n'

            for k,v in data.items():
                if v == None:
                    continue

                if type(v) is list and len(v) == 0:
                    continue
                
                # if k == 'note':
                #     v = self._str_to_json_data(v)

                lua_str += self._add_tab_str(tab + 1)
                if type(k) is int:
                    lua_str += '[' + str(k) + ']'
                else:
                    lua_str += k 
                
                lua_str += ' = '

                try:
                    lua_str += self._json_to_lua_str(v, tab + 1)
                    lua_str += ',\n'
    
                except Exception:
                    print('=====================================')
                    print('error in %s %s' % (k,v))
                    print('=====================================')
                    raise
            
            lua_str += self._add_tab_str(tab)
            lua_str += '}'

            return lua_str
        else:
            print('=====================================')
            print('error type : %s' % type(data))
            print('=====================================')
            return None