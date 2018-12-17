import connexion
import six

from swagger_server.models.smart_nvme import SmartNvme  # noqa: E501
from swagger_server.models.smart_ssd import SmartSsd  # noqa: E501
from swagger_server import util
from src import manager


def add_smart_nvme(smartNvme):  # noqa: E501
    """Upload NVME disk data

     # noqa: E501

    :param smartNvme: Smartctl --json -x output to be added to dataset
    :type smartNvme: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        smartNvme = SmartNvme.from_dict(connexion.request.get_json())  # noqa: E501
    manager.add_smart_nvme(smartNvme)
    return 'do some magic!'


def add_smart_ssd(smartSsd):  # noqa: E501
    """Upload ssd disk data

     # noqa: E501

    :param smartSsd: Smartctl --json -x output to be added to dataset
    :type smartSsd: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        smartSsd = SmartSsd.from_dict(connexion.request.get_json())  # noqa: E501
    manager.add_smart_ssd(smartSsd)
    return 'do some magic!'


def get_smart_nvme():  # noqa: E501
    """Get all NVME disk data

     # noqa: E501


    :rtype: None
    """

    return manager.get_smart_nvme()


def get_smart_ssd():  # noqa: E501
    """Get all ssd disk data

     # noqa: E501


    :rtype: None
    """
    return manager.get_smart_ssd()
