#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.layer_one.core.driver_commands_interface import DriverCommandsInterface


class DriverCommands(DriverCommandsInterface):
    """
    Driver commands implementation
    """

    def __init__(self, logger):
        """
        :param logger: 
        """
        self._logger = logger

    def get_state_id(self):
        pass

    def set_state_id(self, state_id):
        pass

    def map_bidi(self, src_port, dst_port):
        pass

    def map_uni(self, src_port, dst_port):
        pass

    def get_resource_description(self, address):
        pass

    def map_clear(self, ports):
        pass

    def login(self, address, username, password):
        pass

    def map_clear_to(self, src_port, dst_port):
        pass

    def get_attribute_value(self, cs_address, attribute_name):
        pass

    def set_attribute_value(self, cs_address, attribute_name, attribute_value):
        pass

    def map_tap(self, src_port, dst_port):
        return self.map_uni(src_port, dst_port)
