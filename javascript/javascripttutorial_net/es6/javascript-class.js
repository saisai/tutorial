function Animal(type) {
    this.type = type;

}

Animal.prototype.identify = function() {
    console.log(this.type);
};

var  cat = new Animal("Cat");
cat.identify();

