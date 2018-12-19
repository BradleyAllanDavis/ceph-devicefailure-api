import pymongo
from flask import Flask


# open up database connection
client = pymongo.MongoClient("localhost", 27017)
db = client["db"]
smartnvme_collection = db["smart_nvme"]
smartssd_collection = db["smart_ssd"]


def add_smart_nvme(smartNvme):  # noqa: E501
    """Upload NVME disk data

     # noqa: E501

    :param smartNvme: Smartctl --json -x output to be added to dataset
    :type smartNvme: dict | bytes

    :rtype: None
    """
    print('add_smart_nvme()')
    dct = smartNvme.to_dict()
    smartnvme_id = smartnvme_collection.insert_one(dct).inserted_id
    print('smartnvme_id = ' + str(smartnvme_id))
    # return 'success?'


def add_smart_ssd(smartSsd):  # noqa: E501
    """Upload ssd disk data

     # noqa: E501

    :param smartSsd: Smartctl --json -x output to be added to dataset
    :type smartSsd: dict | bytes

    :rtype: None
    """
    print('add_smart_ssd()')
    dct = smartSsd.to_dict()
    smartssd_id = smartssd_collection.insert_one(dct).inserted_id
    print('smartssd_id = ' + str(smartssd_id))
    # return 'success?'


def get_smart_nvme():  # noqa: E501
    """Get all NVME disk data

     # noqa: E501


    :rtype: None
    """
    print('get_smart_nvme()')
    # return 'success?'


def get_smart_ssd():  # noqa: E501
    """Get all ssd disk data

     # noqa: E501


    :rtype: None
    """
    print('get_smart_ssd()')
    # return 'success?'
