# EMSC, Matthieu landes, October 2019

from __future__ import unicode_literals

from tornado.websocket import websocket_connect
from tornado.ioloop import IOLoop
from tornado import gen

import argparse
import logging
import json
import sys

echo_uri = 'wss://www.seismicportal.eu/standing_order/websocket'
PING_INTERVAL = 15


def myprocessing(message):
    """
    You can modify this function to run custom process on the message.
    Messages are json messages and they have this structure:

    {
    "action": "create",
    "data": {
        "type": "Feature",
        "geometry": {
        "type": "Point",
        "coordinates": [
            28.5381,
            40.115,
            -7.0
        ]
        },
        "id": "20250305_0000090",
        "properties": {
        "source_id": "1779128",
        "source_catalog": "EMSC-RTS",
        "lastupdate": "2025-03-05T10:06:56.102425Z",
        "time": "2025-03-05T09:45:07.0Z",
        "flynn_region": "WESTERN TURKEY",
        "lat": 40.115,
        "lon": 28.5381,
        "depth": 7.0,
        "evtype": "ke",
        "auth": "AFAD",
        "mag": 1.4,
        "magtype": "ml",
        "unid": "20250305_0000090",
        }
    }
    }
    """
    try:
        data = json.loads(message)
        info = data['data']['properties']
        info['action'] = data['action']
        logging.info('>>>> {action:7} event from {auth:7}, unid:{unid}, T0:{time}, Mag:{mag}, Region: {flynn_region}'.format(**info))
        logging.debug("%s\n", info)
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
        logging.info("Open WebSocket connection from %s", echo_uri)
        ws = yield websocket_connect(echo_uri, ping_interval=PING_INTERVAL)
    except Exception:
        logging.exception("connection error")
    else:
        logging.info("Waiting for messages...")
        listen(ws)


if __name__ == '__main__':
    argd = argparse.ArgumentParser()
    argd.add_argument('-v', '--verbose', action='count', default=0)

    args = argd.parse_args()

    if args.verbose == 0:
        logging.basicConfig(stream=sys.stderr, level=logging.INFO, format='%(levelname)s - %(message)s')
    else:
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format='%(levelname)s - %(message)s')

    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    ioloop = IOLoop.instance()
    launch_client()
    try:
        ioloop.start()
    except KeyboardInterrupt:
        logging.info("Close WebSocket")
        ioloop.stop()
