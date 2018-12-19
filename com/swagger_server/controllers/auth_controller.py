import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def get_smart_nvme(UUID=None):  # noqa: E501
    """Get all NVME disk data

     # noqa: E501

    :param UUID: Unique User ID
    :type UUID: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'
