// $(function () {
//     var inputFields = $("input:text, input:password, textarea, input[type=email]");
//
//     inputFields.focus(function () {
//         $(this).css("box-shadow", "0 0 10px #666");
//     });
//
//
//     inputFields.blur(function () {
//         $(this).css("box-shadow", "none");
//     });
//
//     $("#nameField").blur(function () {
//         if ($(this).val().length < 3) {
//             $(this).css("box-shadow", "0 0 10px red");
//         } else {
//             $(this).css("box-shadow", "0 0 10px green");
//         }
//     });
//
// });

// $(function () {
//     var checkBox = $(".checkbox");
//     if (checkBox.prop("checked")) {
//         checkBox.add("label[for='cb']").css("box-shadow", "0 0 4px green");
//     }
//     checkBox.change(function () {
//         var isChecked = checkBox.is(":checked");
//         if (isChecked) {
//             $(this)..text()add("label[for='cb']").css("box-shadow", "0 0 4px green");
//         } else {
//             $(this).add("label[for='cb']").css("box-shadow", "0 0 4px red");
//         }
//     });
// });

// $(function () {
//     $("#sel").change(function () {
//         var selectedOption = $(this).find(":selected").text();
//         alert(selectedOption);
//     });
// });

// $(function () {
//     $("#form").submit(function (event) {
//         var textarea = $("#message");
//         // console.log("in here");
//         if (textarea.val().trim() == "") {
//             textarea.css("box-shadow", "0 0 10px red");
//             event.preventDefault();
//         }
//     });
// });

$(function () {
    var form = $("#form");
    enableFastFeadback(form);
    form.submit(function (event) {
        var name = $("#name").val();
        var password = $("#password").val();
        var message = $("#message").val();
        var checked = $("#cb").is(":checked");
        ValidateNameField(name, event);
        ValidatePasswordField(password, event);
        ValidateMessageField(message, event);
        ValidateCheckboxField(checked, event);
    });
});

function enableFastFeadback(formElement) {
    var nameInput = formElement.find("#name");
    var passwordInput = formElement.find("#password");
    var messageInput = formElement.find("#message");
    var checkboxInput = formElement.find("#cb");

    nameInput.blur(function (event) {
        var name = $(this).val();
        ValidateNameField(name, event);
        if (!isValidName(name)) {
            $(this).css({"box-shadow": "0 0 10px #811", "border": "1px solid #600"});
        } else {
            $(this).css({"box-shadow": "0 0 10px #181", "border": "1px solid #060"});
        }
    });
    passwordInput.blur(function (event) {
        var name = $(this).val();
        ValidatePasswordField(name, event);
        if (!isValidName(name)) {
            $(this).css({"box-shadow": "0 0 10px #811", "border": "1px solid #600"});
        } else {
            $(this).css({"box-shadow": "0 0 10px #181", "border": "1px solid #060"});
        }
    });
    messageInput.blur(function (event) {
        var message = $(this).val();
        ValidateMessageField(message, event);
        if (!isValidMessage(message)) {
            $(this).css({"box-shadow": "0 0 10px #811", "border": "1px solid #600"});
        } else {
            $(this).css({"box-shadow": "0 0 10px #181", "border": "1px solid #060"});
        }
    });
    checkboxInput.change(function (event) {
        var checked = $(this).is(":checked");
        ValidateCheckboxField(checked, event);
        if (!checked) {
            $(this).add("label[for='cb']").css({"box-shadow": "0 0 10px #811", "border": "1px solid #600"});

        } else {
            $(this).add("label[for='cb']").css({"box-shadow": "0 0 10px #181", "border": "1px solid #060"});
        }
    });

}

function ValidateNameField(name, event) {
    if (!isValidName(name)) {
        $("#name-feedback").text("Please enter at least two characters").css("color", "red");
        event.preventDefault();
    } else {
        $("#name-feedback").text("");
    }
}

function ValidatePasswordField(password, event) {
    if (!isValidPassword(password)) {
        $("#password-feedback").text("Password should have at least six characters and contain a number").css("color", "red");
        event.preventDefault();
    } else {
        $("#password-feedback").text("");
    }
}

function ValidateMessageField(message, event) {
    if (isValidMessage(message)) {
        $("#message-feedback").text("Please enter a message").css("color", "red");
        event.preventDefault();
    } else {
        $("#message-feedback").text("");
    }
}

function ValidateCheckboxField(checked, event) {
    if (!checked) {
        $("#checkbox-feedback").text("Please agree to this").css("color", "red");
        event.preventDefault();
    } else {
        $("#cb").css("box-shadow", "none");
        $("#checkbox-feedback").text("");
    }
}


function isValidName(name) {
    return name.length >= 2;
}

function isValidPassword(password) {
    return password.length >= 6 && /.*[0-9]*./.test(password);
}

function isValidMessage(message) {
    return message.trim() != "";
}
