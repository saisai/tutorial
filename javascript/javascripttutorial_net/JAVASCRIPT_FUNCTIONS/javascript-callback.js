function download(url, callback) {
    setTimeout(() => {
        // script to download the picture here
        console.log(`Downloading ${url} ...`);

        // process the picture once it is completed
        callback(url);
    }, 3000);
}

function process(picture) {
    console.log(`Processing ${picture}`);
}

let url = 'https://wwww.javascripttutorial.net/pic.jpg';
download(url, process);

console.log("hello");

function downloader(url, callback) {
    setTimeout(() => {
        // script to download the picture here
        console.log(`Downloading ${url} ...`);
        // process the picture once it is completed
        callback(url);

    }, 4000);
}

let urler = 'https://www.javascripttutorial.net/pic.jpg';
downloader(urler, function(picture) {
    console.log(`Processing ${picture}`);
}); 


function download1(url, success, failure) {
    setTimeout(() => {
        // script to download the picture here
        console.log(`Downloading ${url} ...`);
        // over simplification
        let error = url.length === 0 || !url; 
        // call the failure or success callback
        error ? failure(url) :  success(url);
    }, 3000);
}

download1('',
    function(picture) {
        console.log(`Processing the picture ${picture}`);
    },
    function(picture) {
        console.log(`Handling error...`);
    }
);
