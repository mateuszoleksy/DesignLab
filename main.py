import requests
from bs4 import BeautifulSoup
import time
import mysql.connector
from datetime import datetime
import configparser


config = configparser.ConfigParser()

config.read("config.ini")
config.sections()



mydb = mysql.connector.connect(
  host=config["source"]["host"],
  user=config["source"]["user"],
  password=config["source"]["password"],
  database=config["source"]["database"]
)

mydbcursor = mydb.cursor()


while (1):
    # pobieramy strone pod danym adresem np 192.168.0.1
    r = requests.get(config["destionation"]["temperature_ip"])
    # przeksztalcamy ja na kod html zrozumialy dla py
    soup = BeautifulSoup(r.content, 'html.parser')
    value = soup.find("div",id="title").text
    

    now = datetime.now()

    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    
    sql = "INSERT INTO data (time, temperature) VALUES (%s, %s)"
    val = (current_time, value)
    mydbcursor.execute(sql, val)
    #usun stare rekord, domyslnie jest powyzej 1 minuty usuwane
    mydbcursor.execute("DELETE FROM data WHERE time <= now() - interval 1 minute")
    mydb.commit()

    # pobieramy zawartosc klasy albo id 

    time.sleep(3)

