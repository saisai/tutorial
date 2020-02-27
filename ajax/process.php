<?php 
// https://www.youtube.com/watch?v=82hnvUYY6QA
// connect to a database 

$conn = mysqli_connect('localhost', 'root', 'root', 'ajaxtest');

echo 'Processing...';

// check for post variable
/*
if(isset($_POST['name']))
{
	echo 'POST: YOur name is '. $_POST['name'];
}
*/


if(isset($_POST['name']))
{
	$name = mysqli_real_escape_string($conn, $_POST['name']);
	
	echo 'POST: YOur name is '. $_POST['name'];
	
	$query = "INSERT INTO users(name) VALUES ('$name')");
	
  if(mysqli_query($conn, $query)){
    echo 'User Added...';
  } else {
    echo 'ERROR: '. mysqli_error($conn);
  }
}
// check for get variable
if(isset($_GET['name']))
{
	echo 'GET: YOur name is '. $_GET['name'];
}



