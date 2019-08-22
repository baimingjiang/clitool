# CLITool 使用说明

### 安装pip

+ 检查安装pip是否安装

```
    打开命令行工具, 执行 `pip -V`, 如果显示pip版本说明已经有pip, 直接执行后面的内容。
```

+ 安装pip

```
    1. 到https://pip.pypa.io/en/latest/installing/#python-os-support下载get-pip.py
    2. 执行 python get-pip.py
    3. 添加环境变量：这个路径是pip.exe所在路径，一般在python的安装目录下，python\scripts

```

### 安装mtool库

+ 更新CLITool最新

        git pull

+ 安装CLITool

        切换到CLITool目录, 执行
        pip install .

+ 卸载CLITool

        pip uninstall cct

### 项目配置

```
    1. 复制CLITool目录下config.example.yaml为config.yaml
    2. 重新安装：pip install .
    3. 参数配置：TODO
    
```

### 调用方式

    打开终端，执行 `cct`

### 使用示例

1. 导出配置

    	cct cfg

2. 导出行为树

        cct bt