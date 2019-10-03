#Matthieu Landes, EMSC, 22/10/2017
from __future__ import print_function

import requests
from io import BytesIO, StringIO
import csv
import json

import zipfile
import numpy as np


def geturl(url):
    """
    Get the ascii content of an URL
    """
    res = requests.get(url, timeout=15)
    return {'status': res.status_code,
            'content': res.text}

def parsecsv(txt, usedict=False):
    """
    Parse txt input as csv
    the first line may be used to parse input as dictionary
    """
    if usedict:
        parser = csv.DictReader(StringIO(txt), delimiter='|')
        #parser = csv.DictReader(txt, delimiter='|')
    else:
        parser = csv.reader(StringIO(txt), delimiter='|')
        #parser = csv.reader(txt, delimiter='|')
        header = next(parser)

    return [ line for line in parser]


def parsejson(txt):
    """
    Parse txt input as json
    """
    return json.loads(txt)

def parsezip(bufferstr):
    """
    parse binary object as zip file
    This archive is supposed to contain a set of column based file
    """
    z = zipfile.ZipFile(BytesIO(bufferstr))
    res = {}
    for filename in z.namelist():
        data = z.read(filename).decode('utf-8')
        A = np.loadtxt(StringIO(data), delimiter=',')
        res[filename] = A
    return res


if __name__ == "__main__":
    #basic example in text

    print("Web service example using \'text\' format:")
    url = "http://www.seismicportal.eu/fdsnws/event/1/query?eventid=20170919_0000091&format=text"
    res = geturl(url)
    print(parsecsv(res['content']))

    print("\nWeb service example using \'json\' format:")
    url = "http://www.seismicportal.eu/fdsnws/event/1/query?eventid=20170919_0000091&format=json"
    res = geturl(url)
    print(parsejson(res['content']))


    print("\nWeb service example using \'zip\' format (Testimonies web service):")
    url = "http://vigogne.emsc-csem.org/testimonies-ws/api/search?unids=[20170919_0000091]&includeTestimonies=true"
    r = requests.get(url, stream=True)
    print(parsezip(r.content))
