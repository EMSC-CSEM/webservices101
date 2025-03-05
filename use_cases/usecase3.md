# Use case 3

This use case addresses the situation where one user wants to receive fdsn-event information as soon as it arrives. To solve it we will use:

 - the [(near) Real Time Notification service](http://www.seismicportal.eu/realtime.html)
 - the [Fdsn-event service](http://www.seismicportal.eu/fdsn-wsevent.html)

1 **The correct approach** is to set up a listener with the nRT notification service, which opens a websocket connection between the client (your listener) and the Seismic Portal server. The notifications are for new events and updates. Once this listener is running, it's possible to run a custom function (see follong step) for each message received. 

Note that the **ugly approach** might be to repeatedly request the fdsn-event, for example for the last 10 events... It works, but as a lot of users do this, it can overload the fdsn-event service for little (or none) valuable information per request.

2 **Message content** given by the nRT notificcation service. The message sent by the service are geojson and have this structure:

```json
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
```

Where `action` is "update" or "create" if the message is for an update or a new event.

3 **Define your custom processing**. For instance, each time the listener receives a new message you may want to first apply some magnitude or longitude/latitude filtering depending of your interest. Here will choose the following critira:
  > - magnitude >= 5.0
  > - -7 <= longitude < 11 and 41 <= latitude < 52 (metropolitan France)

If the criteria are valid, we will search for the fdsn-event information using the UNID parameter (given in the message)
 > www.seismicportal.eu/fdsnws/event/1/query?eventid=UNID&format=xml

Finally we write the quakeml content in the `output/` directory.


4 Using python3, **a first impementation** is done using the [seismicportal_listener.py](../seismicportal_listener.py) script and by modifying the `myprocessing` function. For instance, this function could be:

```python
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
            logging.error('unid %s not in the Seismic Portal')
            return
        filename = diroutput / f'event_{eqinfo["unid"]}.qml'
        logging.info('write %s', filename)
        with open(filename, 'w') as f:
            quakemlcontent = res.text
            f.write(quakemlcontent)
    else:
        logging.info('Skip event: region is %s, magnitude is %s', regionok, magok)
```
And the resulting python script is [listen_new_event.py](listen_new_event.py).


5 Note that this script may stop if the connection has problems. You will need to add a check that this listener is running and restart it if necessary! On linux server you can do that with a Cron job [>link<](https://en.wikipedia.org/wiki/Cron) for instance.