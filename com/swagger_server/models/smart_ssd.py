# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.smart_nvme_device import SmartNvmeDevice  # noqa: F401,E501
from swagger_server.models.smart_nvme_local_time import SmartNvmeLocalTime  # noqa: F401,E501
from swagger_server.models.smart_nvme_smartctl import SmartNvmeSmartctl  # noqa: F401,E501
from swagger_server.models.smart_ssd_ata_log_directory import SmartSsdAtaLogDirectory  # noqa: F401,E501
from swagger_server.models.smart_ssd_ata_sct_capabilities import SmartSsdAtaSctCapabilities  # noqa: F401,E501
from swagger_server.models.smart_ssd_ata_sct_erc import SmartSsdAtaSctErc  # noqa: F401,E501
from swagger_server.models.smart_ssd_ata_sct_status import SmartSsdAtaSctStatus  # noqa: F401,E501
from swagger_server.models.smart_ssd_ata_sct_temperature_history import SmartSsdAtaSctTemperatureHistory  # noqa: F401,E501
from swagger_server.models.smart_ssd_ata_security import SmartSsdAtaSecurity  # noqa: F401,E501
from swagger_server.models.smart_ssd_ata_smart_attributes import SmartSsdAtaSmartAttributes  # noqa: F401,E501
from swagger_server.models.smart_ssd_ata_smart_data import SmartSsdAtaSmartData  # noqa: F401,E501
from swagger_server.models.smart_ssd_ata_smart_error_log import SmartSsdAtaSmartErrorLog  # noqa: F401,E501
from swagger_server.models.smart_ssd_ata_version import SmartSsdAtaVersion  # noqa: F401,E501
from swagger_server.models.smart_ssd_form_factor import SmartSsdFormFactor  # noqa: F401,E501
from swagger_server.models.smart_ssd_interface_speed import SmartSsdInterfaceSpeed  # noqa: F401,E501
from swagger_server.models.smart_ssd_read_lookahead import SmartSsdReadLookahead  # noqa: F401,E501
from swagger_server.models.smart_ssd_sata_phy_event_counters import SmartSsdSataPhyEventCounters  # noqa: F401,E501
from swagger_server.models.smart_ssd_sata_version import SmartSsdSataVersion  # noqa: F401,E501
from swagger_server.models.smart_ssd_smart_status import SmartSsdSmartStatus  # noqa: F401,E501
from swagger_server.models.smart_ssd_temperature import SmartSsdTemperature  # noqa: F401,E501
from swagger_server.models.smart_ssd_user_capacity import SmartSsdUserCapacity  # noqa: F401,E501
from swagger_server.models.smart_ssd_wwn import SmartSsdWwn  # noqa: F401,E501
from swagger_server import util


