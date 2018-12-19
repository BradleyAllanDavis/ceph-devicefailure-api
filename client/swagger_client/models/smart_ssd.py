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

from swagger_client.models.smart_nvme_device import SmartNvmeDevice  # noqa: F401,E501
from swagger_client.models.smart_nvme_local_time import SmartNvmeLocalTime  # noqa: F401,E501
from swagger_client.models.smart_nvme_smartctl import SmartNvmeSmartctl  # noqa: F401,E501
from swagger_client.models.smart_ssd_ata_log_directory import SmartSsdAtaLogDirectory  # noqa: F401,E501
from swagger_client.models.smart_ssd_ata_sct_capabilities import SmartSsdAtaSctCapabilities  # noqa: F401,E501
from swagger_client.models.smart_ssd_ata_sct_erc import SmartSsdAtaSctErc  # noqa: F401,E501
from swagger_client.models.smart_ssd_ata_sct_status import SmartSsdAtaSctStatus  # noqa: F401,E501
from swagger_client.models.smart_ssd_ata_sct_temperature_history import SmartSsdAtaSctTemperatureHistory  # noqa: F401,E501
from swagger_client.models.smart_ssd_ata_security import SmartSsdAtaSecurity  # noqa: F401,E501
from swagger_client.models.smart_ssd_ata_smart_attributes import SmartSsdAtaSmartAttributes  # noqa: F401,E501
from swagger_client.models.smart_ssd_ata_smart_data import SmartSsdAtaSmartData  # noqa: F401,E501
from swagger_client.models.smart_ssd_ata_smart_error_log import SmartSsdAtaSmartErrorLog  # noqa: F401,E501
from swagger_client.models.smart_ssd_ata_version import SmartSsdAtaVersion  # noqa: F401,E501
from swagger_client.models.smart_ssd_form_factor import SmartSsdFormFactor  # noqa: F401,E501
from swagger_client.models.smart_ssd_interface_speed import SmartSsdInterfaceSpeed  # noqa: F401,E501
from swagger_client.models.smart_ssd_read_lookahead import SmartSsdReadLookahead  # noqa: F401,E501
from swagger_client.models.smart_ssd_sata_phy_event_counters import SmartSsdSataPhyEventCounters  # noqa: F401,E501
from swagger_client.models.smart_ssd_sata_version import SmartSsdSataVersion  # noqa: F401,E501
from swagger_client.models.smart_ssd_smart_status import SmartSsdSmartStatus  # noqa: F401,E501
from swagger_client.models.smart_ssd_temperature import SmartSsdTemperature  # noqa: F401,E501
from swagger_client.models.smart_ssd_user_capacity import SmartSsdUserCapacity  # noqa: F401,E501
from swagger_client.models.smart_ssd_wwn import SmartSsdWwn  # noqa: F401,E501


