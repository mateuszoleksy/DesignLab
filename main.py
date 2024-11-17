import requests
from bs4 import BeautifulSoup
import time
import mysql.connector
from datetime import datetime


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database="kontronik_control"
)

mydbcursor = mydb.cursor()


while (1):
    # pobieramy strone pod danym adresem np 192.168.0.1
    r = requests.get("https://mateuszoleksy.github.io/")
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

