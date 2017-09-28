const fs = require('fs')
var pictures_data = fs.readFileSync('public/pictures.json', 'utf8')
var dataObj = JSON.parse(pictures_data)

// Fisher-Yates shuffle for our array
function shuffle (array) {
    var i = 0
        , j = 0
        , temp = null

    for (i = array.length - 1; i > 0; i -= 1) {
        j = Math.floor(Math.random() * (i + 1))
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
    }
}

shuffle(dataObj)
pictures_data = JSON.stringify(dataObj)

const express = require('express')
const app = express()
const port = 5000
app.use(express.static('public'));

app.get('/', (request, response) => {
  response.sendfile('index.html')
})

// Router for ajax
app.get('/json/', (request, response) => {
    // Random error imitation
    if(Math.random() < 0.8) {
      response.send(pictures_data)
    } else {
      response.send(JSON.stringify(
          [{result: 'error'}]
      ))
    }

})

app.listen(port, (err) => {
  if (err) {
    return console.log('Something bad happened', err)
  }

  console.log(`Server is listening on ${port}`)
})
