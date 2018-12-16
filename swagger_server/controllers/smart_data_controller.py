import connexion
import six

from swagger_server.models.smart_nvme import SmartNvme  # noqa: E501
from swagger_server.models.smart_ssd import SmartSsd  # noqa: E501
from swagger_server import util


def add_smart_nvme(smartSsd):  # noqa: E501
    """Upload NVME disk data

     # noqa: E501

    :param smartSsd: Smartctl --json -x output to be added to dataset
    :type smartSsd: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        smartSsd = SmartNvme.from_dict(connexion.request.get_json())  # noqa: E501

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
    return 'do some magic!'


def get_smart_nvme():  # noqa: E501
    """Get all NVME disk data

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def get_smart_ssd():  # noqa: E501
    """Get all ssd disk data

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
