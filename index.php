<?php
 
global $host, $db_user, $db_pass, $db_name;
require_once "connect.php";

$connection = @new mysqli($host, $db_user, $db_pass, $db_name);

if ($connection->connect_errno!=0)
{
    echo "Error: ".$connection->connect_errno." Opis: ".$connection->connect_error;
}
else
{
$sql = "SELECT * FROM data ";
$result = $connection->query($sql);
$connection->close();
}
?>
<!DOCTYPE html>
<html lang="en">
 
<head>
    <meta charset="UTF-8">
    <title>MATEUSZ OLEKSY ADMINISTRACJA</title>
    <meta http-equiv="refresh" content="10">
    <style>
        table {
            margin: 0 auto;
            font-size: large;
            border: 1px solid black;
        }
 
        h1 {
            text-align: center;
            color: #006600;
            font-size: xx-large;
            font-family: 'Gill Sans', 'Gill Sans MT',
            ' Calibri', 'Trebuchet MS', 'sans-serif';
        }
 
        td {
            background-color: #E4F5D4;
            border: 1px solid black;
        }
 
        th,
        td {
            font-weight: bold;
            border: 1px solid black;
            padding: 10px;
            text-align: center;
        }
 
        td {
            font-weight: lighter;
        }
    </style>
</head>
 
<body>
    <section>
        <h1>Kontronik dane</h1>
        <table>
            <tr>
                <th>Time</th>
                <th>Temperature</th>
            </tr>
            <?php 
                while($rows=$result->fetch_assoc())
                {
            ?>
            <tr>
                <td><?php echo $rows['time'];?></td>
                <td><?php echo $rows['temperature'];?></td>
            </tr>
            <?php
                }
            ?>
        </table>
    </section>
</body>
 
</html>