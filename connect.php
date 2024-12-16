<?php

    $config = parse_ini_file("/home/fit/Desktop/config.ini", true);

    $host = $config["source"]["host"];
    $db_pass = $config["source"]["password"];
    $db_user = $config["source"]["user"];
    $db_name = $config["source"]["database"];
