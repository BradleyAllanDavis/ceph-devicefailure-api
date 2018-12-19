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

from swagger_client.models.smart_ssd_read_lookahead import SmartSsdReadLookahead  # noqa: F401,E501


class SmartSsdAtaSctErc(object):
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
        'read': 'SmartSsdReadLookahead',
        'write': 'SmartSsdReadLookahead'
    }

    attribute_map = {
        'read': 'read',
        'write': 'write'
    }

    def __init__(self, read=None, write=None):  # noqa: E501
        """SmartSsdAtaSctErc - a model defined in Swagger"""  # noqa: E501

        self._read = None
        self._write = None
        self.discriminator = None

        if read is not None:
            self.read = read
        if write is not None:
            self.write = write

    @property
    def read(self):
        """Gets the read of this SmartSsdAtaSctErc.  # noqa: E501


        :return: The read of this SmartSsdAtaSctErc.  # noqa: E501
        :rtype: SmartSsdReadLookahead
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this SmartSsdAtaSctErc.


        :param read: The read of this SmartSsdAtaSctErc.  # noqa: E501
        :type: SmartSsdReadLookahead
        """

        self._read = read

    @property
    def write(self):
        """Gets the write of this SmartSsdAtaSctErc.  # noqa: E501


        :return: The write of this SmartSsdAtaSctErc.  # noqa: E501
        :rtype: SmartSsdReadLookahead
        """
        return self._write

    @write.setter
    def write(self, write):
        """Sets the write of this SmartSsdAtaSctErc.


        :param write: The write of this SmartSsdAtaSctErc.  # noqa: E501
        :type: SmartSsdReadLookahead
        """

        self._write = write

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
        if not isinstance(other, SmartSsdAtaSctErc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
