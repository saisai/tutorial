<?php
// The following example shows how to prevent method overriding:
class Fruit {
    final public function intro() {
    }
}

class Strawberry extends Fruit {
    // will result in error
    public function intro() {

    }
}
