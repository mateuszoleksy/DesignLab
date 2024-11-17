import requests
from bs4 import BeautifulSoup
import time
import mysql.connector
from datetime import datetime


mydb = mysql.connector.connect(
  host="localhost",
  user="alice",
  password="fit",
  database="kontronik_control"
)

mydbcursor = mydb.cursor()


# pobieramy strone pod danym adresem oraz domyslnie program dziala jako deamon
while (1):
   
    r = requests.get("https://mateuszoleksy.github.io/")
    # przeksztalcamy ja na kod html zrozumialy dla py
    soup = BeautifulSoup(r.content, 'html.parser')
    value = soup.find("div",id="title").text
    

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    
    
    sql = "INSERT INTO data (time, temperature) VALUES (%s, %s)"
    val = (current_time, value)
    mydbcursor.execute(sql, val)

    mydb.commit()

    # pobieramy zawartosc klasy albo id 
    print(time.ctime)
    f = open("index.html", "w")
    f.write('''
            <html>
                <head>
                <title>Temperatura RACK</title>
                </head>
                <body>
                    <h1>Temperatura w szafie RACK wynosi: '''+value+" time: "+current_time+'''</h1>
                </body>
            </html>
            ''')
    f.close()
    
    time.sleep(3)

