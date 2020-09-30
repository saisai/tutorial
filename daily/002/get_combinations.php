<?php

function get_combinations($arrays) {
	$result = array(array());
	//foreach ($arrays as $property => $property_values) {
	foreach ($arrays as $property_values) {
		$tmp = array();
		foreach ($result as $result_item) {
			foreach ($property_values as $property_value) {
				//$tmp[] = array_merge($result_item, array($property => $property_value));
				$tmp[] = array_merge($result_item, array($property_value));
			}
		}
		$result = $tmp;
	}
	return $result;
}

$test = array(
		'item1' => array('A', 'B'),
		'item2' => array('C', 'D'),
		'item3' => array('E', 'F'),
	);
$tester= 	array(
		 array('A', 'B'),
		 array('C', 'D'),
		array('E', 'F'),
	);
$woo = array("zip", "zoo");
$tester01 = array(
		 array(1, 2, 3),
		 array(4, 5),
		 array(6, 7, 8),
		 array(9, 10, 11, 12),
		 array('A', 'B', 'C'),
		 $woo,
		);
$combinations = get_combinations( $tester01 ) ;

$ss = sizeof($combinations);
for($i=0; $i < $ss; $i++)
{
	$jj = sizeof($combinations[$i]);
	//var_dump($combinations[$i]);
	for($j=0; $j < $jj; $j++)
	{
		echo $combinations[$i][$j]." ";
	}
	echo PHP_EOL;
}
//var_dump($combinations);
?>
