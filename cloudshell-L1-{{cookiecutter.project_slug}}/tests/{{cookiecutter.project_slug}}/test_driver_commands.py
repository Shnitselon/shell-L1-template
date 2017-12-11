from unittest import TestCase

from mock import Mock

from {{cookiecutter.project_slug}}.driver_commands import DriverCommands


class TestDriverCommands(TestCase):
    def setUp(self):
        self._logger = Mock()
        self._instance = DriverCommands(self._logger)
