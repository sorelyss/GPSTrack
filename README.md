# El camión del Tío
This is a webpage where you can track a device with GPS and also includes the sniffer for the communication with the device.

## Device and Server
We developed a sniffer who listens an UDP port where the mobile device can update its position. It also uploads the decoded info to a mysql database. It was made with python 2.7. It can handle an input of depth of a water body associated with the position of the measure.

## Webpage
This is an user-friendly webpage developed in Django. It shows the last position and depth of the mobile and also the historic routes of this mobile on a map of Google Maps Javascript API and a char of Google Charts API. And finally it can make a 3D plot of the historics depths/positions using the Plotly Javascript API.

You can see a live view of this webpage at: http://gpstracker.ddns.net/
