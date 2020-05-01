import axios from 'axios';
console.log('hello world starterkit');



function getGeneralWarningMessage(input) {
    if (input.length === 0) {
        return "Пустое поле";
    } else if (input.length < 3) {
        return "Слишком коротко"
    }
    return null
}

function getUsernameWarningMessage(login) {
    const generalMessage = getGeneralWarningMessage(login);
    if (generalMessage != null) {
        return generalMessage
    }
    return ""
}

function getPasswordWarningMessage(password) {
    const generalMessage = getGeneralWarningMessage(password);
    if (generalMessage != null) {
        return generalMessage
    }
    return ""
}

export function login() {
    const username = $("#usernameInput").val().trim()
    const usernameWarning = getUsernameWarningMessage(username);
    if (usernameWarning) {
        $("#usernameWarning").show().html(usernameWarning);
    } else {
        $("#usernameWarning").hide()
    }

    const password = $("#passwordInput").val().trim()
    const passwordWarning = getPasswordWarningMessage(password);
    if (passwordWarning) {
        $("#passwordWarning").show().html(passwordWarning);
    } else {
        $("#passwordWarning").hide()
    }


    ///   import axios from 'axios'; axios.post('/auth', { username: username, password: password }) .then(function (response) { console.log(response); }) .catch(function (error) { console.log(error); });

}