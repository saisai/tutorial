let app = new class {
    constructor(name) {
        this.name = name;
    }

    start() {
        console.log(`Starting the ${this.name}....`);
    }
}('Awesome App');

app.start();
