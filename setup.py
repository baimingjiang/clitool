#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
setup(
    name = 'clitool',
    version = '0.1',
    packages = find_packages(),
    include_package_data = True,
    package_data = {
        '': ['*.txt', '*.yaml'],
    },
    install_requires = [
        'Click',
        'colorama',
        'pyyaml',
        'progressbar2'
    ],
    entry_points = '''
        [console_scripts]
        cct=clitool.cmd:main
    ''',
)