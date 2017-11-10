# EMSC Web Services 101

All EMSC services are accessible via the following link : http://www.seismicportal.eu/webservices.html. 

| Name | Description | Direct url |
| --- | --- | --- | 
| Fdsn-event | web service for EMSC events | http://www.seismicportal.eu/fdsn-wsevent.html |
| Flinn-Engdahl Lookup | web service for FE region name | http://www.seismicportal.eu/feregions.html |
| Moment Tensors | web service for MT solutions |  http://vigogne.emsc-csem.org/mtws/ |
| Testimonies | web service for Felt reports | http://vigogne.emsc-csem.org/testimonies-ws/ |
| EventID | web service for event identifiers| http://vigogne.emsc-csem.org/eventid |
| Rupture Models | web service for SRCMOD database | http://vigogne.emsc-csem.org/srcmodws |
| (near) Realtime Notification | Service via websocket to get real time event notification | http://www.seismicportal.eu/realtime.html |

The idea is to access Web services via an url, instead of a "web page" displayed in a browser, and get raw data. The principle is to build an url with some parameters that define the data we want to retrieve.
Parameters depends on the web service specification - for example the FDSN specification etc. However all web services have a Graphical User Interface (GUI) to facilitate user queries.

# How to use of EMSC web services
---

This tutorial aims to present the use of EMSC services with 6 seismological use cases. 

 1. How to search and find events (*fdsn-event* web service)
	> Search all earthquakes that occur in October 2017 with a magnitude greater then 6 and get the event id of the last destructive mexican earthquake.

 2. Collect earthquake parameters (*fdsn-event* web service)
    > In the following, we consider the M7.1 Puebla, Mexico earthquake on September, 19th 2017. The Seismic Portal identifier (unid) is *20170919_0000091*.
	> Get the origin parameters of this event.

 3. Get a Flinn Engdhal region name (*Flinn Engdhal* web service)
	> Search for the Flinn Engdhal region name of the M7.1 Mexico earthquake.

 4. How to manage multiple event identifiers ? (*EventID* web service) 
    > Find the web page of this event on the EMSC, USGS and INGV websites.
	
 5. Get Moment Tensors (*Moment Tensor* web service)
	 > 1. for the M7.1 Puebla, Mexico earthquake
	 > 2. for events between October 1st and 19th 2017

 6. Collect Felt reports (*Testimonies* web service)
	 > 1. Find how many testimonies EMSC has collected for the  M7.1 Puebla, Mexico earthquake
	 > 2. Get all testimonies

Everytime we can complete the tutorial :
 * via the GUI of web services,
 * or via a scripting approach and the [Jupyter Notebook](https://github.com/EMSC-CSEM/webservices101/blob/master/emsc_services.ipynb) gives you a complete walkthrough with python and linux shell.

### Helper functions in python
---
In order to help users for a first use of EMSC webservices in python, you can look at the [helper_tools.py](https://github.com/EMSC-CSEM/webservices101/blob/master/helper_tools.py) and try these few lines!
```python
from helper_tools import *

print "Web service example using \'text\' format:"
url = "http://www.seismicportal.eu/fdsnws/event/1/query?eventid=20170919_0000091&format=text"
res = geturl(url)
print parsecsv(res['content'])

print "\nWeb service example using \'json\' format:"
url = "http://www.seismicportal.eu/fdsnws/event/1/query?eventid=20170919_0000091&format=json"
res = geturl(url)
print parsejson(res['content'])


print "\nWeb service example using \'zip\' format (Testimonies web service):"
url = "http://vigogne.emsc-csem.org/testimonies-ws/api/search?unids=[20170919_0000091]&includeTestimonies=true"
r = requests.get(url, stream=True)
print parsezip(r.content)

```


## Real Time event Notification
---
To get EMSC events in real time, you can use a websocket client that listen to *ws://www.seismicportal.eu/standing_order/websocket*. The python program [seismicportal_listener.py](https://github.com/EMSC-CSEM/webservices101/blob/master/seismicportal_listener.py) gives you one example. 

To test ti just run :

```python seismicportal_listener.py```

---
---

|  | |  | |
| --- | --- | --- | --- |
| <img src="https://github.com/EMSC-CSEM/webservices101/blob/master/img/emsc-logo-new-200.png" alt="EMSC logo" width="100" > | <img src="https://github.com/EMSC-CSEM/webservices101/blob/master/img/EPOS_logo_crop.png" alt="EPOS logo" width="100" > | This content has been done within the EPOS project funded by the European Union's Horizon 2020 research and innovation programme under grant agreement No 676564.| <img src="https://github.com/EMSC-CSEM/webservices101/blob/master/img/EC-H2020.png" alt="EC-H2020"  width="300" > |

