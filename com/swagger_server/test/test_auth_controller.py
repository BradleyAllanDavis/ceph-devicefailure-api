# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAuthController(BaseTestCase):
    """AuthController integration test stubs"""

    def test_get_smart_nvme(self):
        """Test case for get_smart_nvme

        Get all NVME disk data
        """
        query_string = [('UUID', 'UUID_example')]
        response = self.client.open(
            '/cs-739/DiskFailurePrediction/1.0.0/get_auth',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
