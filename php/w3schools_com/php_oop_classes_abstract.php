<?php

// parent class
abstract class Car {
    public $name;
    public function __construct($name) {
        $this->name = $name;
    }

    abstract public function intro(): string;
}

// child class
class Audi extends Car {
    public function intro(): string {
        return "Choose German quality! I'm a $this->name!";
    }
}

class Volvo extends Car {
    public function intro() : string {
        return "Proud to be Swedish! I am a $this->name!";
    }

}

class Citroen extends Car {
    public function intro(): string {
        return "French extravagance! I'm a $this->name!";
    }
}

// Create objects from the child classes
$audi = new audi("Audi");
echo $audi->intro();
echo PHP_EOL;

$volvo = new volvo("Volvo");
echo $volvo->intro();
echo "<br>";
echo PHP_EOL;


$citroen = new citroen("Citroen");
echo $citroen->intro();
echo PHP_EOL;
