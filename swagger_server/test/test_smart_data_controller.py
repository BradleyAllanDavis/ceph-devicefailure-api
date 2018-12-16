# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.smart_nvme import SmartNvme  # noqa: E501
from swagger_server.models.smart_ssd import SmartSsd  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSmartDataController(BaseTestCase):
    """SmartDataController integration test stubs"""

    def test_add_smart_nvme(self):
        """Test case for add_smart_nvme

        Upload NVME disk data
        """
        smartSsd = SmartNvme()
        response = self.client.open(
            '/cs-739/DiskFailurePrediction/1.0.0/smart-nvme',
            method='POST',
            data=json.dumps(smartSsd),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_smart_ssd(self):
        """Test case for add_smart_ssd

        Upload ssd disk data
        """
        smartSsd = SmartSsd()
        response = self.client.open(
            '/cs-739/DiskFailurePrediction/1.0.0/smart-ssd',
            method='POST',
            data=json.dumps(smartSsd),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_smart_nvme(self):
        """Test case for get_smart_nvme

        Get all NVME disk data
        """
        response = self.client.open(
            '/cs-739/DiskFailurePrediction/1.0.0/smart-nvme',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_smart_ssd(self):
        """Test case for get_smart_ssd

        Get all ssd disk data
        """
        response = self.client.open(
            '/cs-739/DiskFailurePrediction/1.0.0/smart-ssd',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
