# Use case 2

1 **Search for a given event in the Seismic Portal** via the GUI and get its ID
 - use the [Seismic Portal homepage](https://www.seismicportal.eu) to find an earthquake in Turkey, September 26th with a magnitude >5 thanks to the top right panel.
  > - unid: 20190926_0000070
  > - longitude latitude: 28,19 40,87
  > - magnitude: Mw 5.7
  > - origin time: 2019-09-26 10:59:25.1 UTC

2 **Check all available information for this event** (origins, phases, moment tensors and felt reports)
 - In the earthquake list, click on the corresponding events.
  > The [event page](https://www.seismicportal.eu/eventdetails.html?unid=20190926_0000070) is displayed and you can check origins, moment tensors and felt reports on the map.
  
3 **Find the EMSC event identifier** to look for extra information on the EMSC website.
 - Used the [eventid service](https://www.seismicportal.eu/eventid/) with the parameters:
 > - source_id: 20190926_0000070
 > - source_catalog: UNID
 > - out_catalog: EMSC

And we obtained
 > the evid: 794756 and the EMSC page for this event will be
 <https://www.emsc-csem.org/Earthquake/earthquake.php?id=794756>

4 **Search previous moment tensors in this region**
 - Go to the [moment tensor service](https://www.seismicportal.eu/mtws/)
 - Use the geographic side panel to select _circle_ and fills the boxes longitude=28,19 latitude=40,87 and radius=3 (click on the search button).
 - Go to the _MAP VIEW_ tap and look the beachballs.

5 **Download all moment tensors** for this event
 - Put the unid in the _EVENT ID_ side panel and click on search.
 - Click on the download button in the bottom right corner.

5 **Search for felt seismic events** close to this event
 - Go to the [felt reports service](https://www.seismicportal.eu/testimonies-ws/) (called testimonies).
 - Fill out the min _#TESTIMONIES_ with 100, the min _MAGNITUDE_ to 5 and click on the search button.
 - Go to the _MAP VIEW_, zoom on the Turkey, draw a rectangle that contains at least the northern west coast and click on the search button.

6 **Download felt reports** for this event
 - On the _LIST VIEW_ select the event in your interest. It increments the event count in your _CART_.
 - In your _CART_, click on the green Download button and select _Events and testimonies as csv zipped_.