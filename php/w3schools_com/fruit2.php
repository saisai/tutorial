<?php

class Fruit {
    public $name;
    public $color;
    public $weight;

    function set_name($n) { // public function (default)
        $this->name = $n;
    }

    protected function set_color($n) { // protected function
        $this->color = $n;
    }

    private function set_weight($n) {   // private function
        $this->weight = $n;
    }
}

$mango = new Fruit();
$mango->set_name('Mango'); // ok
$mango->set_color('Yello'); // ERROR
$mango->set_weight('300'); // ERROR

