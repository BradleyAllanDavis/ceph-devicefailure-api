# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.smart_nvme_eui64 import SmartNvmeEui64  # noqa: F401,E501
from swagger_server.models.smart_nvme_size import SmartNvmeSize  # noqa: F401,E501
from swagger_server import util


class SmartNvmeNvmeNamespaces(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, size: SmartNvmeSize=None, capacity: SmartNvmeSize=None, utilization: SmartNvmeSize=None, formatted_lba_size: int=None, eui64: SmartNvmeEui64=None):  # noqa: E501
        """SmartNvmeNvmeNamespaces - a model defined in Swagger

        :param id: The id of this SmartNvmeNvmeNamespaces.  # noqa: E501
        :type id: int
        :param size: The size of this SmartNvmeNvmeNamespaces.  # noqa: E501
        :type size: SmartNvmeSize
        :param capacity: The capacity of this SmartNvmeNvmeNamespaces.  # noqa: E501
        :type capacity: SmartNvmeSize
        :param utilization: The utilization of this SmartNvmeNvmeNamespaces.  # noqa: E501
        :type utilization: SmartNvmeSize
        :param formatted_lba_size: The formatted_lba_size of this SmartNvmeNvmeNamespaces.  # noqa: E501
        :type formatted_lba_size: int
        :param eui64: The eui64 of this SmartNvmeNvmeNamespaces.  # noqa: E501
        :type eui64: SmartNvmeEui64
        """
        self.swagger_types = {
            'id': int,
            'size': SmartNvmeSize,
            'capacity': SmartNvmeSize,
            'utilization': SmartNvmeSize,
            'formatted_lba_size': int,
            'eui64': SmartNvmeEui64
        }

        self.attribute_map = {
            'id': 'id',
            'size': 'size',
            'capacity': 'capacity',
            'utilization': 'utilization',
            'formatted_lba_size': 'formatted_lba_size',
            'eui64': 'eui64'
        }

        self._id = id
        self._size = size
        self._capacity = capacity
        self._utilization = utilization
        self._formatted_lba_size = formatted_lba_size
        self._eui64 = eui64

    @classmethod
    def from_dict(cls, dikt) -> 'SmartNvmeNvmeNamespaces':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SmartNvme_nvme_namespaces of this SmartNvmeNvmeNamespaces.  # noqa: E501
        :rtype: SmartNvmeNvmeNamespaces
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this SmartNvmeNvmeNamespaces.


        :return: The id of this SmartNvmeNvmeNamespaces.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this SmartNvmeNvmeNamespaces.


        :param id: The id of this SmartNvmeNvmeNamespaces.
        :type id: int
        """

        self._id = id

    @property
    def size(self) -> SmartNvmeSize:
        """Gets the size of this SmartNvmeNvmeNamespaces.


        :return: The size of this SmartNvmeNvmeNamespaces.
        :rtype: SmartNvmeSize
        """
        return self._size

    @size.setter
    def size(self, size: SmartNvmeSize):
        """Sets the size of this SmartNvmeNvmeNamespaces.


        :param size: The size of this SmartNvmeNvmeNamespaces.
        :type size: SmartNvmeSize
        """

        self._size = size

    @property
    def capacity(self) -> SmartNvmeSize:
        """Gets the capacity of this SmartNvmeNvmeNamespaces.


        :return: The capacity of this SmartNvmeNvmeNamespaces.
        :rtype: SmartNvmeSize
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: SmartNvmeSize):
        """Sets the capacity of this SmartNvmeNvmeNamespaces.


        :param capacity: The capacity of this SmartNvmeNvmeNamespaces.
        :type capacity: SmartNvmeSize
        """

        self._capacity = capacity

    @property
    def utilization(self) -> SmartNvmeSize:
        """Gets the utilization of this SmartNvmeNvmeNamespaces.


        :return: The utilization of this SmartNvmeNvmeNamespaces.
        :rtype: SmartNvmeSize
        """
        return self._utilization

    @utilization.setter
    def utilization(self, utilization: SmartNvmeSize):
        """Sets the utilization of this SmartNvmeNvmeNamespaces.


        :param utilization: The utilization of this SmartNvmeNvmeNamespaces.
        :type utilization: SmartNvmeSize
        """

        self._utilization = utilization

    @property
    def formatted_lba_size(self) -> int:
        """Gets the formatted_lba_size of this SmartNvmeNvmeNamespaces.


        :return: The formatted_lba_size of this SmartNvmeNvmeNamespaces.
        :rtype: int
        """
        return self._formatted_lba_size

    @formatted_lba_size.setter
    def formatted_lba_size(self, formatted_lba_size: int):
        """Sets the formatted_lba_size of this SmartNvmeNvmeNamespaces.


        :param formatted_lba_size: The formatted_lba_size of this SmartNvmeNvmeNamespaces.
        :type formatted_lba_size: int
        """

        self._formatted_lba_size = formatted_lba_size

    @property
    def eui64(self) -> SmartNvmeEui64:
        """Gets the eui64 of this SmartNvmeNvmeNamespaces.


        :return: The eui64 of this SmartNvmeNvmeNamespaces.
        :rtype: SmartNvmeEui64
        """
        return self._eui64

    @eui64.setter
    def eui64(self, eui64: SmartNvmeEui64):
        """Sets the eui64 of this SmartNvmeNvmeNamespaces.


        :param eui64: The eui64 of this SmartNvmeNvmeNamespaces.
        :type eui64: SmartNvmeEui64
        """

        self._eui64 = eui64
