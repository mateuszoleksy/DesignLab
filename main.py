import requests
from bs4 import BeautifulSoup
import time
import mysql.connector
from datetime import datetime
import configparser
import binascii
import struct
import re
from bluepy.btle import UUID, Peripheral, BTLEException

p = Peripheral()
uuid = UUID(0x181a)

config = configparser.ConfigParser()

config.read('/home/fit/Desktop/config.ini')
config.sections()

mydb = mysql.connector.connect(
  host=config['source']['host'],
  user=config['source']['user'],
  password=config['source']['password'],
  database=config['source']['database']
)

mydbcursor = mydb.cursor()


while (1):
	# pobieramy strone pod danym adresem np 192.168.0.1
	r = requests.get(config['destionation']['temperature_ip'])
	# przeksztalcamy ja na kod html zrozumialy dla py
	soup = BeautifulSoup(r.content, 'html.parser')
	value = soup.findAll(id=config['temp_page']['id'])[3].text
	val = value.replace('°C', '')
	try:
		val = float(val)
	except:
		val = value
	now = datetime.now()
	current_time = now.strftime('%Y-%m-%d %H:%M:%S')
	
	sql = 'INSERT INTO dev_temp (date, temp) VALUES (%s, %s)'
	tab = (current_time, val)
	mydbcursor.execute(sql, tab)
	#usun stare rekord, domyslnie jest powyzej 1 minuty usuwane
	mydbcursor.execute('DELETE FROM dev_temp WHERE date <= now() - interval '+config['interval']['dev_temp_time'])
	mydb.commit()
	val = 0

	try:
		p.connect("38:1f:8d:58:21:34")
	except BTLEException as e:
		print("error")
	else:
		try:
			ch = p.getServiceByUUID(uuid).getCharacteristics()[0]

			val = ch.read()
			val = int.from_bytes(val, byteorder='little', signed=True)
			sql = 'INSERT INTO lab_temp (date, temp) VALUES (%s, %s)'
			tab = (current_time, val/100)
			mydbcursor.execute(sql, tab)
			#usun stare rekord, domyslnie jest powyzej 1 minuty usuwane
			mydbcursor.execute('DELETE FROM lab_temp WHERE date <= now() - interval '+config['interval']['dev_temp_time'])
			mydb.commit()

			p.disconnect()
		except BTLEException as e:
			continue
	finally:
		p.disconnect()

	# pobieramy zawartosc klasy albo id
	time.sleep(1)
