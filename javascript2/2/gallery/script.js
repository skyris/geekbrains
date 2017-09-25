/**
 * Created by victor on 26.09.17.
 */
var modal = document.getElementById("myModal");

var img = document.getElementById("img01");
var modalImg = document.getElementById("modalImg");
var captionText = document.getElementById("caption");
img.onclick = function () { modal.style.display = "block";
    modalImg.scr = this.src;
    captionText.innerHTML = this.alt;
};

var span = document.getElementsByClassName("close")[0];

span.onclick = function() {
    modal.style.display = "none";
};
