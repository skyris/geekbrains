var path = require('path');
const fs = require('fs');

var pictures_data = fs.readFileSync(path.join(__dirname, 'public/json/pictures.json'), 'utf8');
var cities_data = fs.readFileSync(path.join(__dirname, 'public/json/cities.json'), 'utf8');
var dataObj = JSON.parse(pictures_data);

// Fisher-Yates shuffle for our array
function shuffle (array) {
    var i = 0
        , j = 0
        , temp = null;
    for (i = array.length - 1; i > 0; i -= 1) {
        j = Math.floor(Math.random() * (i + 1));
        temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}

const express = require('express');
const app = express();
const port = 5000;
app.use(express.static(path.join(__dirname, 'public')));


app.get('/feedback/', (req, res) => {
    res.sendfile('public/index.html');
});

app.get('/', (req, res) => {
    res.sendfile('index.html');
});


// Router for ajax
app.get('/json/:name', (req, res) => {
    if(req.params.name == "pics") {
        shuffle(dataObj);
        pictures_data = JSON.stringify(dataObj);
        res.send(pictures_data);
    } else if(req.params.name == "cities") {
        res.send(cities_data);
    } else {
        res.send("");
    }
    
});

app.listen(port, (err) => {
  if(err) {
    return console.log('Something bad happened', err);
  }

  console.log(`Server is listening on ${port}`);
});
