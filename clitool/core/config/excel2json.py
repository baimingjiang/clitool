#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
excel中的配置格式说明
第一行为配表说明
第二行为key

脚本会根据每列内容判定当前列的类别。如果有','则为List类型，如果不是数字则为string类型，如果有浮点数则为float类型，否则为int类型
'''

import xlrd,glob,os,sys,json,codecs,math,shutil
import optparse
from progressbar import *

SKIP_COUNT = 2;# 忽略的表头行数

reload(sys)
sys.setdefaultencoding( "utf-8" )

def isInt(value):
    try:
        f = float(value);
        if math.floor(f) == f:
            return True;
        else:
            return False;
    except:
        return False;
    return True;

def isFloat(value):
    if isInt(value):
        return False;
    try:
        a = float(value)
    except:
        return False;
    return True;

def isNumber(value):
    try:
        a = float(value)
    except:
        return False;
    return True

def isString(value):
    if isNumber(value):
        return False
    return type(value) is str or type(value) is unicode

def checkType(array):
    hasArrayInt = False;
    hasArrayFloat = False;
    hasArrayString = False;
    hasString = False;
    hasFloat = False;
    hasInt = False;

    i = 0
    for value in array:
        i += 1;
        if i <= SKIP_COUNT:
            continue;

        if len(str(value)) <= 0:
            continue;

        if isString(value):
            if value.find(',') != -1:
                strlist = value.split(',')
                for s in strlist:
                    hasString2 = False;
                    hasFloat2 = False;
                    if isString(s):
                        hasString2 = True;
                    elif isFloat(s):
                        hasFloat2 = True;
                if hasString2:
                    hasArrayString = True;
                elif hasFloat2:
                    hasArrayFloat = True;
                else:
                    hasArrayInt = True;
            else:
                hasString = True;
        elif isFloat(value):
            hasFloat = True;

    if hasArrayString:
        return 'List<string>'
    elif hasArrayFloat:
        return 'List<float>'
    elif hasArrayInt:
        return 'List<int>'
    elif hasString:
        return 'string';
    elif hasFloat:
        return 'float';
    else:
        return 'int'

#字符串特殊字符处理
def formatString(str):
    charList = ['"']
    for char in charList:
        str = str.replace('\\'+char, char)
        str = str.replace(char, '\\'+char)
    return str
        
def getValue(value, flag):
    if type(value) == str:
        value = value.strip()

    if value == None or value == '' or value == ' ':
        return None

    if flag == 'int' or flag == 'long':
        return int(value)
    elif flag == 'float':
        return value;
    elif flag == 'List<int>':
        strlist = str(value).replace('.0','').split(',');
        return '[' + ','.join(strlist) + ']'
    elif flag == 'List<float>':
        strlist = str(value).split(',')
        return '[' + ','.join(strlist) + ']'
    elif flag == 'List<string>':
        strlist = str(value).split(',')
        valuelist = []
        for each in strlist:
            each = formatString(each)
            valuelist.append('"' + each + '"')
        return '[' + ','.join(valuelist) + ']'
    elif flag == 'string':
        if isInt(value):
            return '"' + formatString(str(int(value))) + '"'
        return '"' + formatString(str(value)) + '"'
    elif flag == 'mark':
        return None
    else:
        if isInt(value):
            return '"' + str(int(value)) + '"'
        else:
            return '"' + formatString(str(value)) + '"'

def getKey(key):
    key = str(key)
    return key.replace(' ', '_').replace('-', '_').replace('#', '')
    
#获取说明里面默认的数据类型
def getDefaultType(comment):
    if not comment or comment == "":
        return None
    str1 = '(dataType:'
    pos1 = comment.find(str1)
    if pos1<0:
        return None
    pos2 = comment.find(')', pos1)
    if pos2<0:
        return None
    type = comment[pos1+len(str1):pos2]
    if type in ['List<string>','List<float>','List<int>','string','float','int','mark']:
        return type
    return None

def convertSheet(target_path, sheet, basename):
    if sheet.nrows <= 0:
        return

    comments = sheet.row_values(0)
    keys = sheet.row_values(1)

    # 没有任何数据
    if sheet.nrows <= SKIP_COUNT:
        return

    exports = []
    for i in range(len(keys)):
        data = sheet.col_values(i)
        type = getDefaultType(comments[i])
        if type==None:
            type = checkType(data)
        exports.append({'row' : i, 'key' : getKey(keys[i]), 'type' : type})

    fileData = []
    fileData.append('{\n')

    cols = sheet.col_values(0);         # 第一列为key列，决定了有多少条目
    count = len(cols)
    for i in range(SKIP_COUNT, count): 
        if len(str(sheet.cell(i, 0).value)) <= 0:
            continue

        id = cols[i]
        if isInt(id)==True:
            id = int(id)
        fileData.append('\t"'+str(id)+'": ')    #添加第一列为id值
        values = [];
        for item in exports:
            v = getValue(sheet.cell(i, item['row']).value, item['type'])
            if v != None:
                values.append('"{0}":{1}'.format(item['key'], v))

        if i == count - 1:
            #最后一行没有逗号
            fileData.append('{{ {0} }}\n'.format(', '.join(values)))
        else:
            fileData.append('{{ {0} }},\n'.format(', '.join(values)))

    fileData.append('}')

    filename = basename + '.json'
    saveJsonFile(target_path, filename, fileData)

def saveJsonFile(target_path, filename, fileData):
    filename = os.path.basename(filename)
    filename = os.path.join(target_path, filename)
    file_dir = os.path.dirname(filename)
    if not os.path.exists(file_dir) or not os.path.isdir(file_dir):
        os.makedirs(file_dir)

    fp = open(filename, 'w')
    fp.writelines(fileData)
    fp.close()


def convertToJson(target_path, file):
    excel = xlrd.open_workbook(file)
    sheets = excel.sheets()
    basename = os.path.splitext(file)[0]
    convertSheet(target_path, sheets[0], basename)

def doConvert(source_path, target_path):
    for root,dirs,files in os.walk(source_path):
        process = 0
        file_count = len(files)

        widgets = ['Progress: ', Percentage(), ' ', Bar('#'),' ', FileTransferSpeed()]  
        pbar = ProgressBar(widgets = widgets, maxval = 10 * file_count).start()
        
        for file in files:
            pbar.update(10 * process + 1)
            process += 1
            if file.find('.xls') != -1 and file.find('~$') == -1:
                fullPath = os.path.join(root, file)
                convertToJson(target_path, fullPath)
        pbar.finish()

def parse_config(platform):

    source_path = gl_config["configDir"]

    print '[excel2json] SOURCE_PATH: ', source_path
    
    dstDir = gl_config["project_path"]

    platformDic = {"win32": "res/config/", "ios": "resIOS/config/", "android": "resAndroid/config/"}

    if platformDic.has_key(platform):
        target_path = os.path.join(dstDir, platformDic[platform])
        print "\n\n[excel2json] ========================convert " + platform + " config========================"
        print "[excel2json] TARGET_PATH: " + target_path + "\n"
        doConvert(source_path, target_path)
    else:
        for k,v in platformDic.items():
            target_path = os.path.join(dstDir, v)
            print "\n\n[excel2json] ========================convert " + k + " config========================"
            print "[excel2json] TARGET_PATH: " + target_path + "\n"
            doConvert(source_path, target_path)

    print '\n[excel2json]========================convert config over========================'
    print "\n\n\n"
    sys.exit(0)

