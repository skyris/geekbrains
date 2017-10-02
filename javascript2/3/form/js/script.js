function validateForm() {
    var flagSubmit = true;
    var form = document.getElementById("form");
    var name = document.getElementById("name");
    if (isValidName(name.value)) {
        name.style.boxShadow = "0 0 10px #181";
        name.style.border = "1px solid #060";
        var nameFeedback = document.getElementById("name-feedback");
        nameFeedback.innerText = "";
    } else {
        name.style.boxShadow = "0 0 10px #811";
        name.style.border = "1px solid #600";
        var nameFeedback = document.getElementById("name-feedback");
        nameFeedback.innerText = "Please enter at least two characters";
        flagSubmit = false;
    }

    var phone = document.getElementById("phone");
    if (isValidPhone(phone.value)) {
        phone.style.boxShadow = "0 0 10px #181";
        phone.style.border = "1px solid #060";
        var phoneFeedback = document.getElementById("phone-feedback");
        phoneFeedback.innerText = "";
    } else {
        phone.style.boxShadow = "0 0 10px #811";
        phone.style.border = "1px solid #600";
        var phoneFeedback = document.getElementById("phone-feedback");
        phoneFeedback.innerText = "Please enter valid phone number";
        flagSubmit = false;
    }

    var email = document.getElementById("email");
    if (isValidEmail(email.value)) {
        email.style.boxShadow = "0 0 10px #181";
        email.style.border = "1px solid #060";
        var emailFeedback = document.getElementById("phone-feedback");
        emailFeedback.innerText = "";
    } else {
        email.style.boxShadow = "0 0 10px #811";
        email.style.border = "1px solid #600";
        var emailFeedback = document.getElementById("email-feedback");
        emailFeedback.innerText = "Please enter valid email";
        flagSubmit = false;
    }
    var message = document.getElementById("message");
    if (isValidMessage(message.value)) {
        message.style.boxShadow = "0 0 10px #181";
        message.style.border = "1px solid #060";
        var messageFeedback = document.getElementById("message-feedback");
        messageFeedback.innerText = "";
    } else {
        message.style.boxShadow = "0 0 10px #811";
        message.style.border = "1px solid #600";
        var messageFeedback = document.getElementById("message-feedback");
        messageFeedback.innerText = "Please some message";
        flagSubmit = false;
    }

    if(flagSubmit) {
        form.submit();
    }
}


function isValidName(name) {
   return /^[A-Za-zА-Яа-яёЁ]+$/.test(name);
}


function isValidPhone(phone) {
    return /\+\d{1}\(\d{3}\)\d{3}-\d{4}/.test(phone);
}


function isValidEmail(email) {
    return /[\w.-]+@\w+?\.[A-Za-z]{2,6}/.test(email);
}

function isValidMessage(text) {
   return text.length > 0;
}

