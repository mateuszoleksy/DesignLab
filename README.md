# DesignLab
Repository for files associated with Design Laboratory. 
We chose Rack environment control.

#1
07.11.24 dostaliśmy moduł Raspberry Pi 4 Compute wraz z akcesoriami do przeprowadzania konfiguracji płytki.

#2
08.11.24 pomyślne uruchomienie płytki

#3
11.14.24 wgrywanie systemy operacyjnego na dysk nvme 

#4
11.14.24 system Ubuntu 24 LTS został pomyślnie wgrywany do pamięci nvme zainstalowanej w module

#5
11.14.24 pomyślna instalacja i uruchomienie lokalnego serwera z pomocą apache2

#6
11.17.24 realizacja głównego skryptu działającego w trybie "deamon" oraz bazy danych i strony internetowej na serwerze lokalnym.
Zrealizowana funkcja pobierania danych (tempertury) pod wskazanym adresem IP i wpisywania tych danych do bazy danych.

#7
26.11.24 dodanie pliku konfiguracyjnego, tak aby możliwa była modyfikacja połączenia bez wchodzenia w kod źródłowy

#8
9.12.24 dodanie obsługi bluetooth, poprawienie konfiguracji w celu zczytywania danych z danego adres IP. Do zrobienia poprawne dekodowanie danych pochodzacych z termometru BT.

#9
18.12.24 ostatni commit. Przygotowano program do testowania w laboratorium. Dodano nowe opcje do pliku konfiguracyjnego. Poniżej instrukcja do podstawowych danych.

#manual
Ubuntu:
User:pass = fit:alice
User:pass = root:1111


Database http://localhost/phpmyadmin
User:pass (privileges) = phpmyadmin:root (all privileges, non grant)
User:pass (privileges) = root:1111 (all privileges + grant)
User:pass (privileges) = fit:alice (~half privileges, account for editing suitable databases)

config.ini explanation 
[source] section is required for setup the proper connection to the database. You can provide an user and password to the database, host name and database name

[destination_ip]
This section introduces the possibility of getting some data from specific IP address ( for example in local network ). In addition with section [temp_page] you can specify the parent element of html layout and id of child element. 

[interval]
This section is slightly important. You can provide the maximul interval time (in days) the data in database is held. If yolu give e.g. number 1, one day data from actual time (if program is running) will be deleted. It calculates the interval within now and time in stored in database.

Useful commands (Ubuntu)
To on/off bluetooth: sudo rfkill toogle Bluetooth 
To restart/stop/start daemon: sudo systemctl restart/start/stop EnvironmentRackControl.service

