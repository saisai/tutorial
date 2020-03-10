<?php 

require_once "dbconfig.php";

try {
	$pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
	
	// execute the stored procedure
	$sql = "CALL GetCustomers()";
	// call the stored procedure 
	$q = $pdo->query($sql);
	$q->setFetchMode(PDO::FETCH_ASSOC);
	
} catch (PDOException $e) {
	die("Error occured :" . $e->getMessage());
}

while ($r = $q->fetch()):
	echo sprintf("%s ", $r['customerName']) . PHP_EOL;
	echo sprintf('$ %.2f',$r['creditlimit']) . PHP_EOL;
	echo sprintf('$ %.2f',number_format($r['creditlimit'], 2)) . PHP_EOL;
	echo '$' . number_format($r['creditlimit'], 2) . PHP_EOL;
endwhile;