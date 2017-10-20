#EMSC, Matthieu landes, October 2017

#need at least Tornado 3.0
#http://www.tornadoweb.org/en/stable/
from tornado.websocket import websocket_connect
from tornado.ioloop import IOLoop
from datetime import timedelta
import logging

import json

echo_uri = 'ws://www.seismicportal.eu/standing_order/websocket'
PING_TIMEOUT = 15

#You can modify this function to run custom process on the message
def myprocessing(message):
    try:
        data = json.loads(message)
        info = data['data']['properties']
        info['action'] = data['action']
        logging.info('>>>> {action:7} event from {auth:7}, unid:{unid}, T0:{time}, Mag:{mag}, Region: {flynn_region}'.format(**info))
    except Exception:
        logging.exception("Unable to parse json message")

#Class that construct a websocker listener.
class myws():
    conn = None
    keepalive = None
    def __init__(self, uri):
        self.uri = uri
        self.doconn()

    def doconn(self):
        logging.info("trying connection to %s"%(self.uri,))
        w = websocket_connect(self.uri)
        logging.info("connected, waiting for messages")
        w.add_done_callback(self.wsconnection_cb)

    def dokeepalive(self):
        stream = self.conn.protocol.stream
        if not stream.closed():
            self.keepalive = stream.io_loop.add_timeout(timedelta(seconds=PING_TIMEOUT), self.dokeepalive)
            self.conn.protocol.write_ping("")
        else:
            self.keepalive = None # should never happen

    def wsconnection_cb(self, conn):
        self.conn = conn.result()
        self.conn.on_message = self.process_message
        self.keepalive = IOLoop.instance().add_timeout(timedelta(seconds=PING_TIMEOUT), self.dokeepalive)

    #Here we receive and process message
    def process_message(self, message):
        if message is not None:
            myprocessing(message)
        else:
            self.close()

    def close(self):
        logging.info('connection closed')
        if self.keepalive is not None:
            keepalive = self.keepalive
            self.keepalive = None
            IOLoop.instance().remove_timeout(keepalive)
        self.doconn()



import signal
def main():
    logging.getLogger().setLevel(logging.INFO)
    try:
        io_loop = IOLoop.instance()
        signal.signal(signal.SIGTERM, io_loop.stop)
        myws(echo_uri)
        IOLoop.instance().start()
    except KeyboardInterrupt:
        io_loop.stop()



if __name__ == '__main__':
    main()
