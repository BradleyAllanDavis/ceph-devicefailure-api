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


class SmartNvmeEui64(object):
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
        'oui': 'int',
        'ext_id': 'int'
    }

    attribute_map = {
        'oui': 'oui',
        'ext_id': 'ext_id'
    }

    def __init__(self, oui=None, ext_id=None):  # noqa: E501
        """SmartNvmeEui64 - a model defined in Swagger"""  # noqa: E501

        self._oui = None
        self._ext_id = None
        self.discriminator = None

        if oui is not None:
            self.oui = oui
        if ext_id is not None:
            self.ext_id = ext_id

    @property
    def oui(self):
        """Gets the oui of this SmartNvmeEui64.  # noqa: E501


        :return: The oui of this SmartNvmeEui64.  # noqa: E501
        :rtype: int
        """
        return self._oui

    @oui.setter
    def oui(self, oui):
        """Sets the oui of this SmartNvmeEui64.


        :param oui: The oui of this SmartNvmeEui64.  # noqa: E501
        :type: int
        """

        self._oui = oui

    @property
    def ext_id(self):
        """Gets the ext_id of this SmartNvmeEui64.  # noqa: E501


        :return: The ext_id of this SmartNvmeEui64.  # noqa: E501
        :rtype: int
        """
        return self._ext_id

    @ext_id.setter
    def ext_id(self, ext_id):
        """Sets the ext_id of this SmartNvmeEui64.


        :param ext_id: The ext_id of this SmartNvmeEui64.  # noqa: E501
        :type: int
        """

        self._ext_id = ext_id

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
        if not isinstance(other, SmartNvmeEui64):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
