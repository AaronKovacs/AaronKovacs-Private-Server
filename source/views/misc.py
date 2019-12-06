import json
import datetime
import uuid
import os
import threading
import extraction
import requests
import copy
import urllib

from flask import Flask, request, render_template, g, jsonify, Blueprint
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask_restplus import Resource, Api, abort, Namespace
from flask_cors import CORS, cross_origin

from sqlalchemy import or_
from sqlalchemy import DateTime
from sqlalchemy import desc
from sqlalchemy.sql.expression import func, select

from sqlakeyset import get_page, serialize_bookmark, unserialize_bookmark

from ..database.database import Session
from ..helpers.helpers import *
from ..helpers.namespace import APINamespace
from ..configuration.config import PAGE_SIZE

from ..models.text import Text

api = APINamespace('Misc')

@api.route('/text')
class TextStatus(Resource):
    def post(self):
        text = request.json.get('text', '???')
        
        session = Session()
        status_row = Text(value=text)
        session.add(status_row)

        session.commit()
        session.close()

        return success()