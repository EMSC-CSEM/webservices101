# EMSC, Matthieu landes, October 2019

from __future__ import unicode_literals

from tornado.websocket import websocket_connect
from tornado.ioloop import IOLoop
from tornado import gen

import logging
import json
import sys

echo_uri = 'wss://www.seismicportal.eu/standing_order/websocket'
PING_INTERVAL = 15


def myprocessing(message):
    """
    You can modify this function to run custom process on the message
    """
    try:
        data = json.loads(message)
        info = data['data']['properties']
        info['action'] = data['action']
        logging.info('>>>> {action:7} event from {auth:7}, unid:{unid}, T0:{time}, Mag:{mag}, Region: {flynn_region}'.format(**info))
    except Exception:
        logging.exception("Unable to parse json message")


@gen.coroutine
def listen(ws):
    while True:
        msg = yield ws.read_message()
        if msg is None:
            logging.info("close")
            ws = None
            break
        myprocessing(msg)


@gen.coroutine
def launch_client():
    try:
        logging.info("Open WebSocket connection to %s", echo_uri)
        ws = yield websocket_connect(echo_uri, ping_interval=PING_INTERVAL)
    except Exception:
        logging.exception("connection error")
    else:
        logging.info("Waiting for messages...")
        listen(ws)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    ioloop = IOLoop.instance()
    launch_client()
    try:
        ioloop.start()
    except KeyboardInterrupt:
        logging.info("Close WebSocket")
        ioloop.stop()
