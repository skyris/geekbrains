const fs = require('fs')
const express = require('express')

var pictures_data = fs.readFileSync('json/pictures.json', 'utf8')
const app = express()
app.use(express.static('public'));
const port = 5000

app.get('/', (request, response) => {
  response.sendfile('html/index.html')
})


app.get('/json/', (request, response) => {
  response.send(pictures_data)
})

app.listen(port, (err) => {
  if (err) {
    return console.log('Something bad happened', err)
  }

  console.log(`Server is listening on ${port}`)
})
