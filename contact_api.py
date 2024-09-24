#
# f.folkmann@gso.schule.koeln, 2022
#
"""exposes 'contact_svc' funtions remotely"""
from uuid import uuid4
from flask import Flask, Response, request
from json import loads, dumps
from contact import *
import contact_svc as mngr

import logging
log_level = logging.ERROR

app = Flask(__name__)
app.config["DEBUG"] = log_level == logging.DEBUG
logging.basicConfig(level = log_level)

@app.route("/")
def about():
    """respond about info"""
    return "<h1>Hi there this is 'contact_api'</h1>" 

@app.route('/get_contact/<uuid>', methods=['GET'])
def get_contact(uuid):
    try:
        logging.debug(f"S: GET get_contact: {uuid}")
        contact = mngr.get_contact(uuid)
        dict = contact.to_dict()
        json = dumps(dict)
        resp = Response(json, status=200)
        logging.debug(f"S: Resp: {resp}")
        return resp
    except:
        resp = Response("invalid request", status=400)
        logging.debug(f"S: Resp: {resp}")
        return resp

@app.route('/get_contacts/<patt>', methods=['GET'])
@app.route('/get_contacts', methods=['GET'])
def get_contacts(patt = ""):
    try:
        logging.debug(f"S: GET get_contacts: {patt}")
        dict = mngr.get_contacts(patt)
        for uuid in dict.keys():
            contact = dict[uuid]
            dict[uuid] = contact.to_dict()
        json = dumps(dict)
        resp = Response(json, status=200)
        logging.debug(f"S: Resp: {resp}")
        return resp
    except:
        resp = Response("invalid request", status=400)
        logging.debug(f"S: Resp: {resp}")
        return resp

@app.route('/add_contact', methods=['POST'])
def add_contact():
    try:
        # retrieve contact from json data
        json = request.get_json()
        logging.debug(f"S: POST add_contact: {json}")
        dict = loads(json)
        contact = Contact.from_dict(dict)

        # save contact under uuid
        uuid = mngr.create_uuid()
        mngr.save_contact(uuid, contact)
        resp = Response(uuid, status=201)
        logging.debug(f"S: Resp: {resp}")
        return resp
    except:
        resp = Response("invalid request", status=400)
        logging.debug(f"S: Resp: {resp}")
        return resp

@app.route('/save_contact', methods=['PUT'])
def save_contact():
    raise NotImplementedError

@app.route('/delete_contact/<uuid>', methods=['DELETE'])
def delete_contact(uuid):
    try:
        logging.debug(f"S: DELETE delete_contact: {uuid}")
        if mngr.delete_contact(uuid):
            resp = Response("OK", status=200)
        else:
            resp = Response("Not found", status=204)
        logging.debug(f"S: Resp: {resp}")
        return resp
    except:
        resp = Response("invalid request", status=400)
        logging.debug(f"S: Resp: {resp}")
        return resp

# run api using flask
app.run()
