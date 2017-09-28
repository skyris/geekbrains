
// Get the modal
var modal = document.getElementById('myModal');
var modalImg = document.getElementById("modalImg ");
var captionText = document.getElementById("caption");
function modalOnClick(){
    modal.style.display = "block";
    modalImg.src = this.getAttribute("pic");
    captionText.innerHTML = this.alt;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
        modal.style.display = "none";
    };

    function generateClassPicture() {
        var id = 0;
        return function ({desc, path, thumbPath}) {
            id += 1;
            this.id = "img" + id;
            this.desc = desc;
            this.path = path;
            this.thumbPath = thumbPath;
        }
    }
var Picture = generateClassPicture();

Picture.prototype.render= function() {
    return "<img id='" + this.id + "' class='gallery' src='" + this.path + "'" +
        " alt='" + this.desc + "' width='300' height='200'>";
};

Picture.prototype.makeElement = function() {
    var img = document.createElement("img");
    img.src = "images/" + this.thumbPath;
    img.id = this.id;
    img.className = "gallery";
    img.alt = this.desc;
    img.width = "300";
    img.height = "200";
    img.setAttribute("pic", "images/" + this.path)
    return img;
};

var galleryFrame = document.getElementById("galleryFrame");
var picturesArray = [];

var xhr = new XMLHttpRequest();
xhr.open("GET", "/json/", true);
xhr.timeout = 15000;
xhr.ontimeout = function () {
    console.log("Timeout expired!");
};
xhr.send(null);
var dataFromServer;
xhr.onreadystatechange = function () {
   if(xhr.readyState == xhr.DONE && xhr.status == 200) {
     dataFromServer = JSON.parse(this.responseText);
     if(dataFromServer[0].result != "error") {
       for(var currData of dataFromServer ) {
           var pictureElement = new Picture(currData);
           var elem = pictureElement.makeElement();
           elem.onclick = modalOnClick;
           galleryFrame.appendChild(elem);
           picturesArray.push(elem);
       }
     } else {
         console.log("Fail to load ajax");
     }
   }
};



