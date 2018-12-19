import json
import pymongo
from bson import json_util
from bson import ObjectId
from flask import Flask


app = Flask(__name__)

# open up database connection
client = pymongo.MongoClient("localhost", 27017)
db = client["db"]
smartnvme_collection = db["smart_nvme"]
smartssd_collection = db["smart_ssd"]


# class JSONEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o)
#         return json.JSONEncoder.default(self, o)


def add_smart_nvme(smartNvme):  # noqa: E501
    """Upload NVME disk data

     # noqa: E501

    :param smartNvme: Smartctl --json -x output to be added to dataset
    :type smartNvme: dict | bytes

    :rtype: None
    """
    app.logger.info('manager.add_smart_nvme()')
    dct = smartNvme.to_dict()
    smartnvme_id = smartnvme_collection.insert_one(dct).inserted_id
    app.logger.info('smartnvme_id = ' + str(smartnvme_id))


def add_smart_ssd(smartSsd):  # noqa: E501
    """Upload ssd disk data

     # noqa: E501

    :param smartSsd: Smartctl --json -x output to be added to dataset
    :type smartSsd: dict | bytes

    :rtype: None
    """
    app.logger.info('manager.add_smart_ssd()')
    dct = smartSsd.to_dict()
    smartssd_id = smartssd_collection.insert_one(dct).inserted_id
    app.logger.info('smartssd_id = ' + str(smartssd_id))


def get_smart_nvme():  # noqa: E501
    """Get all NVME disk data

     # noqa: E501


    :rtype: None
    """
    app.logger.info('manager.get_smart_nvme()')
    docs = list(smartnvme_collection.find())
    return json.dumps(docs, default=json_util.default)


def get_smart_ssd():  # noqa: E501
    """Get all ssd disk data

     # noqa: E501


    :rtype: None
    """
    app.logger.info('manager.get_smart_ssd()')
    docs = list(smartssd_collection.find())
    return json.dumps(docs, default=json_util.default)
