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

Use of web services
 * on the web, useful to separate data access and data display
 * automatic access via script (e.g. python, shell)

# How to use of EMSC web services

This tutorial aims to present the use of EMSC services with concrete examples. 

The [Jupyter Notebook](https://github.com/EMSC-CSEM/webservices101/blob/master/emsc_services.ipynb) gives a complete walkthrough with python and linux shell of the following use cases.

 * How to search and find events (*fdsn-event* web service)
	> Search all earthquakes that occur in October 2017 with a magnitude greater then 6 and get the event id of the last destructive mexican earthquake.

 * Collect earthquake parameters (*fdsn-event* web service)
    > In the following, we consider the M7.1 Puebla, Mexico earthquake on September, 19th 2017. The Seismic Portal identifier (unid) is *20170919_0000091*.
	> Get the origin parameters of this event.

 * Get a Flinn Engdhal region name (*Flinn Engdhal* web service)
	> Search for the Flinn Engdhal region name of the M7.1 Mexico earthquake.

 * How to manage information from multiple institutes ? (*EventID* web service) 
    > Find the web page of this event on the EMSC, USGS and INGV websites.
	
 * Get Moment Tensors (*Moment Tensor* web service)
	 > 1. for the M7.1 Puebla, Mexico earthquake
	 > 2. for events between October 1st and 19th 2017

 * Collect Felt reports (*Testimonies* web service)
	 > 1. Find how many testimonies EMSC has collected for the  M7.1 Puebla, Mexico earthquake
	 > 2. Get all testimonies

## Real Time event Notification

To get EMSC events in real time, you can use a websocket client that listen to *ws://www.seismicportal.eu/standing_order/websocket*. The python program [seismicportal_listener.py](https://github.com/EMSC-CSEM/webservices101/blob/master/seismicportal_listener.py) gives you one example. Just run :

```python seismicportal_listener.py```


