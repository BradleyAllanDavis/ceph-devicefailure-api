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

from swagger_client.models.smart_ssd_ata_log_directory_table import SmartSsdAtaLogDirectoryTable  # noqa: F401,E501


class SmartSsdAtaLogDirectory(object):
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
        'gp_dir_version': 'int',
        'smart_dir_version': 'int',
        'smart_dir_multi_sector': 'bool',
        'table': 'list[SmartSsdAtaLogDirectoryTable]'
    }

    attribute_map = {
        'gp_dir_version': 'gp_dir_version',
        'smart_dir_version': 'smart_dir_version',
        'smart_dir_multi_sector': 'smart_dir_multi_sector',
        'table': 'table'
    }

    def __init__(self, gp_dir_version=None, smart_dir_version=None, smart_dir_multi_sector=None, table=None):  # noqa: E501
        """SmartSsdAtaLogDirectory - a model defined in Swagger"""  # noqa: E501

        self._gp_dir_version = None
        self._smart_dir_version = None
        self._smart_dir_multi_sector = None
        self._table = None
        self.discriminator = None

        if gp_dir_version is not None:
            self.gp_dir_version = gp_dir_version
        if smart_dir_version is not None:
            self.smart_dir_version = smart_dir_version
        if smart_dir_multi_sector is not None:
            self.smart_dir_multi_sector = smart_dir_multi_sector
        if table is not None:
            self.table = table

    @property
    def gp_dir_version(self):
        """Gets the gp_dir_version of this SmartSsdAtaLogDirectory.  # noqa: E501


        :return: The gp_dir_version of this SmartSsdAtaLogDirectory.  # noqa: E501
        :rtype: int
        """
        return self._gp_dir_version

    @gp_dir_version.setter
    def gp_dir_version(self, gp_dir_version):
        """Sets the gp_dir_version of this SmartSsdAtaLogDirectory.


        :param gp_dir_version: The gp_dir_version of this SmartSsdAtaLogDirectory.  # noqa: E501
        :type: int
        """

        self._gp_dir_version = gp_dir_version

    @property
    def smart_dir_version(self):
        """Gets the smart_dir_version of this SmartSsdAtaLogDirectory.  # noqa: E501


        :return: The smart_dir_version of this SmartSsdAtaLogDirectory.  # noqa: E501
        :rtype: int
        """
        return self._smart_dir_version

    @smart_dir_version.setter
    def smart_dir_version(self, smart_dir_version):
        """Sets the smart_dir_version of this SmartSsdAtaLogDirectory.


        :param smart_dir_version: The smart_dir_version of this SmartSsdAtaLogDirectory.  # noqa: E501
        :type: int
        """

        self._smart_dir_version = smart_dir_version

    @property
    def smart_dir_multi_sector(self):
        """Gets the smart_dir_multi_sector of this SmartSsdAtaLogDirectory.  # noqa: E501


        :return: The smart_dir_multi_sector of this SmartSsdAtaLogDirectory.  # noqa: E501
        :rtype: bool
        """
        return self._smart_dir_multi_sector

    @smart_dir_multi_sector.setter
    def smart_dir_multi_sector(self, smart_dir_multi_sector):
        """Sets the smart_dir_multi_sector of this SmartSsdAtaLogDirectory.


        :param smart_dir_multi_sector: The smart_dir_multi_sector of this SmartSsdAtaLogDirectory.  # noqa: E501
        :type: bool
        """

        self._smart_dir_multi_sector = smart_dir_multi_sector

    @property
    def table(self):
        """Gets the table of this SmartSsdAtaLogDirectory.  # noqa: E501


        :return: The table of this SmartSsdAtaLogDirectory.  # noqa: E501
        :rtype: list[SmartSsdAtaLogDirectoryTable]
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this SmartSsdAtaLogDirectory.


        :param table: The table of this SmartSsdAtaLogDirectory.  # noqa: E501
        :type: list[SmartSsdAtaLogDirectoryTable]
        """

        self._table = table

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
        if not isinstance(other, SmartSsdAtaLogDirectory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other