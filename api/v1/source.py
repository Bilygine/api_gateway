import google
import json
import logging

import connexion
import requests
from google.cloud import storage

import config
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '../credentials/bilygine_google_credentials.json'


def post(body: dict):
    """
    Method POST endpoint /source
    :param body: dictionary with URL and other parameters

    :return message and http code
    """
    logging.info(f"Sending url {body.get('url')} to downloader")
    r = requests.post(url=config.DOWNLOADER_URL, params=body)
    logging.info(f"response code: {r.status_code}")
    if r.status_code == 200:
        return r.json(), 201
    else:
        return "A problem has been raise from downloader", 200


def put(source_id: str, body: dict):
    """
    Method PUT endpoint /source/{source_id}
    :param source_id: uuid for a source in database
    :param body: dictionary with updated information for a source_id

    :return message and status code depending on downloader response
    """
    logging.info(f"Updating source {source_id} with body {body.items()}")
    data = json.dumps(body)
    r = requests.put(url=config.DOWNLOADER_ENDPOINT, data=data, params={"source_id": source_id})
    logging.info(f"request finished with status code {r.status_code}")
    if r.status_code == 200:
        return "Updated", 200
    elif r.status_code == 404:
        return "Source not found", 404
    else:
        return "A problem has been raise from downloader", 200


def delete(source_id: str):
    """
    Method DETELE endpoint /source/{source_id}
    :param source_id: uuid for a source in database

    :return 200 for delete and in case of a problem or 404 if the source is not found
    """
    logging.info(f"Deleting source {source_id}")
    r = requests.delete(url=config.DOWNLOADER_URL, params={"source_id": source_id})
    logging.info(f"request finished with status code {r.status_code}")
    if r.status_code == 200:
        return "Deleted", 200
    elif r.status_code == 404:
        return "Source not found", 404
    else:
        return "A problem has been raise from downloader", 200


def post_file(body):
    client = storage.\
        Client.\
        from_service_account_json(json_credentials_path='../credentials/bilygine_google_credentials.json')
    bucket = client.get_bucket(config.BUCKET_NAME)
    b = bucket.blob(blob_name="upload/{}".format(body.get('file_name')))
    try:
        upload_url = b.create_resumable_upload_session(content_type=config.GOOGLE_CONTENT_TYPE)
    except google.api_core.exeptions.NotFound:
        raise FileNotFoundError

    return upload_url, 200


