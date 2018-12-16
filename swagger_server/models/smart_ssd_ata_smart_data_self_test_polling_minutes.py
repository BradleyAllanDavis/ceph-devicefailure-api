# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SmartSsdAtaSmartDataSelfTestPollingMinutes(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, short: int=None, extended: int=None, conveyance: int=None):  # noqa: E501
        """SmartSsdAtaSmartDataSelfTestPollingMinutes - a model defined in Swagger

        :param short: The short of this SmartSsdAtaSmartDataSelfTestPollingMinutes.  # noqa: E501
        :type short: int
        :param extended: The extended of this SmartSsdAtaSmartDataSelfTestPollingMinutes.  # noqa: E501
        :type extended: int
        :param conveyance: The conveyance of this SmartSsdAtaSmartDataSelfTestPollingMinutes.  # noqa: E501
        :type conveyance: int
        """
        self.swagger_types = {
            'short': int,
            'extended': int,
            'conveyance': int
        }

        self.attribute_map = {
            'short': 'short',
            'extended': 'extended',
            'conveyance': 'conveyance'
        }

        self._short = short
        self._extended = extended
        self._conveyance = conveyance

    @classmethod
    def from_dict(cls, dikt) -> 'SmartSsdAtaSmartDataSelfTestPollingMinutes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SmartSsd_ata_smart_data_self_test_polling_minutes of this SmartSsdAtaSmartDataSelfTestPollingMinutes.  # noqa: E501
        :rtype: SmartSsdAtaSmartDataSelfTestPollingMinutes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def short(self) -> int:
        """Gets the short of this SmartSsdAtaSmartDataSelfTestPollingMinutes.


        :return: The short of this SmartSsdAtaSmartDataSelfTestPollingMinutes.
        :rtype: int
        """
        return self._short

    @short.setter
    def short(self, short: int):
        """Sets the short of this SmartSsdAtaSmartDataSelfTestPollingMinutes.


        :param short: The short of this SmartSsdAtaSmartDataSelfTestPollingMinutes.
        :type short: int
        """

        self._short = short

    @property
    def extended(self) -> int:
        """Gets the extended of this SmartSsdAtaSmartDataSelfTestPollingMinutes.


        :return: The extended of this SmartSsdAtaSmartDataSelfTestPollingMinutes.
        :rtype: int
        """
        return self._extended

    @extended.setter
    def extended(self, extended: int):
        """Sets the extended of this SmartSsdAtaSmartDataSelfTestPollingMinutes.


        :param extended: The extended of this SmartSsdAtaSmartDataSelfTestPollingMinutes.
        :type extended: int
        """

        self._extended = extended

    @property
    def conveyance(self) -> int:
        """Gets the conveyance of this SmartSsdAtaSmartDataSelfTestPollingMinutes.


        :return: The conveyance of this SmartSsdAtaSmartDataSelfTestPollingMinutes.
        :rtype: int
        """
        return self._conveyance

    @conveyance.setter
    def conveyance(self, conveyance: int):
        """Sets the conveyance of this SmartSsdAtaSmartDataSelfTestPollingMinutes.


        :param conveyance: The conveyance of this SmartSsdAtaSmartDataSelfTestPollingMinutes.
        :type conveyance: int
        """

        self._conveyance = conveyance
