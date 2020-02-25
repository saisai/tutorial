<?php

$test = array(1, 2, 3, 4, 5);

//$tester = array();
print_r($test);

foreach($test as &$key)
{
    $key = $key * 2;
}

//unset($test); // break the reference with the last element
print_r($test);

// https://www.youtube.com/watch?v=sxh2WZeiclQ
// at 5:35

?>
