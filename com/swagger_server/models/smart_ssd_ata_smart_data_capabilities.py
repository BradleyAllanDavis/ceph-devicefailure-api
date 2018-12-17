# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SmartSsdAtaSmartDataCapabilities(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, values: List[int]=None, exec_offline_immediate_supported: bool=None, offline_is_aborted_upon_new_cmd: bool=None, offline_surface_scan_supported: bool=None, self_tests_supported: bool=None, conveyance_self_test_supported: bool=None, selective_self_test_supported: bool=None, attribute_autosave_enabled: bool=None, error_logging_supported: bool=None, gp_logging_supported: bool=None):  # noqa: E501
        """SmartSsdAtaSmartDataCapabilities - a model defined in Swagger

        :param values: The values of this SmartSsdAtaSmartDataCapabilities.  # noqa: E501
        :type values: List[int]
        :param exec_offline_immediate_supported: The exec_offline_immediate_supported of this SmartSsdAtaSmartDataCapabilities.  # noqa: E501
        :type exec_offline_immediate_supported: bool
        :param offline_is_aborted_upon_new_cmd: The offline_is_aborted_upon_new_cmd of this SmartSsdAtaSmartDataCapabilities.  # noqa: E501
        :type offline_is_aborted_upon_new_cmd: bool
        :param offline_surface_scan_supported: The offline_surface_scan_supported of this SmartSsdAtaSmartDataCapabilities.  # noqa: E501
        :type offline_surface_scan_supported: bool
        :param self_tests_supported: The self_tests_supported of this SmartSsdAtaSmartDataCapabilities.  # noqa: E501
        :type self_tests_supported: bool
        :param conveyance_self_test_supported: The conveyance_self_test_supported of this SmartSsdAtaSmartDataCapabilities.  # noqa: E501
        :type conveyance_self_test_supported: bool
        :param selective_self_test_supported: The selective_self_test_supported of this SmartSsdAtaSmartDataCapabilities.  # noqa: E501
        :type selective_self_test_supported: bool
        :param attribute_autosave_enabled: The attribute_autosave_enabled of this SmartSsdAtaSmartDataCapabilities.  # noqa: E501
        :type attribute_autosave_enabled: bool
        :param error_logging_supported: The error_logging_supported of this SmartSsdAtaSmartDataCapabilities.  # noqa: E501
        :type error_logging_supported: bool
        :param gp_logging_supported: The gp_logging_supported of this SmartSsdAtaSmartDataCapabilities.  # noqa: E501
        :type gp_logging_supported: bool
        """
        self.swagger_types = {
            'values': List[int],
            'exec_offline_immediate_supported': bool,
            'offline_is_aborted_upon_new_cmd': bool,
            'offline_surface_scan_supported': bool,
            'self_tests_supported': bool,
            'conveyance_self_test_supported': bool,
            'selective_self_test_supported': bool,
            'attribute_autosave_enabled': bool,
            'error_logging_supported': bool,
            'gp_logging_supported': bool
        }

        self.attribute_map = {
            'values': 'values',
            'exec_offline_immediate_supported': 'exec_offline_immediate_supported',
            'offline_is_aborted_upon_new_cmd': 'offline_is_aborted_upon_new_cmd',
            'offline_surface_scan_supported': 'offline_surface_scan_supported',
            'self_tests_supported': 'self_tests_supported',
            'conveyance_self_test_supported': 'conveyance_self_test_supported',
            'selective_self_test_supported': 'selective_self_test_supported',
            'attribute_autosave_enabled': 'attribute_autosave_enabled',
            'error_logging_supported': 'error_logging_supported',
            'gp_logging_supported': 'gp_logging_supported'
        }

        self._values = values
        self._exec_offline_immediate_supported = exec_offline_immediate_supported
        self._offline_is_aborted_upon_new_cmd = offline_is_aborted_upon_new_cmd
        self._offline_surface_scan_supported = offline_surface_scan_supported
        self._self_tests_supported = self_tests_supported
        self._conveyance_self_test_supported = conveyance_self_test_supported
        self._selective_self_test_supported = selective_self_test_supported
        self._attribute_autosave_enabled = attribute_autosave_enabled
        self._error_logging_supported = error_logging_supported
        self._gp_logging_supported = gp_logging_supported

    @classmethod
    def from_dict(cls, dikt) -> 'SmartSsdAtaSmartDataCapabilities':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SmartSsd_ata_smart_data_capabilities of this SmartSsdAtaSmartDataCapabilities.  # noqa: E501
        :rtype: SmartSsdAtaSmartDataCapabilities
        """
        return util.deserialize_model(dikt, cls)

    @property
    def values(self) -> List[int]:
        """Gets the values of this SmartSsdAtaSmartDataCapabilities.


        :return: The values of this SmartSsdAtaSmartDataCapabilities.
        :rtype: List[int]
        """
        return self._values

    @values.setter
    def values(self, values: List[int]):
        """Sets the values of this SmartSsdAtaSmartDataCapabilities.


        :param values: The values of this SmartSsdAtaSmartDataCapabilities.
        :type values: List[int]
        """

        self._values = values

    @property
    def exec_offline_immediate_supported(self) -> bool:
        """Gets the exec_offline_immediate_supported of this SmartSsdAtaSmartDataCapabilities.


        :return: The exec_offline_immediate_supported of this SmartSsdAtaSmartDataCapabilities.
        :rtype: bool
        """
        return self._exec_offline_immediate_supported

    @exec_offline_immediate_supported.setter
    def exec_offline_immediate_supported(self, exec_offline_immediate_supported: bool):
        """Sets the exec_offline_immediate_supported of this SmartSsdAtaSmartDataCapabilities.


        :param exec_offline_immediate_supported: The exec_offline_immediate_supported of this SmartSsdAtaSmartDataCapabilities.
        :type exec_offline_immediate_supported: bool
        """

        self._exec_offline_immediate_supported = exec_offline_immediate_supported

    @property
    def offline_is_aborted_upon_new_cmd(self) -> bool:
        """Gets the offline_is_aborted_upon_new_cmd of this SmartSsdAtaSmartDataCapabilities.


        :return: The offline_is_aborted_upon_new_cmd of this SmartSsdAtaSmartDataCapabilities.
        :rtype: bool
        """
        return self._offline_is_aborted_upon_new_cmd

    @offline_is_aborted_upon_new_cmd.setter
    def offline_is_aborted_upon_new_cmd(self, offline_is_aborted_upon_new_cmd: bool):
        """Sets the offline_is_aborted_upon_new_cmd of this SmartSsdAtaSmartDataCapabilities.


        :param offline_is_aborted_upon_new_cmd: The offline_is_aborted_upon_new_cmd of this SmartSsdAtaSmartDataCapabilities.
        :type offline_is_aborted_upon_new_cmd: bool
        """

        self._offline_is_aborted_upon_new_cmd = offline_is_aborted_upon_new_cmd

    @property
    def offline_surface_scan_supported(self) -> bool:
        """Gets the offline_surface_scan_supported of this SmartSsdAtaSmartDataCapabilities.


        :return: The offline_surface_scan_supported of this SmartSsdAtaSmartDataCapabilities.
        :rtype: bool
        """
        return self._offline_surface_scan_supported

    @offline_surface_scan_supported.setter
    def offline_surface_scan_supported(self, offline_surface_scan_supported: bool):
        """Sets the offline_surface_scan_supported of this SmartSsdAtaSmartDataCapabilities.


        :param offline_surface_scan_supported: The offline_surface_scan_supported of this SmartSsdAtaSmartDataCapabilities.
        :type offline_surface_scan_supported: bool
        """

        self._offline_surface_scan_supported = offline_surface_scan_supported

    @property
    def self_tests_supported(self) -> bool:
        """Gets the self_tests_supported of this SmartSsdAtaSmartDataCapabilities.


        :return: The self_tests_supported of this SmartSsdAtaSmartDataCapabilities.
        :rtype: bool
        """
        return self._self_tests_supported

    @self_tests_supported.setter
    def self_tests_supported(self, self_tests_supported: bool):
        """Sets the self_tests_supported of this SmartSsdAtaSmartDataCapabilities.


        :param self_tests_supported: The self_tests_supported of this SmartSsdAtaSmartDataCapabilities.
        :type self_tests_supported: bool
        """

        self._self_tests_supported = self_tests_supported

    @property
    def conveyance_self_test_supported(self) -> bool:
        """Gets the conveyance_self_test_supported of this SmartSsdAtaSmartDataCapabilities.


        :return: The conveyance_self_test_supported of this SmartSsdAtaSmartDataCapabilities.
        :rtype: bool
        """
        return self._conveyance_self_test_supported

    @conveyance_self_test_supported.setter
    def conveyance_self_test_supported(self, conveyance_self_test_supported: bool):
        """Sets the conveyance_self_test_supported of this SmartSsdAtaSmartDataCapabilities.


        :param conveyance_self_test_supported: The conveyance_self_test_supported of this SmartSsdAtaSmartDataCapabilities.
        :type conveyance_self_test_supported: bool
        """

        self._conveyance_self_test_supported = conveyance_self_test_supported

    @property
    def selective_self_test_supported(self) -> bool:
        """Gets the selective_self_test_supported of this SmartSsdAtaSmartDataCapabilities.


        :return: The selective_self_test_supported of this SmartSsdAtaSmartDataCapabilities.
        :rtype: bool
        """
        return self._selective_self_test_supported

    @selective_self_test_supported.setter
    def selective_self_test_supported(self, selective_self_test_supported: bool):
        """Sets the selective_self_test_supported of this SmartSsdAtaSmartDataCapabilities.


        :param selective_self_test_supported: The selective_self_test_supported of this SmartSsdAtaSmartDataCapabilities.
        :type selective_self_test_supported: bool
        """

        self._selective_self_test_supported = selective_self_test_supported

    @property
    def attribute_autosave_enabled(self) -> bool:
        """Gets the attribute_autosave_enabled of this SmartSsdAtaSmartDataCapabilities.


        :return: The attribute_autosave_enabled of this SmartSsdAtaSmartDataCapabilities.
        :rtype: bool
        """
        return self._attribute_autosave_enabled

    @attribute_autosave_enabled.setter
    def attribute_autosave_enabled(self, attribute_autosave_enabled: bool):
        """Sets the attribute_autosave_enabled of this SmartSsdAtaSmartDataCapabilities.


        :param attribute_autosave_enabled: The attribute_autosave_enabled of this SmartSsdAtaSmartDataCapabilities.
        :type attribute_autosave_enabled: bool
        """

        self._attribute_autosave_enabled = attribute_autosave_enabled

    @property
    def error_logging_supported(self) -> bool:
        """Gets the error_logging_supported of this SmartSsdAtaSmartDataCapabilities.


        :return: The error_logging_supported of this SmartSsdAtaSmartDataCapabilities.
        :rtype: bool
        """
        return self._error_logging_supported

    @error_logging_supported.setter
    def error_logging_supported(self, error_logging_supported: bool):
        """Sets the error_logging_supported of this SmartSsdAtaSmartDataCapabilities.


        :param error_logging_supported: The error_logging_supported of this SmartSsdAtaSmartDataCapabilities.
        :type error_logging_supported: bool
        """

        self._error_logging_supported = error_logging_supported

    @property
    def gp_logging_supported(self) -> bool:
        """Gets the gp_logging_supported of this SmartSsdAtaSmartDataCapabilities.


        :return: The gp_logging_supported of this SmartSsdAtaSmartDataCapabilities.
        :rtype: bool
        """
        return self._gp_logging_supported

    @gp_logging_supported.setter
    def gp_logging_supported(self, gp_logging_supported: bool):
        """Sets the gp_logging_supported of this SmartSsdAtaSmartDataCapabilities.


        :param gp_logging_supported: The gp_logging_supported of this SmartSsdAtaSmartDataCapabilities.
        :type gp_logging_supported: bool
        """

        self._gp_logging_supported = gp_logging_supported