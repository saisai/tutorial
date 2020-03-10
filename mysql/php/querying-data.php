<?php 

require_once "dbconfig.php";

try {
	
	$pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
	
	$sql = "SELECT lastName,
			firstName,
			jobTitle
			FROM employees
			WHERE lastName LIKE :lname OR
			firstName LIKE :fname;";
			
	// prepare statement for execution
	$q = $pdo->prepare($sql);
	
	// pass values to the query and execute it 
	//$q->execute();
	$q->execute(
		array(':lname' => '%i', ':fname' => 'M%')
		);
				
	$q->setFetchMode(PDO::FETCH_ASSOC);
	//var_dump($q->fetch());
	// print out the result set 
	while ($r = $q->fetch()){
		echo sprintf("%s <br />", $r['lastName']) . PHP_EOL;
	}
} catch (PDOException $e) {
	
	die("Could not connect to the database $dbname :" . $e->getMessage());
}