# Use case 1

## Search information concerning the M5.3 seismic event on 2019-03-30 in Greece

1 Check the UGSG web site: <https://earthquake.usgs.gov/earthquakes/map/> and search the event.

* Map search [>here<](https://earthquake.usgs.gov/earthquakes/map/#%7B%22autoUpdate%22%3A%5B%5D%2C%22basemap%22%3A%22grayscale%22%2C%22feed%22%3A%221556884360661%22%2C%22listFormat%22%3A%22default%22%2C%22mapposition%22%3A%5B%5B23.32208001137843%2C-17.1826171875%5D%2C%5B53.592504809039376%2C42.5830078125%5D%5D%2C%22overlays%22%3A%5B%22plates%22%5D%2C%22restrictListToMap%22%3A%5B%22restrictListToMap%22%5D%2C%22search%22%3A%7B%22id%22%3A%221556884360661%22%2C%22name%22%3A%22Search%20Results%22%2C%22isSearch%22%3Atrue%2C%22params%22%3A%7B%22starttime%22%3A%222019-03-10%2000%3A00%3A00%22%2C%22endtime%22%3A%222019-05-03%2023%3A59%3A59%22%2C%22minmagnitude%22%3A5%2C%22orderby%22%3A%22time%22%7D%7D%2C%22sort%22%3A%22newest%22%2C%22timezone%22%3A%22utc%22%2C%22viewModes%22%3A%5B%22list%22%2C%22map%22%5D%2C%22event%22%3A%22us2000k7ki%22%7D)

* Find the event page [Event page](https://earthquake.usgs.gov/earthquakes/eventpage/us2000k7ki/executive).
   > We get the USGS event identifier: us2000k7ki

3 __Find EMSC event ID and UNID.__ With the [EventID](https://www.seismicportal.eu/eventid/) web service, let's look for the EMSC and Seismic Portal identifier:

* Seismic Portal (UNID) : 20190330_0000065
  > <www.seismicportal.eu/eventid/api/convert?source_id=us2000k7ki&source_catalog=USGS&out_catalog=UNID>  

  EMSC ID : 754693
  > <www.seismicportal.eu/eventid/api/convert?source_id=us2000k7ki&source_catalog=USGS&out_catalog=EMSC>

* Verify the UNID on the search page of the [Seismic Portal](https://www.seismicportal.eu/)
  * minimum magnitude: 5
  * from 2019-03-30 to 2019-03-31
  
  Go to the event page
  > <www.seismicportal.eu/eventdetails.html?unid=20190330_0000065>

* Check EMSC maps for this event:
  > <www.emsc-csem.org/Earthquake/earthquake.php?id=754693>

4 __Collect Origins, Moment tensors and Felt reports data with EMSC web services.__

* [Fdsn-event](https://www.seismicportal.eu/fdsn-wsevent.html)
  > <www.seismicportal.eu/fdsnws/event/1/query?eventid=20190330_0000065&format=json&includeallorigins=true>

* [Moment tensors](https://www.seismicportal.eu/mtws/)
  > <www.seismicportal.eu/mtws/api/search?eventid=20190330_0000065&format=text>

* [Felt reports](http://www.seismicportal.eu/testimonies-ws/)
  > <www.seismicportal.eu/testimonies-ws/api/search?unids=[20190330_0000065]&includeTestimonies=true>

5 __Search more data for events in the same regions.__

* events with more than 500 felt reports with [Felt report ws](https://www.seismicportal.eu/testimonies-ws/):
  > <www.seismicportal.eu/testimonies-ws/api/search?lat=38&lon=23.2&maxradius=3&minnbtestimonies=500&format=text>

* check moment tensors in the regions with [Moment tensor ws](https://www.seismicportal.eu/mtws/):
  > <www.seismicportal.eu/mtws/api/search?lat=38&lon=23.2&maxradius=3&format=text>

6 __Get data in json or QuakeML for this event with [Event](https://www.seismicportal.eu/fdsn-wsevent.html) and [MT](https://www.seismicportal.eu/mtws/) web services.__

* all origins in QuakeML
  > <www.seismicportal.eu/fdsnws/event/1/query?limit=10&eventid=20190330_0000065&format=xml&includeallorigins=true>

  or in json format
  > <www.seismicportal.eu/fdsnws/event/1/query?limit=10&eventid=20190330_0000065&format=json&includeallorigins=true>

* all moment tensors in QuakeML
  > <www.seismicportal.eu/mtws/api/search?eventid=20190330_0000065&format=xml>

  or in json
  > <www.seismicportal.eu/mtws/api/search?eventid=20190330_0000065&format=json>