<?php

$test = '["2",["2","6","7","8","9"]]';

var_dump(json_encode($test));
$rr = json_decode($test);
echo $rr[0];
var_dump($rr[1]);

/*
echo sizeof($test);
$rr = array_map('intval', $test[0][1]);

var_dump($rr);
*/


?>
