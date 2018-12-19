import pymongo
from flask import Flask
import uuid
import hashlib
from swagger_server.models.inline_response200 import InlineResponse200
import connexion
from swagger_server.models.smart_nvme import SmartNvme

app = Flask(__name__)

# open up database connection
client = pymongo.MongoClient("localhost", 27017)
db = client["db"]
smartnvme_collection = db["smart_nvme"]
smartssd_collection = db["smart_ssd"]
auth_collection = db["auth"]


def add_smart_nvme(smartNvme, UUID):  # noqa: E501
    """Upload NVME disk data

     # noqa: E501

    :param smartNvme: Smartctl --json -x output to be added to dataset
    :type smartNvme: dict | bytes

    :rtype: None
    """
    app.logger.info('manager.add_smart_nvme()')

    if connexion.request.is_json:
        smartNvme = SmartNvme.from_dict(connexion.request.get_json())  # noqa: E501

    if (check_auth(UUID) is False):
        return "Authorization Failed"

    dct = smartNvme.to_dict()
    dct["UUID"] = UUID
    smartnvme_id = smartnvme_collection.insert_one(dct).inserted_id
    app.logger.info('smartnvme_id = ' + str(smartnvme_id))
    # return 'success?'


def add_smart_ssd(smartSsd, UUID):  # noqa: E501
    """Upload ssd disk data

     # noqa: E501

    :param smartSsd: Smartctl --json -x output to be added to dataset
    :type smartSsd: dict | bytes

    :rtype: None
    """
    app.logger.info('manager.add_smart_ssd()')

    if connexion.request.is_json:
        smartSsd = SmartNvme.from_dict(connexion.request.get_json())  # noqa: E501

    if (check_auth(UUID) is False):
        return "Authorization Failed"
    dct = smartSsd.to_dict()
    dct["UUID"] = UUID
    smartssd_id = smartssd_collection.insert_one(dct).inserted_id
    app.logger.info('smartssd_id = ' + str(smartssd_id))
    # return 'success?'


def get_smart_nvme():  # noqa: E501
    """Get all NVME disk data

     # noqa: E501


    :rtype: None
    """
    app.logger.info('manager.get_smart_nvme()')
    check_auth()
    # return 'success?'


def get_smart_ssd():  # noqa: E501
    """Get all ssd disk data

     # noqa: E501


    :rtype: None
    """
    app.logger.info('manager.get_smart_ssd()')
    check_auth()
    # return 'success?'


def get_auth(UUID=None):
    """
    Provide new UUID
    Provide new ApiKey
    hash api key and store
    :return:
    """
    new_id = False
    if (UUID is None):
        UUID = str(uuid.uuid4())
        new_id = True

    apiKey = str(uuid.uuid4())
    hashed = hashlib.sha256(apiKey.encode()).hexdigest()
    if new_id:
        store_dict = {"UUID": UUID, "apiKey": hashed}
        auth_id = auth_collection.insert_one(store_dict).inserted_id
    else:
        auth_id = auth_collection.find_one_and_update({"UUID": UUID}, {"$set": {"apiKey": hashed}}, upsert=True)
    app.logger.info("auth id = " + str(auth_id))

    return InlineResponse200(UUID, apiKey)


def check_auth(UUID):
    if ("Authorization" not in connexion.request.headers):
        return False

    apiKey = connexion.request.headers["Authorization"]
    hashedInput = hashlib.sha256(apiKey.encode()).hexdigest()

    auth = auth_collection.find_one({"UUID": UUID})

    if auth is None:
        return False

    if auth["apiKey"] == hashedInput:
        return True
    else:
        return False
