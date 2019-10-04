# EMSC Web Services 101

All EMSC services are accessible via the following link : http://www.seismicportal.eu/webservices.html. 

| Name | Description | Direct url |
| --- | --- | --- | 
| Fdsn-event | web service for EMSC events | http://www.seismicportal.eu/fdsn-wsevent.html |
| Flinn-Engdahl Lookup | web service for FE region name | http://www.seismicportal.eu/feregions.html |
| Moment Tensors | web service for MT solutions |  http://www.seismicportal.eu/mtws/ |
| Testimonies | web service for Felt reports | http://www.seismicportal.eu/testimonies-ws/ |
| EventID | web service for event identifiers| http://www.seismicportal.eu/eventid |
| Rupture Models | web service for SRCMOD database | http://www.seismicportal.eu/srcmodws |
| (near) Realtime Notification | Service via websocket to get real time event notification | http://www.seismicportal.eu/realtime.html |

The idea is to access Web services via an url, instead of a "web page" displayed in a browser, and get raw data. The principle is to build an url with some parameters that define the data we want to retrieve.
Parameters depends on the web service specification - for example the FDSN specification etc. However all web services have a Graphical User Interface (GUI) to facilitate user queries.

## How to use of EMSC web services
---
 * **Two walkthroughs** showing concrete examples : [use case 1](use_cases/usecase1.md) and [use case 2](use_cases/usecase2.md). They guide to :
   - search for events
   - check for available origins, moment tensors and felt reports
   - find event identifier matches between USGS, EMSC and the Seismic Portal
   - download data
 * **Jupyter Notebook** describing use of webservices in python and shell [link](emsc_services/emsc_services.md), version [ipynb](emsc_services/emsc_services.ipynb).


### Helper functions in python
---
In order to help users for a first use of EMSC webservices in python, you can look at the [helper_tools.py](helper_tools.py) and try these few lines!
```python
from __future__ import print_function
from helper_tools import *

print("Web service example using \'text\' format:")
url = "http://www.seismicportal.eu/fdsnws/event/1/query?eventid=20170919_0000091&format=text"
res = geturl(url)
print(parsecsv(res['content']))

print("\nWeb service example using \'json\' format:")
url = "http://www.seismicportal.eu/fdsnws/event/1/query?eventid=20170919_0000091&format=json"
res = geturl(url)
print(parsejson(res['content']))


print("\nWeb service example using \'zip\' format (Testimonies web service):")
url = "http://www.seismicportal.eu/testimonies-ws/api/search?unids=[20170919_0000091]&includeTestimonies=true"
r = requests.get(url, stream=True)
print(parsezip(r.content))

```


## Real Time event Notification
---
To get EMSC events in real time, you can use a websocket client that listen to *ws://www.seismicportal.eu/standing_order/websocket*. The python program [seismicportal_listener.py](seismicportal_listener.py) gives you one example. 

To test ti just run :

```bash
python seismicportal_listener.py
```


|  | |  | |
| --- | --- | --- | --- |
| <img src="img/emsc-logo-new-200.png" alt="EMSC logo" width="100" > | <img src="img/EPOS_logo_crop.png" alt="EPOS logo" width="100" > | This content has been done within the EPOS project funded by the European Union's Horizon 2020 research and innovation programme under grant agreement No 676564.| <img src="img/EC-H2020.png" alt="EC-H2020"  width="300" > |
