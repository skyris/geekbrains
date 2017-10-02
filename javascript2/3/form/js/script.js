function validateForm() {
    var flagSubmit = true;
    validateItem("name", isValidName, "Please enter at least two characters");
    validateItem("phone", isValidPhone, "Please enter valid phone number");
    validateItem("email", isValidEmail, "Please enter valid email");
    validateItem("message", isValidMessage, "Please enter your message");

    var form = document.getElementById("form");
    if(flagSubmit) {
        form.submit();
    }
}

function validateItem(id, validateFunction, feedbackMessage) {
    var element = document.getElementById(id);
    var elementFeedback = document.getElementById(id + "-feedback");
    if (validateFunction(element.value)) {
        element.style.boxShadow = "0 0 10px #181";
        element.style.border = "1px solid #060";
        elementFeedback.innerText = "";
    } else {
        element.style.boxShadow = "0 0 10px #811";
        element.style.border = "1px solid #600";
        elementFeedback.innerText = feedbackMessage;
        flagSubmit = false;
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

