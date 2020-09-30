const axios = require('axios').default;

axios.get('https://jsonplaceholder.typicode.com/posts')
    .then(resp => {
        console.log(resp.data);
    })
    .catch(err => {
        // handle error here
        console.log(err);
    })
