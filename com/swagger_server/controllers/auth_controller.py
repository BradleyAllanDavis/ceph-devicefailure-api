import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util
from src import manager


def get_auth(UUID=None):  # noqa: E501
    """Generate new UUID and API Key

     # noqa: E501

    :param UUID: Unique User ID
    :type UUID: str

    :rtype: InlineResponse200
    """
    return manager.get_auth(UUID)
