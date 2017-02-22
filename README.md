# El camión del Tío
This is a webpage where you can track a device with GPS and also includes the sniffer for the communication with the device.

## Device and Server
We developed a sniffer who listens an UDP port where the mobile device can update its position. It also uploads the decoded info to a mysql database. It was made with python 2.7.

## Webpage
This is an user-friendly webpage developed in Django. It shows the last position of the mobile in a table and an interactive map.
