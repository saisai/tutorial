const fs =require('fs')

const getFiles = (filename) => {
  return new Promise((resolve, reject) => {
    fs.readFile(filename, (err, data)=>{
      if(err) {
        reject(err)
        return
      }
      resolve(data)
    })
  })
}

getFiles('/etc/passwd')
  .then(data=>console.log(data))
  .catch(err => console.log(err));
