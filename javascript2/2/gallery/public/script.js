console.log("hello");

// Get the modal
var modal = document.getElementById('myModal');
var modalImg = document.getElementById("modalImg ");
var captionText = document.getElementById("caption");
function modalOnClick(){
    console.log(this);
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
var from_server = '[ { "path": "img001_1200_800.jpeg", "thumbPath": "img001_300_200.jpeg", "desc": "" }, { "path": "img002_1200_800.jpeg", "thumbPath": "img002_300_200.jpeg", "desc": "" }, { "path": "img003_1200_800.jpeg", "thumbPath": "img003_300_200.jpeg", "desc": "" }, { "path": "img004_1200_800.jpeg", "thumbPath": "img004_300_200.jpeg", "desc": "" }, { "path": "img005_1200_800.jpeg", "thumbPath": "img005_300_200.jpeg", "desc": "" }, { "path": "img006_1200_800.jpeg", "thumbPath": "img006_300_200.jpeg", "desc": "" }, { "path": "img007_1200_800.jpeg", "thumbPath": "img007_300_200.jpeg", "desc": "" }, { "path": "img008_1200_800.jpeg", "thumbPath": "img008_300_200.jpeg", "desc": "" }, { "path": "img009_1200_800.jpeg", "thumbPath": "img009_300_200.jpeg", "desc": "" }, { "path": "img010_1200_800.jpeg", "thumbPath": "img010_300_200.jpeg", "desc": "" }, { "path": "img011_1200_800.jpeg", "thumbPath": "img011_300_200.jpeg", "desc": "" }, { "path": "img012_1200_800.jpeg", "thumbPath": "img012_300_200.jpeg", "desc": "" }, { "path": "img013_1200_800.jpeg", "thumbPath": "img013_300_200.jpeg", "desc": "" }, { "path": "img014_1200_800.jpeg", "thumbPath": "img014_300_200.jpeg", "desc": "" }, { "path": "img015_1200_800.jpeg", "thumbPath": "img015_300_200.jpeg", "desc": "" }, { "path": "img016_1200_800.jpeg", "thumbPath": "img016_300_200.jpeg", "desc": "" }, { "path": "img017_1200_800.jpeg", "thumbPath": "img017_300_200.jpeg", "desc": "" }, { "path": "img018_1200_800.jpeg", "thumbPath": "img018_300_200.jpeg", "desc": "" }, { "path": "img019_1200_800.jpeg", "thumbPath": "img019_300_200.jpeg", "desc": "" }, { "path": "img020_1200_800.jpeg", "thumbPath": "img020_300_200.jpeg", "desc": "" }, { "path": "img021_1200_800.jpeg", "thumbPath": "img021_300_200.jpeg", "desc": "" } ]';
var picsData = JSON.parse(from_server);
var galleryFrame = document.getElementById("galleryFrame");
var picturesArray = [];
for(var currPicData of picsData) {
    var pictureElement = new Picture(currPicData);
    var elem = pictureElement.makeElement();
    elem.onclick = modalOnClick;
    galleryFrame.appendChild(elem);
    picturesArray.push(elem);
}



