# How to use of EMSC web services
---

This tutorial aims to present the use of EMSC services with 6 seismological use cases. You can complete the tutorial :
 * via the GUI of web services,
 * or **via a scripting approach and the Jupyter Notebook [markdown](emsc_services.md) or [ipynb](emsc_services.ipynb) gives you a complete walkthrough** with python and linux shell.

 1. How to search and find events (*fdsn-event* web service)
	> Search all earthquakes that occur in September and October 2017 with a magnitude greater then 6..5 and get the event id of the last destructive mexican earthquake.

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