class SmartSsd(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, json_format_version: List[int]=None, smartctl: SmartNvmeSmartctl=None, device: SmartNvmeDevice=None, model_family: str=None, model_name: str=None, serial_number: str=None, wwn: SmartSsdWwn=None, firmware_version: str=None, user_capacity: SmartSsdUserCapacity=None, logical_block_size: int=None, physical_block_size: int=None, rotation_rate: int=None, form_factor: SmartSsdFormFactor=None, in_smartctl_database: bool=None, ata_version: SmartSsdAtaVersion=None, sata_version: SmartSsdSataVersion=None, interface_speed: SmartSsdInterfaceSpeed=None, local_time: SmartNvmeLocalTime=None, read_lookahead: SmartSsdReadLookahead=None, write_cache: SmartSsdReadLookahead=None, ata_security: SmartSsdAtaSecurity=None, smart_status: SmartSsdSmartStatus=None, ata_smart_data: SmartSsdAtaSmartData=None, ata_sct_capabilities: SmartSsdAtaSctCapabilities=None, ata_smart_attributes: SmartSsdAtaSmartAttributes=None, temperature: SmartSsdTemperature=None, ata_log_directory: SmartSsdAtaLogDirectory=None, ata_smart_error_log: SmartSsdAtaSmartErrorLog=None, ata_smart_self_test_log: SmartSsdAtaSmartErrorLog=None, ata_sct_status: SmartSsdAtaSctStatus=None, ata_sct_temperature_history: SmartSsdAtaSctTemperatureHistory=None, ata_sct_erc: SmartSsdAtaSctErc=None, sata_phy_event_counters: SmartSsdSataPhyEventCounters=None):  # noqa: E501
        """SmartSsd - a model defined in Swagger

        :param json_format_version: The json_format_version of this SmartSsd.  # noqa: E501
        :type json_format_version: List[int]
        :param smartctl: The smartctl of this SmartSsd.  # noqa: E501
        :type smartctl: SmartNvmeSmartctl
        :param device: The device of this SmartSsd.  # noqa: E501
        :type device: SmartNvmeDevice
        :param model_family: The model_family of this SmartSsd.  # noqa: E501
        :type model_family: str
        :param model_name: The model_name of this SmartSsd.  # noqa: E501
        :type model_name: str
        :param serial_number: The serial_number of this SmartSsd.  # noqa: E501
        :type serial_number: str
        :param wwn: The wwn of this SmartSsd.  # noqa: E501
        :type wwn: SmartSsdWwn
        :param firmware_version: The firmware_version of this SmartSsd.  # noqa: E501
        :type firmware_version: str
        :param user_capacity: The user_capacity of this SmartSsd.  # noqa: E501
        :type user_capacity: SmartSsdUserCapacity
        :param logical_block_size: The logical_block_size of this SmartSsd.  # noqa: E501
        :type logical_block_size: int
        :param physical_block_size: The physical_block_size of this SmartSsd.  # noqa: E501
        :type physical_block_size: int
        :param rotation_rate: The rotation_rate of this SmartSsd.  # noqa: E501
        :type rotation_rate: int
        :param form_factor: The form_factor of this SmartSsd.  # noqa: E501
        :type form_factor: SmartSsdFormFactor
        :param in_smartctl_database: The in_smartctl_database of this SmartSsd.  # noqa: E501
        :type in_smartctl_database: bool
        :param ata_version: The ata_version of this SmartSsd.  # noqa: E501
        :type ata_version: SmartSsdAtaVersion
        :param sata_version: The sata_version of this SmartSsd.  # noqa: E501
        :type sata_version: SmartSsdSataVersion
        :param interface_speed: The interface_speed of this SmartSsd.  # noqa: E501
        :type interface_speed: SmartSsdInterfaceSpeed
        :param local_time: The local_time of this SmartSsd.  # noqa: E501
        :type local_time: SmartNvmeLocalTime
        :param read_lookahead: The read_lookahead of this SmartSsd.  # noqa: E501
        :type read_lookahead: SmartSsdReadLookahead
        :param write_cache: The write_cache of this SmartSsd.  # noqa: E501
        :type write_cache: SmartSsdReadLookahead
        :param ata_security: The ata_security of this SmartSsd.  # noqa: E501
        :type ata_security: SmartSsdAtaSecurity
        :param smart_status: The smart_status of this SmartSsd.  # noqa: E501
        :type smart_status: SmartSsdSmartStatus
        :param ata_smart_data: The ata_smart_data of this SmartSsd.  # noqa: E501
        :type ata_smart_data: SmartSsdAtaSmartData
        :param ata_sct_capabilities: The ata_sct_capabilities of this SmartSsd.  # noqa: E501
        :type ata_sct_capabilities: SmartSsdAtaSctCapabilities
        :param ata_smart_attributes: The ata_smart_attributes of this SmartSsd.  # noqa: E501
        :type ata_smart_attributes: SmartSsdAtaSmartAttributes
        :param temperature: The temperature of this SmartSsd.  # noqa: E501
        :type temperature: SmartSsdTemperature
        :param ata_log_directory: The ata_log_directory of this SmartSsd.  # noqa: E501
        :type ata_log_directory: SmartSsdAtaLogDirectory
        :param ata_smart_error_log: The ata_smart_error_log of this SmartSsd.  # noqa: E501
        :type ata_smart_error_log: SmartSsdAtaSmartErrorLog
        :param ata_smart_self_test_log: The ata_smart_self_test_log of this SmartSsd.  # noqa: E501
        :type ata_smart_self_test_log: SmartSsdAtaSmartErrorLog
        :param ata_sct_status: The ata_sct_status of this SmartSsd.  # noqa: E501
        :type ata_sct_status: SmartSsdAtaSctStatus
        :param ata_sct_temperature_history: The ata_sct_temperature_history of this SmartSsd.  # noqa: E501
        :type ata_sct_temperature_history: SmartSsdAtaSctTemperatureHistory
        :param ata_sct_erc: The ata_sct_erc of this SmartSsd.  # noqa: E501
        :type ata_sct_erc: SmartSsdAtaSctErc
        :param sata_phy_event_counters: The sata_phy_event_counters of this SmartSsd.  # noqa: E501
        :type sata_phy_event_counters: SmartSsdSataPhyEventCounters
        """
        self.swagger_types = {
            'json_format_version': List[int],
            'smartctl': SmartNvmeSmartctl,
            'device': SmartNvmeDevice,
            'model_family': str,
            'model_name': str,
            'serial_number': str,
            'wwn': SmartSsdWwn,
            'firmware_version': str,
            'user_capacity': SmartSsdUserCapacity,
            'logical_block_size': int,
            'physical_block_size': int,
            'rotation_rate': int,
            'form_factor': SmartSsdFormFactor,
            'in_smartctl_database': bool,
            'ata_version': SmartSsdAtaVersion,
            'sata_version': SmartSsdSataVersion,
            'interface_speed': SmartSsdInterfaceSpeed,
            'local_time': SmartNvmeLocalTime,
            'read_lookahead': SmartSsdReadLookahead,
            'write_cache': SmartSsdReadLookahead,
            'ata_security': SmartSsdAtaSecurity,
            'smart_status': SmartSsdSmartStatus,
            'ata_smart_data': SmartSsdAtaSmartData,
            'ata_sct_capabilities': SmartSsdAtaSctCapabilities,
            'ata_smart_attributes': SmartSsdAtaSmartAttributes,
            'temperature': SmartSsdTemperature,
            'ata_log_directory': SmartSsdAtaLogDirectory,
            'ata_smart_error_log': SmartSsdAtaSmartErrorLog,
            'ata_smart_self_test_log': SmartSsdAtaSmartErrorLog,
            'ata_sct_status': SmartSsdAtaSctStatus,
            'ata_sct_temperature_history': SmartSsdAtaSctTemperatureHistory,
            'ata_sct_erc': SmartSsdAtaSctErc,
            'sata_phy_event_counters': SmartSsdSataPhyEventCounters
        }

        self.attribute_map = {
            'json_format_version': 'json_format_version',
            'smartctl': 'smartctl',
            'device': 'device',
            'model_family': 'model_family',
            'model_name': 'model_name',
            'serial_number': 'serial_number',
            'wwn': 'wwn',
            'firmware_version': 'firmware_version',
            'user_capacity': 'user_capacity',
            'logical_block_size': 'logical_block_size',
            'physical_block_size': 'physical_block_size',
            'rotation_rate': 'rotation_rate',
            'form_factor': 'form_factor',
            'in_smartctl_database': 'in_smartctl_database',
            'ata_version': 'ata_version',
            'sata_version': 'sata_version',
            'interface_speed': 'interface_speed',
            'local_time': 'local_time',
            'read_lookahead': 'read_lookahead',
            'write_cache': 'write_cache',
            'ata_security': 'ata_security',
            'smart_status': 'smart_status',
            'ata_smart_data': 'ata_smart_data',
            'ata_sct_capabilities': 'ata_sct_capabilities',
            'ata_smart_attributes': 'ata_smart_attributes',
            'temperature': 'temperature',
            'ata_log_directory': 'ata_log_directory',
            'ata_smart_error_log': 'ata_smart_error_log',
            'ata_smart_self_test_log': 'ata_smart_self_test_log',
            'ata_sct_status': 'ata_sct_status',
            'ata_sct_temperature_history': 'ata_sct_temperature_history',
            'ata_sct_erc': 'ata_sct_erc',
            'sata_phy_event_counters': 'sata_phy_event_counters'
        }

        self._json_format_version = json_format_version
        self._smartctl = smartctl
        self._device = device
        self._model_family = model_family
        self._model_name = model_name
        self._serial_number = serial_number
        self._wwn = wwn
        self._firmware_version = firmware_version
        self._user_capacity = user_capacity
        self._logical_block_size = logical_block_size
        self._physical_block_size = physical_block_size
        self._rotation_rate = rotation_rate
        self._form_factor = form_factor
        self._in_smartctl_database = in_smartctl_database
        self._ata_version = ata_version
        self._sata_version = sata_version
        self._interface_speed = interface_speed
        self._local_time = local_time
        self._read_lookahead = read_lookahead
        self._write_cache = write_cache
        self._ata_security = ata_security
        self._smart_status = smart_status
        self._ata_smart_data = ata_smart_data
        self._ata_sct_capabilities = ata_sct_capabilities
        self._ata_smart_attributes = ata_smart_attributes
        self._temperature = temperature
        self._ata_log_directory = ata_log_directory
        self._ata_smart_error_log = ata_smart_error_log
        self._ata_smart_self_test_log = ata_smart_self_test_log
        self._ata_sct_status = ata_sct_status
        self._ata_sct_temperature_history = ata_sct_temperature_history
        self._ata_sct_erc = ata_sct_erc
        self._sata_phy_event_counters = sata_phy_event_counters

    @classmethod
    def from_dict(cls, dikt) -> 'SmartSsd':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SmartSsd of this SmartSsd.  # noqa: E501
        :rtype: SmartSsd
        """
        return util.deserialize_model(dikt, cls)

    @property
    def json_format_version(self) -> List[int]:
        """Gets the json_format_version of this SmartSsd.


        :return: The json_format_version of this SmartSsd.
        :rtype: List[int]
        """
        return self._json_format_version

    @json_format_version.setter
    def json_format_version(self, json_format_version: List[int]):
        """Sets the json_format_version of this SmartSsd.


        :param json_format_version: The json_format_version of this SmartSsd.
        :type json_format_version: List[int]
        """

        self._json_format_version = json_format_version

    @property
    def smartctl(self) -> SmartNvmeSmartctl:
        """Gets the smartctl of this SmartSsd.


        :return: The smartctl of this SmartSsd.
        :rtype: SmartNvmeSmartctl
        """
        return self._smartctl

    @smartctl.setter
    def smartctl(self, smartctl: SmartNvmeSmartctl):
        """Sets the smartctl of this SmartSsd.


        :param smartctl: The smartctl of this SmartSsd.
        :type smartctl: SmartNvmeSmartctl
        """

        self._smartctl = smartctl

    @property
    def device(self) -> SmartNvmeDevice:
        """Gets the device of this SmartSsd.


        :return: The device of this SmartSsd.
        :rtype: SmartNvmeDevice
        """
        return self._device

    @device.setter
    def device(self, device: SmartNvmeDevice):
        """Sets the device of this SmartSsd.


        :param device: The device of this SmartSsd.
        :type device: SmartNvmeDevice
        """

        self._device = device

    @property
    def model_family(self) -> str:
        """Gets the model_family of this SmartSsd.


        :return: The model_family of this SmartSsd.
        :rtype: str
        """
        return self._model_family

    @model_family.setter
    def model_family(self, model_family: str):
        """Sets the model_family of this SmartSsd.


        :param model_family: The model_family of this SmartSsd.
        :type model_family: str
        """

        self._model_family = model_family

    @property
    def model_name(self) -> str:
        """Gets the model_name of this SmartSsd.


        :return: The model_name of this SmartSsd.
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name: str):
        """Sets the model_name of this SmartSsd.


        :param model_name: The model_name of this SmartSsd.
        :type model_name: str
        """

        self._model_name = model_name

    @property
    def serial_number(self) -> str:
        """Gets the serial_number of this SmartSsd.


        :return: The serial_number of this SmartSsd.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number: str):
        """Sets the serial_number of this SmartSsd.


        :param serial_number: The serial_number of this SmartSsd.
        :type serial_number: str
        """

        self._serial_number = serial_number

    @property
    def wwn(self) -> SmartSsdWwn:
        """Gets the wwn of this SmartSsd.


        :return: The wwn of this SmartSsd.
        :rtype: SmartSsdWwn
        """
        return self._wwn

    @wwn.setter
    def wwn(self, wwn: SmartSsdWwn):
        """Sets the wwn of this SmartSsd.


        :param wwn: The wwn of this SmartSsd.
        :type wwn: SmartSsdWwn
        """

        self._wwn = wwn

    @property
    def firmware_version(self) -> str:
        """Gets the firmware_version of this SmartSsd.


        :return: The firmware_version of this SmartSsd.
        :rtype: str
        """
        return self._firmware_version

    @firmware_version.setter
    def firmware_version(self, firmware_version: str):
        """Sets the firmware_version of this SmartSsd.


        :param firmware_version: The firmware_version of this SmartSsd.
        :type firmware_version: str
        """

        self._firmware_version = firmware_version

    @property
    def user_capacity(self) -> SmartSsdUserCapacity:
        """Gets the user_capacity of this SmartSsd.


        :return: The user_capacity of this SmartSsd.
        :rtype: SmartSsdUserCapacity
        """
        return self._user_capacity

    @user_capacity.setter
    def user_capacity(self, user_capacity: SmartSsdUserCapacity):
        """Sets the user_capacity of this SmartSsd.


        :param user_capacity: The user_capacity of this SmartSsd.
        :type user_capacity: SmartSsdUserCapacity
        """

        self._user_capacity = user_capacity

    @property
    def logical_block_size(self) -> int:
        """Gets the logical_block_size of this SmartSsd.


        :return: The logical_block_size of this SmartSsd.
        :rtype: int
        """
        return self._logical_block_size

    @logical_block_size.setter
    def logical_block_size(self, logical_block_size: int):
        """Sets the logical_block_size of this SmartSsd.


        :param logical_block_size: The logical_block_size of this SmartSsd.
        :type logical_block_size: int
        """

        self._logical_block_size = logical_block_size

    @property
    def physical_block_size(self) -> int:
        """Gets the physical_block_size of this SmartSsd.


        :return: The physical_block_size of this SmartSsd.
        :rtype: int
        """
        return self._physical_block_size

    @physical_block_size.setter
    def physical_block_size(self, physical_block_size: int):
        """Sets the physical_block_size of this SmartSsd.


        :param physical_block_size: The physical_block_size of this SmartSsd.
        :type physical_block_size: int
        """

        self._physical_block_size = physical_block_size

    @property
    def rotation_rate(self) -> int:
        """Gets the rotation_rate of this SmartSsd.


        :return: The rotation_rate of this SmartSsd.
        :rtype: int
        """
        return self._rotation_rate

    @rotation_rate.setter
    def rotation_rate(self, rotation_rate: int):
        """Sets the rotation_rate of this SmartSsd.


        :param rotation_rate: The rotation_rate of this SmartSsd.
        :type rotation_rate: int
        """

        self._rotation_rate = rotation_rate

    @property
    def form_factor(self) -> SmartSsdFormFactor:
        """Gets the form_factor of this SmartSsd.


        :return: The form_factor of this SmartSsd.
        :rtype: SmartSsdFormFactor
        """
        return self._form_factor

    @form_factor.setter
    def form_factor(self, form_factor: SmartSsdFormFactor):
        """Sets the form_factor of this SmartSsd.


        :param form_factor: The form_factor of this SmartSsd.
        :type form_factor: SmartSsdFormFactor
        """

        self._form_factor = form_factor

    @property
    def in_smartctl_database(self) -> bool:
        """Gets the in_smartctl_database of this SmartSsd.


        :return: The in_smartctl_database of this SmartSsd.
        :rtype: bool
        """
        return self._in_smartctl_database

    @in_smartctl_database.setter
    def in_smartctl_database(self, in_smartctl_database: bool):
        """Sets the in_smartctl_database of this SmartSsd.


        :param in_smartctl_database: The in_smartctl_database of this SmartSsd.
        :type in_smartctl_database: bool
        """

        self._in_smartctl_database = in_smartctl_database

    @property
    def ata_version(self) -> SmartSsdAtaVersion:
        """Gets the ata_version of this SmartSsd.


        :return: The ata_version of this SmartSsd.
        :rtype: SmartSsdAtaVersion
        """
        return self._ata_version

    @ata_version.setter
    def ata_version(self, ata_version: SmartSsdAtaVersion):
        """Sets the ata_version of this SmartSsd.


        :param ata_version: The ata_version of this SmartSsd.
        :type ata_version: SmartSsdAtaVersion
        """

        self._ata_version = ata_version

    @property
    def sata_version(self) -> SmartSsdSataVersion:
        """Gets the sata_version of this SmartSsd.


        :return: The sata_version of this SmartSsd.
        :rtype: SmartSsdSataVersion
        """
        return self._sata_version

    @sata_version.setter
    def sata_version(self, sata_version: SmartSsdSataVersion):
        """Sets the sata_version of this SmartSsd.


        :param sata_version: The sata_version of this SmartSsd.
        :type sata_version: SmartSsdSataVersion
        """

        self._sata_version = sata_version

    @property
    def interface_speed(self) -> SmartSsdInterfaceSpeed:
        """Gets the interface_speed of this SmartSsd.


        :return: The interface_speed of this SmartSsd.
        :rtype: SmartSsdInterfaceSpeed
        """
        return self._interface_speed

    @interface_speed.setter
    def interface_speed(self, interface_speed: SmartSsdInterfaceSpeed):
        """Sets the interface_speed of this SmartSsd.


        :param interface_speed: The interface_speed of this SmartSsd.
        :type interface_speed: SmartSsdInterfaceSpeed
        """

        self._interface_speed = interface_speed

    @property
    def local_time(self) -> SmartNvmeLocalTime:
        """Gets the local_time of this SmartSsd.


        :return: The local_time of this SmartSsd.
        :rtype: SmartNvmeLocalTime
        """
        return self._local_time

    @local_time.setter
    def local_time(self, local_time: SmartNvmeLocalTime):
        """Sets the local_time of this SmartSsd.


        :param local_time: The local_time of this SmartSsd.
        :type local_time: SmartNvmeLocalTime
        """

        self._local_time = local_time

    @property
    def read_lookahead(self) -> SmartSsdReadLookahead:
        """Gets the read_lookahead of this SmartSsd.


        :return: The read_lookahead of this SmartSsd.
        :rtype: SmartSsdReadLookahead
        """
        return self._read_lookahead

    @read_lookahead.setter
    def read_lookahead(self, read_lookahead: SmartSsdReadLookahead):
        """Sets the read_lookahead of this SmartSsd.


        :param read_lookahead: The read_lookahead of this SmartSsd.
        :type read_lookahead: SmartSsdReadLookahead
        """

        self._read_lookahead = read_lookahead

    @property
    def write_cache(self) -> SmartSsdReadLookahead:
        """Gets the write_cache of this SmartSsd.


        :return: The write_cache of this SmartSsd.
        :rtype: SmartSsdReadLookahead
        """
        return self._write_cache

    @write_cache.setter
    def write_cache(self, write_cache: SmartSsdReadLookahead):
        """Sets the write_cache of this SmartSsd.


        :param write_cache: The write_cache of this SmartSsd.
        :type write_cache: SmartSsdReadLookahead
        """

        self._write_cache = write_cache

    @property
    def ata_security(self) -> SmartSsdAtaSecurity:
        """Gets the ata_security of this SmartSsd.


        :return: The ata_security of this SmartSsd.
        :rtype: SmartSsdAtaSecurity
        """
        return self._ata_security

    @ata_security.setter
    def ata_security(self, ata_security: SmartSsdAtaSecurity):
        """Sets the ata_security of this SmartSsd.


        :param ata_security: The ata_security of this SmartSsd.
        :type ata_security: SmartSsdAtaSecurity
        """

        self._ata_security = ata_security

    @property
    def smart_status(self) -> SmartSsdSmartStatus:
        """Gets the smart_status of this SmartSsd.


        :return: The smart_status of this SmartSsd.
        :rtype: SmartSsdSmartStatus
        """
        return self._smart_status

    @smart_status.setter
    def smart_status(self, smart_status: SmartSsdSmartStatus):
        """Sets the smart_status of this SmartSsd.


        :param smart_status: The smart_status of this SmartSsd.
        :type smart_status: SmartSsdSmartStatus
        """

        self._smart_status = smart_status

    @property
    def ata_smart_data(self) -> SmartSsdAtaSmartData:
        """Gets the ata_smart_data of this SmartSsd.


        :return: The ata_smart_data of this SmartSsd.
        :rtype: SmartSsdAtaSmartData
        """
        return self._ata_smart_data

    @ata_smart_data.setter
    def ata_smart_data(self, ata_smart_data: SmartSsdAtaSmartData):
        """Sets the ata_smart_data of this SmartSsd.


        :param ata_smart_data: The ata_smart_data of this SmartSsd.
        :type ata_smart_data: SmartSsdAtaSmartData
        """

        self._ata_smart_data = ata_smart_data

    @property
    def ata_sct_capabilities(self) -> SmartSsdAtaSctCapabilities:
        """Gets the ata_sct_capabilities of this SmartSsd.


        :return: The ata_sct_capabilities of this SmartSsd.
        :rtype: SmartSsdAtaSctCapabilities
        """
        return self._ata_sct_capabilities

    @ata_sct_capabilities.setter
    def ata_sct_capabilities(self, ata_sct_capabilities: SmartSsdAtaSctCapabilities):
        """Sets the ata_sct_capabilities of this SmartSsd.


        :param ata_sct_capabilities: The ata_sct_capabilities of this SmartSsd.
        :type ata_sct_capabilities: SmartSsdAtaSctCapabilities
        """

        self._ata_sct_capabilities = ata_sct_capabilities

    @property
    def ata_smart_attributes(self) -> SmartSsdAtaSmartAttributes:
        """Gets the ata_smart_attributes of this SmartSsd.


        :return: The ata_smart_attributes of this SmartSsd.
        :rtype: SmartSsdAtaSmartAttributes
        """
        return self._ata_smart_attributes

    @ata_smart_attributes.setter
    def ata_smart_attributes(self, ata_smart_attributes: SmartSsdAtaSmartAttributes):
        """Sets the ata_smart_attributes of this SmartSsd.


        :param ata_smart_attributes: The ata_smart_attributes of this SmartSsd.
        :type ata_smart_attributes: SmartSsdAtaSmartAttributes
        """

        self._ata_smart_attributes = ata_smart_attributes

    @property
    def temperature(self) -> SmartSsdTemperature:
        """Gets the temperature of this SmartSsd.


        :return: The temperature of this SmartSsd.
        :rtype: SmartSsdTemperature
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature: SmartSsdTemperature):
        """Sets the temperature of this SmartSsd.


        :param temperature: The temperature of this SmartSsd.
        :type temperature: SmartSsdTemperature
        """

        self._temperature = temperature

    @property
    def ata_log_directory(self) -> SmartSsdAtaLogDirectory:
        """Gets the ata_log_directory of this SmartSsd.


        :return: The ata_log_directory of this SmartSsd.
        :rtype: SmartSsdAtaLogDirectory
        """
        return self._ata_log_directory

    @ata_log_directory.setter
    def ata_log_directory(self, ata_log_directory: SmartSsdAtaLogDirectory):
        """Sets the ata_log_directory of this SmartSsd.


        :param ata_log_directory: The ata_log_directory of this SmartSsd.
        :type ata_log_directory: SmartSsdAtaLogDirectory
        """

        self._ata_log_directory = ata_log_directory

    @property
    def ata_smart_error_log(self) -> SmartSsdAtaSmartErrorLog:
        """Gets the ata_smart_error_log of this SmartSsd.


        :return: The ata_smart_error_log of this SmartSsd.
        :rtype: SmartSsdAtaSmartErrorLog
        """
        return self._ata_smart_error_log

    @ata_smart_error_log.setter
    def ata_smart_error_log(self, ata_smart_error_log: SmartSsdAtaSmartErrorLog):
        """Sets the ata_smart_error_log of this SmartSsd.


        :param ata_smart_error_log: The ata_smart_error_log of this SmartSsd.
        :type ata_smart_error_log: SmartSsdAtaSmartErrorLog
        """

        self._ata_smart_error_log = ata_smart_error_log

    @property
    def ata_smart_self_test_log(self) -> SmartSsdAtaSmartErrorLog:
        """Gets the ata_smart_self_test_log of this SmartSsd.


        :return: The ata_smart_self_test_log of this SmartSsd.
        :rtype: SmartSsdAtaSmartErrorLog
        """
        return self._ata_smart_self_test_log

    @ata_smart_self_test_log.setter
    def ata_smart_self_test_log(self, ata_smart_self_test_log: SmartSsdAtaSmartErrorLog):
        """Sets the ata_smart_self_test_log of this SmartSsd.


        :param ata_smart_self_test_log: The ata_smart_self_test_log of this SmartSsd.
        :type ata_smart_self_test_log: SmartSsdAtaSmartErrorLog
        """

        self._ata_smart_self_test_log = ata_smart_self_test_log

    @property
    def ata_sct_status(self) -> SmartSsdAtaSctStatus:
        """Gets the ata_sct_status of this SmartSsd.


        :return: The ata_sct_status of this SmartSsd.
        :rtype: SmartSsdAtaSctStatus
        """
        return self._ata_sct_status

    @ata_sct_status.setter
    def ata_sct_status(self, ata_sct_status: SmartSsdAtaSctStatus):
        """Sets the ata_sct_status of this SmartSsd.


        :param ata_sct_status: The ata_sct_status of this SmartSsd.
        :type ata_sct_status: SmartSsdAtaSctStatus
        """

        self._ata_sct_status = ata_sct_status

    @property
    def ata_sct_temperature_history(self) -> SmartSsdAtaSctTemperatureHistory:
        """Gets the ata_sct_temperature_history of this SmartSsd.


        :return: The ata_sct_temperature_history of this SmartSsd.
        :rtype: SmartSsdAtaSctTemperatureHistory
        """
        return self._ata_sct_temperature_history

    @ata_sct_temperature_history.setter
    def ata_sct_temperature_history(self, ata_sct_temperature_history: SmartSsdAtaSctTemperatureHistory):
        """Sets the ata_sct_temperature_history of this SmartSsd.


        :param ata_sct_temperature_history: The ata_sct_temperature_history of this SmartSsd.
        :type ata_sct_temperature_history: SmartSsdAtaSctTemperatureHistory
        """

        self._ata_sct_temperature_history = ata_sct_temperature_history

    @property
    def ata_sct_erc(self) -> SmartSsdAtaSctErc:
        """Gets the ata_sct_erc of this SmartSsd.


        :return: The ata_sct_erc of this SmartSsd.
        :rtype: SmartSsdAtaSctErc
        """
        return self._ata_sct_erc

    @ata_sct_erc.setter
    def ata_sct_erc(self, ata_sct_erc: SmartSsdAtaSctErc):
        """Sets the ata_sct_erc of this SmartSsd.


        :param ata_sct_erc: The ata_sct_erc of this SmartSsd.
        :type ata_sct_erc: SmartSsdAtaSctErc
        """

        self._ata_sct_erc = ata_sct_erc

    @property
    def sata_phy_event_counters(self) -> SmartSsdSataPhyEventCounters:
        """Gets the sata_phy_event_counters of this SmartSsd.


        :return: The sata_phy_event_counters of this SmartSsd.
        :rtype: SmartSsdSataPhyEventCounters
        """
        return self._sata_phy_event_counters

    @sata_phy_event_counters.setter
    def sata_phy_event_counters(self, sata_phy_event_counters: SmartSsdSataPhyEventCounters):
        """Sets the sata_phy_event_counters of this SmartSsd.


        :param sata_phy_event_counters: The sata_phy_event_counters of this SmartSsd.
        :type sata_phy_event_counters: SmartSsdSataPhyEventCounters
        """

        self._sata_phy_event_counters = sata_phy_event_counters