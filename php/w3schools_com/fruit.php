<?php

class Fruit {
    public $name;
    protected $color;
    private $weight;
}

$mango = new Fruit();
$mango->name = 'Mango'; // ok
$mango->color = 'Yello'; // ERROR
$mango->weight = '300'; // ERROR

