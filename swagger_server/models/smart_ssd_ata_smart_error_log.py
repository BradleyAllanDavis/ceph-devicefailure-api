# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.smart_ssd_ata_smart_error_log_extended import SmartSsdAtaSmartErrorLogExtended  # noqa: F401,E501
from swagger_server import util


class SmartSsdAtaSmartErrorLog(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, extended: SmartSsdAtaSmartErrorLogExtended=None):  # noqa: E501
        """SmartSsdAtaSmartErrorLog - a model defined in Swagger

        :param extended: The extended of this SmartSsdAtaSmartErrorLog.  # noqa: E501
        :type extended: SmartSsdAtaSmartErrorLogExtended
        """
        self.swagger_types = {
            'extended': SmartSsdAtaSmartErrorLogExtended
        }

        self.attribute_map = {
            'extended': 'extended'
        }

        self._extended = extended

    @classmethod
    def from_dict(cls, dikt) -> 'SmartSsdAtaSmartErrorLog':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SmartSsd_ata_smart_error_log of this SmartSsdAtaSmartErrorLog.  # noqa: E501
        :rtype: SmartSsdAtaSmartErrorLog
        """
        return util.deserialize_model(dikt, cls)

    @property
    def extended(self) -> SmartSsdAtaSmartErrorLogExtended:
        """Gets the extended of this SmartSsdAtaSmartErrorLog.


        :return: The extended of this SmartSsdAtaSmartErrorLog.
        :rtype: SmartSsdAtaSmartErrorLogExtended
        """
        return self._extended

    @extended.setter
    def extended(self, extended: SmartSsdAtaSmartErrorLogExtended):
        """Sets the extended of this SmartSsdAtaSmartErrorLog.


        :param extended: The extended of this SmartSsdAtaSmartErrorLog.
        :type extended: SmartSsdAtaSmartErrorLogExtended
        """

        self._extended = extended
