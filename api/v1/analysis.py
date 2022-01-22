import json
import logging

import requests


import config


def post(source_id: str, body: dict):
    """
    Method POST endpoint /source/{source_id}/analysis
    :param source_id: uuid of source in db
    :param body: dictionary with language_code, encoding and sample_rate_hertz ALL REQUIRED

    :return depending status code from http call, a message and a http is returned
    """
    logging.info(f"Sending body {body.items()} to analyzer")
    body.update({"source_id": source_id})
    data = json.dumps(body)
    r = requests.post(url=config.ANALIZER_URL, data=data)
    logging.info(f"response code: {r.status_code}")
    if r.status_code == 200:
        return "created", 201
    elif r.status_code == 404:
        return "Source not found", 404
    else:
        return "A problem has been raise from analyzer", 200


