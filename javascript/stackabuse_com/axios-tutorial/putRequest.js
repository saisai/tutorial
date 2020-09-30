const axios = require('axios').default;

const updatePost = {
    id: 1,
    userId: 1,
    title: 'A new title',
    body: 'Update this post'
};

const sendPutRequest = async () => {
    try {
        const resp = await axios.put('https://jsonplaceholder.typicode.com/posts/1', updatePost);
        console.log(resp.data);
    } catch(err) {
        console.log(err);
    }
}

sendPutRequest();
