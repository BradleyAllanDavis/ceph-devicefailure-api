# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SmartNvmeNvmePciVendor(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, subsystem_id: int=None):  # noqa: E501
        """SmartNvmeNvmePciVendor - a model defined in Swagger

        :param id: The id of this SmartNvmeNvmePciVendor.  # noqa: E501
        :type id: int
        :param subsystem_id: The subsystem_id of this SmartNvmeNvmePciVendor.  # noqa: E501
        :type subsystem_id: int
        """
        self.swagger_types = {
            'id': int,
            'subsystem_id': int
        }

        self.attribute_map = {
            'id': 'id',
            'subsystem_id': 'subsystem_id'
        }

        self._id = id
        self._subsystem_id = subsystem_id

    @classmethod
    def from_dict(cls, dikt) -> 'SmartNvmeNvmePciVendor':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SmartNvme_nvme_pci_vendor of this SmartNvmeNvmePciVendor.  # noqa: E501
        :rtype: SmartNvmeNvmePciVendor
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this SmartNvmeNvmePciVendor.


        :return: The id of this SmartNvmeNvmePciVendor.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this SmartNvmeNvmePciVendor.


        :param id: The id of this SmartNvmeNvmePciVendor.
        :type id: int
        """

        self._id = id

    @property
    def subsystem_id(self) -> int:
        """Gets the subsystem_id of this SmartNvmeNvmePciVendor.


        :return: The subsystem_id of this SmartNvmeNvmePciVendor.
        :rtype: int
        """
        return self._subsystem_id

    @subsystem_id.setter
    def subsystem_id(self, subsystem_id: int):
        """Sets the subsystem_id of this SmartNvmeNvmePciVendor.


        :param subsystem_id: The subsystem_id of this SmartNvmeNvmePciVendor.
        :type subsystem_id: int
        """

        self._subsystem_id = subsystem_id