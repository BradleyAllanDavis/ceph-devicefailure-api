# coding: utf-8

"""
    Ceph SMART Metrics

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.smart_nvme_eui64 import SmartNvmeEui64  # noqa: F401,E501
from swagger_client.models.smart_nvme_size import SmartNvmeSize  # noqa: F401,E501


class SmartNvmeNvmeNamespaces(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'size': 'SmartNvmeSize',
        'capacity': 'SmartNvmeSize',
        'utilization': 'SmartNvmeSize',
        'formatted_lba_size': 'int',
        'eui64': 'SmartNvmeEui64'
    }

    attribute_map = {
        'id': 'id',
        'size': 'size',
        'capacity': 'capacity',
        'utilization': 'utilization',
        'formatted_lba_size': 'formatted_lba_size',
        'eui64': 'eui64'
    }

    def __init__(self, id=None, size=None, capacity=None, utilization=None, formatted_lba_size=None, eui64=None):  # noqa: E501
        """SmartNvmeNvmeNamespaces - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._size = None
        self._capacity = None
        self._utilization = None
        self._formatted_lba_size = None
        self._eui64 = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if capacity is not None:
            self.capacity = capacity
        if utilization is not None:
            self.utilization = utilization
        if formatted_lba_size is not None:
            self.formatted_lba_size = formatted_lba_size
        if eui64 is not None:
            self.eui64 = eui64

    @property
    def id(self):
        """Gets the id of this SmartNvmeNvmeNamespaces.  # noqa: E501


        :return: The id of this SmartNvmeNvmeNamespaces.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SmartNvmeNvmeNamespaces.


        :param id: The id of this SmartNvmeNvmeNamespaces.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def size(self):
        """Gets the size of this SmartNvmeNvmeNamespaces.  # noqa: E501


        :return: The size of this SmartNvmeNvmeNamespaces.  # noqa: E501
        :rtype: SmartNvmeSize
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SmartNvmeNvmeNamespaces.


        :param size: The size of this SmartNvmeNvmeNamespaces.  # noqa: E501
        :type: SmartNvmeSize
        """

        self._size = size

    @property
    def capacity(self):
        """Gets the capacity of this SmartNvmeNvmeNamespaces.  # noqa: E501


        :return: The capacity of this SmartNvmeNvmeNamespaces.  # noqa: E501
        :rtype: SmartNvmeSize
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this SmartNvmeNvmeNamespaces.


        :param capacity: The capacity of this SmartNvmeNvmeNamespaces.  # noqa: E501
        :type: SmartNvmeSize
        """

        self._capacity = capacity

    @property
    def utilization(self):
        """Gets the utilization of this SmartNvmeNvmeNamespaces.  # noqa: E501


        :return: The utilization of this SmartNvmeNvmeNamespaces.  # noqa: E501
        :rtype: SmartNvmeSize
        """
        return self._utilization

    @utilization.setter
    def utilization(self, utilization):
        """Sets the utilization of this SmartNvmeNvmeNamespaces.


        :param utilization: The utilization of this SmartNvmeNvmeNamespaces.  # noqa: E501
        :type: SmartNvmeSize
        """

        self._utilization = utilization

    @property
    def formatted_lba_size(self):
        """Gets the formatted_lba_size of this SmartNvmeNvmeNamespaces.  # noqa: E501


        :return: The formatted_lba_size of this SmartNvmeNvmeNamespaces.  # noqa: E501
        :rtype: int
        """
        return self._formatted_lba_size

    @formatted_lba_size.setter
    def formatted_lba_size(self, formatted_lba_size):
        """Sets the formatted_lba_size of this SmartNvmeNvmeNamespaces.


        :param formatted_lba_size: The formatted_lba_size of this SmartNvmeNvmeNamespaces.  # noqa: E501
        :type: int
        """

        self._formatted_lba_size = formatted_lba_size

    @property
    def eui64(self):
        """Gets the eui64 of this SmartNvmeNvmeNamespaces.  # noqa: E501


        :return: The eui64 of this SmartNvmeNvmeNamespaces.  # noqa: E501
        :rtype: SmartNvmeEui64
        """
        return self._eui64

    @eui64.setter
    def eui64(self, eui64):
        """Sets the eui64 of this SmartNvmeNvmeNamespaces.


        :param eui64: The eui64 of this SmartNvmeNvmeNamespaces.  # noqa: E501
        :type: SmartNvmeEui64
        """

        self._eui64 = eui64

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SmartNvmeNvmeNamespaces):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
