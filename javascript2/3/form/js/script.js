function formValidation() {
    
}



function isValidName(name) {
   return /^[A-Za-zА-Яа-яёЁ]+$/.test(name);
}


function isValidPhone(phone) {
    return /\+\d{1}\(\d{3}\)\d{3}-\d{4}/.test(phone);
}


function isValidEmail(email) {
    return /.\.[A-Za-z]{2,6}/.test(email);
}

function isValidMessage(text) {
   return text.length > 0;
}


function () {

}