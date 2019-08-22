#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import json
import io
import os
import sys

@click.group()
def main():
    pass

@click.command()
@click.option('-i', '--input-path', required = False, help = u'input_path')
@click.option('-l', '--output-path', required = False, help = u'output_path')
def bt(**options):
    click.echo('Export behavior-tree about the unit.')
    click.echo('Start:')
    from clitool.core.task.behavior.ExportLuaTreeTask import ExportLuaTreeTask
    task = ExportLuaTreeTask(options)
    task.run()
    click.echo('Finish.')

@click.command()
@click.option('--platform', '-p', default = 'all', type = click.Choice(['all', 'ios', 'win32', 'android']), help = u'Select the platform of app')
def cfg(platform):
    """
    The program that parse config files and export config.
    """
    parse_config(platform)

@click.command()
def audio():
    """
    The program that copy audio files to target.
    """
    pass

@click.command()
def ui():
    """
    The program that build and load ui res.
    """
    pass


main.add_command(bt)
main.add_command(cfg)
main.add_command(audio)
main.add_command(ui)


if __name__ == '__main__':
    main()