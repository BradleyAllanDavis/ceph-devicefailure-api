# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SmartSsdUserCapacityBytes(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, n: int=None, s: str=None):  # noqa: E501
        """SmartSsdUserCapacityBytes - a model defined in Swagger

        :param n: The n of this SmartSsdUserCapacityBytes.  # noqa: E501
        :type n: int
        :param s: The s of this SmartSsdUserCapacityBytes.  # noqa: E501
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
    def from_dict(cls, dikt) -> 'SmartSsdUserCapacityBytes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SmartSsd_user_capacity_bytes of this SmartSsdUserCapacityBytes.  # noqa: E501
        :rtype: SmartSsdUserCapacityBytes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def n(self) -> int:
        """Gets the n of this SmartSsdUserCapacityBytes.


        :return: The n of this SmartSsdUserCapacityBytes.
        :rtype: int
        """
        return self._n

    @n.setter
    def n(self, n: int):
        """Sets the n of this SmartSsdUserCapacityBytes.


        :param n: The n of this SmartSsdUserCapacityBytes.
        :type n: int
        """

        self._n = n

    @property
    def s(self) -> str:
        """Gets the s of this SmartSsdUserCapacityBytes.


        :return: The s of this SmartSsdUserCapacityBytes.
        :rtype: str
        """
        return self._s

    @s.setter
    def s(self, s: str):
        """Sets the s of this SmartSsdUserCapacityBytes.


        :param s: The s of this SmartSsdUserCapacityBytes.
        :type s: str
        """

        self._s = s