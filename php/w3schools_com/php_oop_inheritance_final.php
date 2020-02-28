<?php

// The final keyword can be used to prevent class inheritance or to prevent method overriding.
final class Fruit {
    //some code
}

// will result in error
class Strawberry extends Fruit {
    // some code
}
