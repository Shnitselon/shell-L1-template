#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.layer_one.core.command_executor import CommandExecutor
from {{cookiecutter.project_slug}}.driver_commands import DriverCommands


class DriverCommandExecutor(CommandExecutor):
    """
    Mrv command executor
    """

    def __init__(self, logger):
        super(DriverCommandExecutor, self).__init__(logger)
        self._driver_instance = DriverCommands(logger)

    def driver_instance(self):
        """
        Instance of the driver commands
        :return:
        :rtype: {{cookiecutter.project_slug}}.DriverCommands
        """
        return self._driver_instance
