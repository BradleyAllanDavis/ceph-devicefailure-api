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


class SmartSsdAtaSmartAttributesFlags(object):
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
        'value': 'int',
        'string': 'str',
        'prefailure': 'bool',
        'updated_online': 'bool',
        'performance': 'bool',
        'error_rate': 'bool',
        'event_count': 'bool',
        'auto_keep': 'bool'
    }

    attribute_map = {
        'value': 'value',
        'string': 'string',
        'prefailure': 'prefailure',
        'updated_online': 'updated_online',
        'performance': 'performance',
        'error_rate': 'error_rate',
        'event_count': 'event_count',
        'auto_keep': 'auto_keep'
    }

    def __init__(self, value=None, string=None, prefailure=None, updated_online=None, performance=None, error_rate=None, event_count=None, auto_keep=None):  # noqa: E501
        """SmartSsdAtaSmartAttributesFlags - a model defined in Swagger"""  # noqa: E501

        self._value = None
        self._string = None
        self._prefailure = None
        self._updated_online = None
        self._performance = None
        self._error_rate = None
        self._event_count = None
        self._auto_keep = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if string is not None:
            self.string = string
        if prefailure is not None:
            self.prefailure = prefailure
        if updated_online is not None:
            self.updated_online = updated_online
        if performance is not None:
            self.performance = performance
        if error_rate is not None:
            self.error_rate = error_rate
        if event_count is not None:
            self.event_count = event_count
        if auto_keep is not None:
            self.auto_keep = auto_keep

    @property
    def value(self):
        """Gets the value of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501


        :return: The value of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SmartSsdAtaSmartAttributesFlags.


        :param value: The value of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501
        :type: int
        """

        self._value = value

    @property
    def string(self):
        """Gets the string of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501


        :return: The string of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501
        :rtype: str
        """
        return self._string

    @string.setter
    def string(self, string):
        """Sets the string of this SmartSsdAtaSmartAttributesFlags.


        :param string: The string of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501
        :type: str
        """

        self._string = string

    @property
    def prefailure(self):
        """Gets the prefailure of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501


        :return: The prefailure of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501
        :rtype: bool
        """
        return self._prefailure

    @prefailure.setter
    def prefailure(self, prefailure):
        """Sets the prefailure of this SmartSsdAtaSmartAttributesFlags.


        :param prefailure: The prefailure of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501
        :type: bool
        """

        self._prefailure = prefailure

    @property
    def updated_online(self):
        """Gets the updated_online of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501


        :return: The updated_online of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501
        :rtype: bool
        """
        return self._updated_online

    @updated_online.setter
    def updated_online(self, updated_online):
        """Sets the updated_online of this SmartSsdAtaSmartAttributesFlags.


        :param updated_online: The updated_online of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501
        :type: bool
        """

        self._updated_online = updated_online

    @property
    def performance(self):
        """Gets the performance of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501


        :return: The performance of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501
        :rtype: bool
        """
        return self._performance

    @performance.setter
    def performance(self, performance):
        """Sets the performance of this SmartSsdAtaSmartAttributesFlags.


        :param performance: The performance of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501
        :type: bool
        """

        self._performance = performance

    @property
    def error_rate(self):
        """Gets the error_rate of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501


        :return: The error_rate of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501
        :rtype: bool
        """
        return self._error_rate

    @error_rate.setter
    def error_rate(self, error_rate):
        """Sets the error_rate of this SmartSsdAtaSmartAttributesFlags.


        :param error_rate: The error_rate of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501
        :type: bool
        """

        self._error_rate = error_rate

    @property
    def event_count(self):
        """Gets the event_count of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501


        :return: The event_count of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501
        :rtype: bool
        """
        return self._event_count

    @event_count.setter
    def event_count(self, event_count):
        """Sets the event_count of this SmartSsdAtaSmartAttributesFlags.


        :param event_count: The event_count of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501
        :type: bool
        """

        self._event_count = event_count

    @property
    def auto_keep(self):
        """Gets the auto_keep of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501


        :return: The auto_keep of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501
        :rtype: bool
        """
        return self._auto_keep

    @auto_keep.setter
    def auto_keep(self, auto_keep):
        """Sets the auto_keep of this SmartSsdAtaSmartAttributesFlags.


        :param auto_keep: The auto_keep of this SmartSsdAtaSmartAttributesFlags.  # noqa: E501
        :type: bool
        """

        self._auto_keep = auto_keep

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
        if not isinstance(other, SmartSsdAtaSmartAttributesFlags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
