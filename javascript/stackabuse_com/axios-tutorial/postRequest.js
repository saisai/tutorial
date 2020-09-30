const axios = require('axios').default;

const newPost = {
    userId: 1,
    title: 'A new post',
    body: 'This is the boyd of the new post'
};

const sendPostRequest = async () => {
   try {
        const resp = await axios.post('https://jsonplaceholder.typicode.com/posts', newPost);

        console.log(resp.data);
    } catch(err) {
        console.log(err);
    }
};
sendPostRequest();
