# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SmartSsdUserCapacityBlocks(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, n: int=None, s: str=None):  # noqa: E501
        """SmartSsdUserCapacityBlocks - a model defined in Swagger

        :param n: The n of this SmartSsdUserCapacityBlocks.  # noqa: E501
        :type n: int
        :param s: The s of this SmartSsdUserCapacityBlocks.  # noqa: E501
        :type s: str
        """
        self.swagger_types = {
            'n': int,
            's': str
        }

        self.attribute_map = {
            'n': 'n',
            's': 's'
        }

        self._n = n
        self._s = s

    @classmethod
    def from_dict(cls, dikt) -> 'SmartSsdUserCapacityBlocks':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SmartSsd_user_capacity_blocks of this SmartSsdUserCapacityBlocks.  # noqa: E501
        :rtype: SmartSsdUserCapacityBlocks
        """
        return util.deserialize_model(dikt, cls)

    @property
    def n(self) -> int:
        """Gets the n of this SmartSsdUserCapacityBlocks.


        :return: The n of this SmartSsdUserCapacityBlocks.
        :rtype: int
        """
        return self._n

    @n.setter
    def n(self, n: int):
        """Sets the n of this SmartSsdUserCapacityBlocks.


        :param n: The n of this SmartSsdUserCapacityBlocks.
        :type n: int
        """

        self._n = n

    @property
    def s(self) -> str:
        """Gets the s of this SmartSsdUserCapacityBlocks.


        :return: The s of this SmartSsdUserCapacityBlocks.
        :rtype: str
        """
        return self._s

    @s.setter
    def s(self, s: str):
        """Sets the s of this SmartSsdUserCapacityBlocks.


        :param s: The s of this SmartSsdUserCapacityBlocks.
        :type s: str
        """

        self._s = s