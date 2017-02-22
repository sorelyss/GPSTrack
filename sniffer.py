import socket
import MySQLdb
from datetime import datetime, timedelta

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  # your password
                     db="design")        # name of the data base444
cur = db.cursor()
query = ("INSERT INTO home_data(longitude,latitude,date) VALUES (%s,%s,%s)")

UDP_IP = "192.168.0.4"
UDP_PORT = 9220

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
  try:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data = data[1:33]
    if data[0:3]=="REV":
	    weeks = data[5:9]
	    sec = data[10:15]
	    slat = data[15]
	    
	    lat = data[16:18]
	    dlat = data[18:23]
	    lat_s = str(slat)+str(lat)+"."+str(dlat)
	    slon = data[23]
	    lon = data[24:27]
	    dlon = data[27:32]
	    lon_s = str(slon)+str(lon)+"."+str(dlon)
	    utc = datetime(1980,1,6)+timedelta(weeks=int(weeks))+timedelta(seconds=int(sec))
	    cot = utc-timedelta(hours=5)
	    
	    print "ADDRESS:      "+str(addr)
	    print "DATE/TIME:    "+str(cot)
	    print "LATITUD:      "+lat_s
	    print "LONGITUD:     "+lon_s
	    print "--------------------------------------------------------"
	    print "RAW DATA:"
	    print data
	    print weeks
	    print sec
	    print data[15:23]
	    print data[23:32]
	    print "--------------------------------------------------------"

	    cur.execute(query, (lon_s, lat_s, cot))
	    db.commit()

  except KeyboardInterrupt:
    break