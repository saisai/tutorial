<?php

$servername ='localhost';
$username = 'root';
$password= 'root';

try {
    $conn = new PDO("mysql:host=$servername;dbname=ajaxtest", $username, $password);
    // set the pdo error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connected successfully";

    // close connection
    $conn = null;
}catch (PDOException $e) {
    echo "Connection failed: ". $e->getMessage();
}
