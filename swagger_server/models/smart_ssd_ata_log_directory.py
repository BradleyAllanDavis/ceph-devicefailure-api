# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.smart_ssd_ata_log_directory_table import SmartSsdAtaLogDirectoryTable  # noqa: F401,E501
from swagger_server import util


class SmartSsdAtaLogDirectory(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, gp_dir_version: int=None, smart_dir_version: int=None, smart_dir_multi_sector: bool=None, table: List[SmartSsdAtaLogDirectoryTable]=None):  # noqa: E501
        """SmartSsdAtaLogDirectory - a model defined in Swagger

        :param gp_dir_version: The gp_dir_version of this SmartSsdAtaLogDirectory.  # noqa: E501
        :type gp_dir_version: int
        :param smart_dir_version: The smart_dir_version of this SmartSsdAtaLogDirectory.  # noqa: E501
        :type smart_dir_version: int
        :param smart_dir_multi_sector: The smart_dir_multi_sector of this SmartSsdAtaLogDirectory.  # noqa: E501
        :type smart_dir_multi_sector: bool
        :param table: The table of this SmartSsdAtaLogDirectory.  # noqa: E501
        :type table: List[SmartSsdAtaLogDirectoryTable]
        """
        self.swagger_types = {
            'gp_dir_version': int,
            'smart_dir_version': int,
            'smart_dir_multi_sector': bool,
            'table': List[SmartSsdAtaLogDirectoryTable]
        }

        self.attribute_map = {
            'gp_dir_version': 'gp_dir_version',
            'smart_dir_version': 'smart_dir_version',
            'smart_dir_multi_sector': 'smart_dir_multi_sector',
            'table': 'table'
        }

        self._gp_dir_version = gp_dir_version
        self._smart_dir_version = smart_dir_version
        self._smart_dir_multi_sector = smart_dir_multi_sector
        self._table = table

    @classmethod
    def from_dict(cls, dikt) -> 'SmartSsdAtaLogDirectory':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SmartSsd_ata_log_directory of this SmartSsdAtaLogDirectory.  # noqa: E501
        :rtype: SmartSsdAtaLogDirectory
        """
        return util.deserialize_model(dikt, cls)

    @property
    def gp_dir_version(self) -> int:
        """Gets the gp_dir_version of this SmartSsdAtaLogDirectory.


        :return: The gp_dir_version of this SmartSsdAtaLogDirectory.
        :rtype: int
        """
        return self._gp_dir_version

    @gp_dir_version.setter
    def gp_dir_version(self, gp_dir_version: int):
        """Sets the gp_dir_version of this SmartSsdAtaLogDirectory.


        :param gp_dir_version: The gp_dir_version of this SmartSsdAtaLogDirectory.
        :type gp_dir_version: int
        """

        self._gp_dir_version = gp_dir_version

    @property
    def smart_dir_version(self) -> int:
        """Gets the smart_dir_version of this SmartSsdAtaLogDirectory.


        :return: The smart_dir_version of this SmartSsdAtaLogDirectory.
        :rtype: int
        """
        return self._smart_dir_version

    @smart_dir_version.setter
    def smart_dir_version(self, smart_dir_version: int):
        """Sets the smart_dir_version of this SmartSsdAtaLogDirectory.


        :param smart_dir_version: The smart_dir_version of this SmartSsdAtaLogDirectory.
        :type smart_dir_version: int
        """

        self._smart_dir_version = smart_dir_version

    @property
    def smart_dir_multi_sector(self) -> bool:
        """Gets the smart_dir_multi_sector of this SmartSsdAtaLogDirectory.


        :return: The smart_dir_multi_sector of this SmartSsdAtaLogDirectory.
        :rtype: bool
        """
        return self._smart_dir_multi_sector

    @smart_dir_multi_sector.setter
    def smart_dir_multi_sector(self, smart_dir_multi_sector: bool):
        """Sets the smart_dir_multi_sector of this SmartSsdAtaLogDirectory.


        :param smart_dir_multi_sector: The smart_dir_multi_sector of this SmartSsdAtaLogDirectory.
        :type smart_dir_multi_sector: bool
        """

        self._smart_dir_multi_sector = smart_dir_multi_sector

    @property
    def table(self) -> List[SmartSsdAtaLogDirectoryTable]:
        """Gets the table of this SmartSsdAtaLogDirectory.


        :return: The table of this SmartSsdAtaLogDirectory.
        :rtype: List[SmartSsdAtaLogDirectoryTable]
        """
        return self._table

    @table.setter
    def table(self, table: List[SmartSsdAtaLogDirectoryTable]):
        """Sets the table of this SmartSsdAtaLogDirectory.


        :param table: The table of this SmartSsdAtaLogDirectory.
        :type table: List[SmartSsdAtaLogDirectoryTable]
        """

        self._table = table