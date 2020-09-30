const express = require('express')
const path = require('path')
const app = express()
const port = 3000
const host = '192.168.0.150'
//app.get('/', (req, res) => res.send('Hello World!'))

//app.listen(port, host, () => console.log(`Example app listening on port ${port}!`))

app.use(express.json())
app.use(express.urlencoded({extended: false}))

app.get('/', (req, res) => {
    //res.send("Hello from express")
    //res.send({msg: 'hello'})
    //res.json({msg: 'hello'})
    //res.send(req.header('host'))
    //res.send(req.header('user-agent'))
    res.send(req.rawHeaders)
})

app.listen(port, host, () => console.log('Server started on 3000'))

