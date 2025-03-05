# EMSC, Matthieu landes, February 2025
from tornado.websocket import websocket_connect
from tornado.ioloop import IOLoop
from tornado import gen

import argparse
import logging
import json
import sys

import pathlib
import requests

echo_uri = 'wss://www.seismicportal.eu/standing_order/websocket'
PING_INTERVAL = 15


def myprocessing(message, diroutput='.'):
    """
    Check if the event has a magnitude > 5 
    and is inside -7 <= longitude < 11 and 41 <= latitude < 52

    Write the result in the diroutput directory
    """
    try:
        data = json.loads(message)
    except Exception:
        logging.exception("Unable to parse json message")

    # eqinfo contains earthquake parameters
    eqinfo = data['data']['properties']
    logging.info('>>>> {action:7} event from {auth:7}, unid:{unid}, T0:{time}, Mag:{mag}, Region: {flynn_region}'.format(**eqinfo, action=data['action']))
    logging.debug("%s\n", eqinfo)

    regionok = -7 <= eqinfo['lon'] < 11 and 41 <= eqinfo['lat'] < 52
    magok = eqinfo['mag'] > 5

    if regionok and magok:
        # request event information to the fdsn-event service
        url = f'https://www.seismicportal.eu/fdsnws/event/1/query?eventid={eqinfo["unid"]}&format=xml'
        res = requests.get(url)
        if res.status_code != 200:
            logging.error('unid %s not in the seismicportal')
            return
        filename = diroutput / f'event_{eqinfo["unid"]}.qml'
        logging.info('write %s', filename)
        with open(filename, 'w') as f:
            quakemlcontent = res.text
            f.write(quakemlcontent)
    else:
        logging.info('Skip event: region is %s, magnitude is %s', regionok, magok)


@gen.coroutine
def listen(ws, *args, **kwargs):
    while True:
        msg = yield ws.read_message()
        if msg is None:
            logging.info("close")
            ws = None
            break
        myprocessing(msg, *args, **kwargs)


@gen.coroutine
def launch_client(*args, **kwargs):
    try:
        logging.info("Open WebSocket connection from %s", echo_uri)
        ws = yield websocket_connect(echo_uri, ping_interval=PING_INTERVAL)
    except Exception:
        logging.exception("connection error")
    else:
        logging.info("Waiting for messages...")
        listen(ws, *args, **kwargs)


if __name__ == '__main__':
    argd = argparse.ArgumentParser()
    argd.add_argument('-v', '--verbose', action='count', default=0)
    argd.add_argument('-o', '--diroutput', default='output/')

    args = argd.parse_args()

    if args.verbose == 0:
        logging.basicConfig(stream=sys.stderr, level=logging.INFO, format='%(levelname)s - %(message)s')
    else:
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format='%(levelname)s - %(message)s')

    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    # create output directory is needed
    diroutput = pathlib.Path(args.diroutput)
    logging.info('Output directory: %s', diroutput)
    diroutput.mkdir(parents=True, exist_ok=True)

    ioloop = IOLoop.instance()
    launch_client(diroutput=diroutput)
    try:
        ioloop.start()
    except KeyboardInterrupt:
        logging.info("Close WebSocket")
        ioloop.stop()