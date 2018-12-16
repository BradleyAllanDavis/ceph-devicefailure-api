# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SmartNvmeSmartctl(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, version: List[int]=None, svn_revision: str=None, platform_info: str=None, build_info: str=None, argv: List[str]=None, exit_status: int=None):  # noqa: E501
        """SmartNvmeSmartctl - a model defined in Swagger

        :param version: The version of this SmartNvmeSmartctl.  # noqa: E501
        :type version: List[int]
        :param svn_revision: The svn_revision of this SmartNvmeSmartctl.  # noqa: E501
        :type svn_revision: str
        :param platform_info: The platform_info of this SmartNvmeSmartctl.  # noqa: E501
        :type platform_info: str
        :param build_info: The build_info of this SmartNvmeSmartctl.  # noqa: E501
        :type build_info: str
        :param argv: The argv of this SmartNvmeSmartctl.  # noqa: E501
        :type argv: List[str]
        :param exit_status: The exit_status of this SmartNvmeSmartctl.  # noqa: E501
        :type exit_status: int
        """
        self.swagger_types = {
            'version': List[int],
            'svn_revision': str,
            'platform_info': str,
            'build_info': str,
            'argv': List[str],
            'exit_status': int
        }

        self.attribute_map = {
            'version': 'version',
            'svn_revision': 'svn_revision',
            'platform_info': 'platform_info',
            'build_info': 'build_info',
            'argv': 'argv',
            'exit_status': 'exit_status'
        }

        self._version = version
        self._svn_revision = svn_revision
        self._platform_info = platform_info
        self._build_info = build_info
        self._argv = argv
        self._exit_status = exit_status

    @classmethod
    def from_dict(cls, dikt) -> 'SmartNvmeSmartctl':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SmartNvme_smartctl of this SmartNvmeSmartctl.  # noqa: E501
        :rtype: SmartNvmeSmartctl
        """
        return util.deserialize_model(dikt, cls)

    @property
    def version(self) -> List[int]:
        """Gets the version of this SmartNvmeSmartctl.


        :return: The version of this SmartNvmeSmartctl.
        :rtype: List[int]
        """
        return self._version

    @version.setter
    def version(self, version: List[int]):
        """Sets the version of this SmartNvmeSmartctl.


        :param version: The version of this SmartNvmeSmartctl.
        :type version: List[int]
        """

        self._version = version

    @property
    def svn_revision(self) -> str:
        """Gets the svn_revision of this SmartNvmeSmartctl.


        :return: The svn_revision of this SmartNvmeSmartctl.
        :rtype: str
        """
        return self._svn_revision

    @svn_revision.setter
    def svn_revision(self, svn_revision: str):
        """Sets the svn_revision of this SmartNvmeSmartctl.


        :param svn_revision: The svn_revision of this SmartNvmeSmartctl.
        :type svn_revision: str
        """

        self._svn_revision = svn_revision

    @property
    def platform_info(self) -> str:
        """Gets the platform_info of this SmartNvmeSmartctl.


        :return: The platform_info of this SmartNvmeSmartctl.
        :rtype: str
        """
        return self._platform_info

    @platform_info.setter
    def platform_info(self, platform_info: str):
        """Sets the platform_info of this SmartNvmeSmartctl.


        :param platform_info: The platform_info of this SmartNvmeSmartctl.
        :type platform_info: str
        """

        self._platform_info = platform_info

    @property
    def build_info(self) -> str:
        """Gets the build_info of this SmartNvmeSmartctl.


        :return: The build_info of this SmartNvmeSmartctl.
        :rtype: str
        """
        return self._build_info

    @build_info.setter
    def build_info(self, build_info: str):
        """Sets the build_info of this SmartNvmeSmartctl.


        :param build_info: The build_info of this SmartNvmeSmartctl.
        :type build_info: str
        """

        self._build_info = build_info

    @property
    def argv(self) -> List[str]:
        """Gets the argv of this SmartNvmeSmartctl.


        :return: The argv of this SmartNvmeSmartctl.
        :rtype: List[str]
        """
        return self._argv

    @argv.setter
    def argv(self, argv: List[str]):
        """Sets the argv of this SmartNvmeSmartctl.


        :param argv: The argv of this SmartNvmeSmartctl.
        :type argv: List[str]
        """

        self._argv = argv

    @property
    def exit_status(self) -> int:
        """Gets the exit_status of this SmartNvmeSmartctl.


        :return: The exit_status of this SmartNvmeSmartctl.
        :rtype: int
        """
        return self._exit_status

    @exit_status.setter
    def exit_status(self, exit_status: int):
        """Sets the exit_status of this SmartNvmeSmartctl.


        :param exit_status: The exit_status of this SmartNvmeSmartctl.
        :type exit_status: int
        """

        self._exit_status = exit_status