class SmartSsd(object):
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
        'json_format_version': 'list[int]',
        'smartctl': 'SmartNvmeSmartctl',
        'device': 'SmartNvmeDevice',
        'model_family': 'str',
        'model_name': 'str',
        'serial_number': 'str',
        'wwn': 'SmartSsdWwn',
        'firmware_version': 'str',
        'user_capacity': 'SmartSsdUserCapacity',
        'logical_block_size': 'int',
        'physical_block_size': 'int',
        'rotation_rate': 'int',
        'form_factor': 'SmartSsdFormFactor',
        'in_smartctl_database': 'bool',
        'ata_version': 'SmartSsdAtaVersion',
        'sata_version': 'SmartSsdSataVersion',
        'interface_speed': 'SmartSsdInterfaceSpeed',
        'local_time': 'SmartNvmeLocalTime',
        'read_lookahead': 'SmartSsdReadLookahead',
        'write_cache': 'SmartSsdReadLookahead',
        'ata_security': 'SmartSsdAtaSecurity',
        'smart_status': 'SmartSsdSmartStatus',
        'ata_smart_data': 'SmartSsdAtaSmartData',
        'ata_sct_capabilities': 'SmartSsdAtaSctCapabilities',
        'ata_smart_attributes': 'SmartSsdAtaSmartAttributes',
        'temperature': 'SmartSsdTemperature',
        'ata_log_directory': 'SmartSsdAtaLogDirectory',
        'ata_smart_error_log': 'SmartSsdAtaSmartErrorLog',
        'ata_smart_self_test_log': 'SmartSsdAtaSmartErrorLog',
        'ata_sct_status': 'SmartSsdAtaSctStatus',
        'ata_sct_temperature_history': 'SmartSsdAtaSctTemperatureHistory',
        'ata_sct_erc': 'SmartSsdAtaSctErc',
        'sata_phy_event_counters': 'SmartSsdSataPhyEventCounters'
    }

    attribute_map = {
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

    def __init__(self, json_format_version=None, smartctl=None, device=None, model_family=None, model_name=None, serial_number=None, wwn=None, firmware_version=None, user_capacity=None, logical_block_size=None, physical_block_size=None, rotation_rate=None, form_factor=None, in_smartctl_database=None, ata_version=None, sata_version=None, interface_speed=None, local_time=None, read_lookahead=None, write_cache=None, ata_security=None, smart_status=None, ata_smart_data=None, ata_sct_capabilities=None, ata_smart_attributes=None, temperature=None, ata_log_directory=None, ata_smart_error_log=None, ata_smart_self_test_log=None, ata_sct_status=None, ata_sct_temperature_history=None, ata_sct_erc=None, sata_phy_event_counters=None):  # noqa: E501
        """SmartSsd - a model defined in Swagger"""  # noqa: E501

        self._json_format_version = None
        self._smartctl = None
        self._device = None
        self._model_family = None
        self._model_name = None
        self._serial_number = None
        self._wwn = None
        self._firmware_version = None
        self._user_capacity = None
        self._logical_block_size = None
        self._physical_block_size = None
        self._rotation_rate = None
        self._form_factor = None
        self._in_smartctl_database = None
        self._ata_version = None
        self._sata_version = None
        self._interface_speed = None
        self._local_time = None
        self._read_lookahead = None
        self._write_cache = None
        self._ata_security = None
        self._smart_status = None
        self._ata_smart_data = None
        self._ata_sct_capabilities = None
        self._ata_smart_attributes = None
        self._temperature = None
        self._ata_log_directory = None
        self._ata_smart_error_log = None
        self._ata_smart_self_test_log = None
        self._ata_sct_status = None
        self._ata_sct_temperature_history = None
        self._ata_sct_erc = None
        self._sata_phy_event_counters = None
        self.discriminator = None

        if json_format_version is not None:
            self.json_format_version = json_format_version
        if smartctl is not None:
            self.smartctl = smartctl
        if device is not None:
            self.device = device
        if model_family is not None:
            self.model_family = model_family
        if model_name is not None:
            self.model_name = model_name
        if serial_number is not None:
            self.serial_number = serial_number
        if wwn is not None:
            self.wwn = wwn
        if firmware_version is not None:
            self.firmware_version = firmware_version
        if user_capacity is not None:
            self.user_capacity = user_capacity
        if logical_block_size is not None:
            self.logical_block_size = logical_block_size
        if physical_block_size is not None:
            self.physical_block_size = physical_block_size
        if rotation_rate is not None:
            self.rotation_rate = rotation_rate
        if form_factor is not None:
            self.form_factor = form_factor
        if in_smartctl_database is not None:
            self.in_smartctl_database = in_smartctl_database
        if ata_version is not None:
            self.ata_version = ata_version
        if sata_version is not None:
            self.sata_version = sata_version
        if interface_speed is not None:
            self.interface_speed = interface_speed
        if local_time is not None:
            self.local_time = local_time
        if read_lookahead is not None:
            self.read_lookahead = read_lookahead
        if write_cache is not None:
            self.write_cache = write_cache
        if ata_security is not None:
            self.ata_security = ata_security
        if smart_status is not None:
            self.smart_status = smart_status
        if ata_smart_data is not None:
            self.ata_smart_data = ata_smart_data
        if ata_sct_capabilities is not None:
            self.ata_sct_capabilities = ata_sct_capabilities
        if ata_smart_attributes is not None:
            self.ata_smart_attributes = ata_smart_attributes
        if temperature is not None:
            self.temperature = temperature
        if ata_log_directory is not None:
            self.ata_log_directory = ata_log_directory
        if ata_smart_error_log is not None:
            self.ata_smart_error_log = ata_smart_error_log
        if ata_smart_self_test_log is not None:
            self.ata_smart_self_test_log = ata_smart_self_test_log
        if ata_sct_status is not None:
            self.ata_sct_status = ata_sct_status
        if ata_sct_temperature_history is not None:
            self.ata_sct_temperature_history = ata_sct_temperature_history
        if ata_sct_erc is not None:
            self.ata_sct_erc = ata_sct_erc
        if sata_phy_event_counters is not None:
            self.sata_phy_event_counters = sata_phy_event_counters

    @property
    def json_format_version(self):
        """Gets the json_format_version of this SmartSsd.  # noqa: E501


        :return: The json_format_version of this SmartSsd.  # noqa: E501
        :rtype: list[int]
        """
        return self._json_format_version

    @json_format_version.setter
    def json_format_version(self, json_format_version):
        """Sets the json_format_version of this SmartSsd.


        :param json_format_version: The json_format_version of this SmartSsd.  # noqa: E501
        :type: list[int]
        """

        self._json_format_version = json_format_version

    @property
    def smartctl(self):
        """Gets the smartctl of this SmartSsd.  # noqa: E501


        :return: The smartctl of this SmartSsd.  # noqa: E501
        :rtype: SmartNvmeSmartctl
        """
        return self._smartctl

    @smartctl.setter
    def smartctl(self, smartctl):
        """Sets the smartctl of this SmartSsd.


        :param smartctl: The smartctl of this SmartSsd.  # noqa: E501
        :type: SmartNvmeSmartctl
        """

        self._smartctl = smartctl

    @property
    def device(self):
        """Gets the device of this SmartSsd.  # noqa: E501


        :return: The device of this SmartSsd.  # noqa: E501
        :rtype: SmartNvmeDevice
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this SmartSsd.


        :param device: The device of this SmartSsd.  # noqa: E501
        :type: SmartNvmeDevice
        """

        self._device = device

    @property
    def model_family(self):
        """Gets the model_family of this SmartSsd.  # noqa: E501


        :return: The model_family of this SmartSsd.  # noqa: E501
        :rtype: str
        """
        return self._model_family

    @model_family.setter
    def model_family(self, model_family):
        """Sets the model_family of this SmartSsd.


        :param model_family: The model_family of this SmartSsd.  # noqa: E501
        :type: str
        """

        self._model_family = model_family

    @property
    def model_name(self):
        """Gets the model_name of this SmartSsd.  # noqa: E501


        :return: The model_name of this SmartSsd.  # noqa: E501
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this SmartSsd.


        :param model_name: The model_name of this SmartSsd.  # noqa: E501
        :type: str
        """

        self._model_name = model_name

    @property
    def serial_number(self):
        """Gets the serial_number of this SmartSsd.  # noqa: E501


        :return: The serial_number of this SmartSsd.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this SmartSsd.


        :param serial_number: The serial_number of this SmartSsd.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def wwn(self):
        """Gets the wwn of this SmartSsd.  # noqa: E501


        :return: The wwn of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdWwn
        """
        return self._wwn

    @wwn.setter
    def wwn(self, wwn):
        """Sets the wwn of this SmartSsd.


        :param wwn: The wwn of this SmartSsd.  # noqa: E501
        :type: SmartSsdWwn
        """

        self._wwn = wwn

    @property
    def firmware_version(self):
        """Gets the firmware_version of this SmartSsd.  # noqa: E501


        :return: The firmware_version of this SmartSsd.  # noqa: E501
        :rtype: str
        """
        return self._firmware_version

    @firmware_version.setter
    def firmware_version(self, firmware_version):
        """Sets the firmware_version of this SmartSsd.


        :param firmware_version: The firmware_version of this SmartSsd.  # noqa: E501
        :type: str
        """

        self._firmware_version = firmware_version

    @property
    def user_capacity(self):
        """Gets the user_capacity of this SmartSsd.  # noqa: E501


        :return: The user_capacity of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdUserCapacity
        """
        return self._user_capacity

    @user_capacity.setter
    def user_capacity(self, user_capacity):
        """Sets the user_capacity of this SmartSsd.


        :param user_capacity: The user_capacity of this SmartSsd.  # noqa: E501
        :type: SmartSsdUserCapacity
        """

        self._user_capacity = user_capacity

    @property
    def logical_block_size(self):
        """Gets the logical_block_size of this SmartSsd.  # noqa: E501


        :return: The logical_block_size of this SmartSsd.  # noqa: E501
        :rtype: int
        """
        return self._logical_block_size

    @logical_block_size.setter
    def logical_block_size(self, logical_block_size):
        """Sets the logical_block_size of this SmartSsd.


        :param logical_block_size: The logical_block_size of this SmartSsd.  # noqa: E501
        :type: int
        """

        self._logical_block_size = logical_block_size

    @property
    def physical_block_size(self):
        """Gets the physical_block_size of this SmartSsd.  # noqa: E501


        :return: The physical_block_size of this SmartSsd.  # noqa: E501
        :rtype: int
        """
        return self._physical_block_size

    @physical_block_size.setter
    def physical_block_size(self, physical_block_size):
        """Sets the physical_block_size of this SmartSsd.


        :param physical_block_size: The physical_block_size of this SmartSsd.  # noqa: E501
        :type: int
        """

        self._physical_block_size = physical_block_size

    @property
    def rotation_rate(self):
        """Gets the rotation_rate of this SmartSsd.  # noqa: E501


        :return: The rotation_rate of this SmartSsd.  # noqa: E501
        :rtype: int
        """
        return self._rotation_rate

    @rotation_rate.setter
    def rotation_rate(self, rotation_rate):
        """Sets the rotation_rate of this SmartSsd.


        :param rotation_rate: The rotation_rate of this SmartSsd.  # noqa: E501
        :type: int
        """

        self._rotation_rate = rotation_rate

    @property
    def form_factor(self):
        """Gets the form_factor of this SmartSsd.  # noqa: E501


        :return: The form_factor of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdFormFactor
        """
        return self._form_factor

    @form_factor.setter
    def form_factor(self, form_factor):
        """Sets the form_factor of this SmartSsd.


        :param form_factor: The form_factor of this SmartSsd.  # noqa: E501
        :type: SmartSsdFormFactor
        """

        self._form_factor = form_factor

    @property
    def in_smartctl_database(self):
        """Gets the in_smartctl_database of this SmartSsd.  # noqa: E501


        :return: The in_smartctl_database of this SmartSsd.  # noqa: E501
        :rtype: bool
        """
        return self._in_smartctl_database

    @in_smartctl_database.setter
    def in_smartctl_database(self, in_smartctl_database):
        """Sets the in_smartctl_database of this SmartSsd.


        :param in_smartctl_database: The in_smartctl_database of this SmartSsd.  # noqa: E501
        :type: bool
        """

        self._in_smartctl_database = in_smartctl_database

    @property
    def ata_version(self):
        """Gets the ata_version of this SmartSsd.  # noqa: E501


        :return: The ata_version of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdAtaVersion
        """
        return self._ata_version

    @ata_version.setter
    def ata_version(self, ata_version):
        """Sets the ata_version of this SmartSsd.


        :param ata_version: The ata_version of this SmartSsd.  # noqa: E501
        :type: SmartSsdAtaVersion
        """

        self._ata_version = ata_version

    @property
    def sata_version(self):
        """Gets the sata_version of this SmartSsd.  # noqa: E501


        :return: The sata_version of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdSataVersion
        """
        return self._sata_version

    @sata_version.setter
    def sata_version(self, sata_version):
        """Sets the sata_version of this SmartSsd.


        :param sata_version: The sata_version of this SmartSsd.  # noqa: E501
        :type: SmartSsdSataVersion
        """

        self._sata_version = sata_version

    @property
    def interface_speed(self):
        """Gets the interface_speed of this SmartSsd.  # noqa: E501


        :return: The interface_speed of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdInterfaceSpeed
        """
        return self._interface_speed

    @interface_speed.setter
    def interface_speed(self, interface_speed):
        """Sets the interface_speed of this SmartSsd.


        :param interface_speed: The interface_speed of this SmartSsd.  # noqa: E501
        :type: SmartSsdInterfaceSpeed
        """

        self._interface_speed = interface_speed

    @property
    def local_time(self):
        """Gets the local_time of this SmartSsd.  # noqa: E501


        :return: The local_time of this SmartSsd.  # noqa: E501
        :rtype: SmartNvmeLocalTime
        """
        return self._local_time

    @local_time.setter
    def local_time(self, local_time):
        """Sets the local_time of this SmartSsd.


        :param local_time: The local_time of this SmartSsd.  # noqa: E501
        :type: SmartNvmeLocalTime
        """

        self._local_time = local_time

    @property
    def read_lookahead(self):
        """Gets the read_lookahead of this SmartSsd.  # noqa: E501


        :return: The read_lookahead of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdReadLookahead
        """
        return self._read_lookahead

    @read_lookahead.setter
    def read_lookahead(self, read_lookahead):
        """Sets the read_lookahead of this SmartSsd.


        :param read_lookahead: The read_lookahead of this SmartSsd.  # noqa: E501
        :type: SmartSsdReadLookahead
        """

        self._read_lookahead = read_lookahead

    @property
    def write_cache(self):
        """Gets the write_cache of this SmartSsd.  # noqa: E501


        :return: The write_cache of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdReadLookahead
        """
        return self._write_cache

    @write_cache.setter
    def write_cache(self, write_cache):
        """Sets the write_cache of this SmartSsd.


        :param write_cache: The write_cache of this SmartSsd.  # noqa: E501
        :type: SmartSsdReadLookahead
        """

        self._write_cache = write_cache

    @property
    def ata_security(self):
        """Gets the ata_security of this SmartSsd.  # noqa: E501


        :return: The ata_security of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdAtaSecurity
        """
        return self._ata_security

    @ata_security.setter
    def ata_security(self, ata_security):
        """Sets the ata_security of this SmartSsd.


        :param ata_security: The ata_security of this SmartSsd.  # noqa: E501
        :type: SmartSsdAtaSecurity
        """

        self._ata_security = ata_security

    @property
    def smart_status(self):
        """Gets the smart_status of this SmartSsd.  # noqa: E501


        :return: The smart_status of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdSmartStatus
        """
        return self._smart_status

    @smart_status.setter
    def smart_status(self, smart_status):
        """Sets the smart_status of this SmartSsd.


        :param smart_status: The smart_status of this SmartSsd.  # noqa: E501
        :type: SmartSsdSmartStatus
        """

        self._smart_status = smart_status

    @property
    def ata_smart_data(self):
        """Gets the ata_smart_data of this SmartSsd.  # noqa: E501


        :return: The ata_smart_data of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdAtaSmartData
        """
        return self._ata_smart_data

    @ata_smart_data.setter
    def ata_smart_data(self, ata_smart_data):
        """Sets the ata_smart_data of this SmartSsd.


        :param ata_smart_data: The ata_smart_data of this SmartSsd.  # noqa: E501
        :type: SmartSsdAtaSmartData
        """

        self._ata_smart_data = ata_smart_data

    @property
    def ata_sct_capabilities(self):
        """Gets the ata_sct_capabilities of this SmartSsd.  # noqa: E501


        :return: The ata_sct_capabilities of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdAtaSctCapabilities
        """
        return self._ata_sct_capabilities

    @ata_sct_capabilities.setter
    def ata_sct_capabilities(self, ata_sct_capabilities):
        """Sets the ata_sct_capabilities of this SmartSsd.


        :param ata_sct_capabilities: The ata_sct_capabilities of this SmartSsd.  # noqa: E501
        :type: SmartSsdAtaSctCapabilities
        """

        self._ata_sct_capabilities = ata_sct_capabilities

    @property
    def ata_smart_attributes(self):
        """Gets the ata_smart_attributes of this SmartSsd.  # noqa: E501


        :return: The ata_smart_attributes of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdAtaSmartAttributes
        """
        return self._ata_smart_attributes

    @ata_smart_attributes.setter
    def ata_smart_attributes(self, ata_smart_attributes):
        """Sets the ata_smart_attributes of this SmartSsd.


        :param ata_smart_attributes: The ata_smart_attributes of this SmartSsd.  # noqa: E501
        :type: SmartSsdAtaSmartAttributes
        """

        self._ata_smart_attributes = ata_smart_attributes

    @property
    def temperature(self):
        """Gets the temperature of this SmartSsd.  # noqa: E501


        :return: The temperature of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdTemperature
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this SmartSsd.


        :param temperature: The temperature of this SmartSsd.  # noqa: E501
        :type: SmartSsdTemperature
        """

        self._temperature = temperature

    @property
    def ata_log_directory(self):
        """Gets the ata_log_directory of this SmartSsd.  # noqa: E501


        :return: The ata_log_directory of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdAtaLogDirectory
        """
        return self._ata_log_directory

    @ata_log_directory.setter
    def ata_log_directory(self, ata_log_directory):
        """Sets the ata_log_directory of this SmartSsd.


        :param ata_log_directory: The ata_log_directory of this SmartSsd.  # noqa: E501
        :type: SmartSsdAtaLogDirectory
        """

        self._ata_log_directory = ata_log_directory

    @property
    def ata_smart_error_log(self):
        """Gets the ata_smart_error_log of this SmartSsd.  # noqa: E501


        :return: The ata_smart_error_log of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdAtaSmartErrorLog
        """
        return self._ata_smart_error_log

    @ata_smart_error_log.setter
    def ata_smart_error_log(self, ata_smart_error_log):
        """Sets the ata_smart_error_log of this SmartSsd.


        :param ata_smart_error_log: The ata_smart_error_log of this SmartSsd.  # noqa: E501
        :type: SmartSsdAtaSmartErrorLog
        """

        self._ata_smart_error_log = ata_smart_error_log

    @property
    def ata_smart_self_test_log(self):
        """Gets the ata_smart_self_test_log of this SmartSsd.  # noqa: E501


        :return: The ata_smart_self_test_log of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdAtaSmartErrorLog
        """
        return self._ata_smart_self_test_log

    @ata_smart_self_test_log.setter
    def ata_smart_self_test_log(self, ata_smart_self_test_log):
        """Sets the ata_smart_self_test_log of this SmartSsd.


        :param ata_smart_self_test_log: The ata_smart_self_test_log of this SmartSsd.  # noqa: E501
        :type: SmartSsdAtaSmartErrorLog
        """

        self._ata_smart_self_test_log = ata_smart_self_test_log

    @property
    def ata_sct_status(self):
        """Gets the ata_sct_status of this SmartSsd.  # noqa: E501


        :return: The ata_sct_status of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdAtaSctStatus
        """
        return self._ata_sct_status

    @ata_sct_status.setter
    def ata_sct_status(self, ata_sct_status):
        """Sets the ata_sct_status of this SmartSsd.


        :param ata_sct_status: The ata_sct_status of this SmartSsd.  # noqa: E501
        :type: SmartSsdAtaSctStatus
        """

        self._ata_sct_status = ata_sct_status

    @property
    def ata_sct_temperature_history(self):
        """Gets the ata_sct_temperature_history of this SmartSsd.  # noqa: E501


        :return: The ata_sct_temperature_history of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdAtaSctTemperatureHistory
        """
        return self._ata_sct_temperature_history

    @ata_sct_temperature_history.setter
    def ata_sct_temperature_history(self, ata_sct_temperature_history):
        """Sets the ata_sct_temperature_history of this SmartSsd.


        :param ata_sct_temperature_history: The ata_sct_temperature_history of this SmartSsd.  # noqa: E501
        :type: SmartSsdAtaSctTemperatureHistory
        """

        self._ata_sct_temperature_history = ata_sct_temperature_history

    @property
    def ata_sct_erc(self):
        """Gets the ata_sct_erc of this SmartSsd.  # noqa: E501


        :return: The ata_sct_erc of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdAtaSctErc
        """
        return self._ata_sct_erc

    @ata_sct_erc.setter
    def ata_sct_erc(self, ata_sct_erc):
        """Sets the ata_sct_erc of this SmartSsd.


        :param ata_sct_erc: The ata_sct_erc of this SmartSsd.  # noqa: E501
        :type: SmartSsdAtaSctErc
        """

        self._ata_sct_erc = ata_sct_erc

    @property
    def sata_phy_event_counters(self):
        """Gets the sata_phy_event_counters of this SmartSsd.  # noqa: E501


        :return: The sata_phy_event_counters of this SmartSsd.  # noqa: E501
        :rtype: SmartSsdSataPhyEventCounters
        """
        return self._sata_phy_event_counters

    @sata_phy_event_counters.setter
    def sata_phy_event_counters(self, sata_phy_event_counters):
        """Sets the sata_phy_event_counters of this SmartSsd.


        :param sata_phy_event_counters: The sata_phy_event_counters of this SmartSsd.  # noqa: E501
        :type: SmartSsdSataPhyEventCounters
        """

        self._sata_phy_event_counters = sata_phy_event_counters

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
        if not isinstance(other, SmartSsd):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
