import * as $ from 'jquery';
import axios from 'axios';






$("#loginButton").prop( "disabled", true );



const API_URL = "/api/";

function getGeneralWarningMessage(input) {
    if (input.length === 0) {
        return "Пустое поле";
    } else if (input.length < 3) {
        return "Слишком коротко";
    }
    return null;
}

function getUsernameWarningMessage(login) {
    const generalMessage = getGeneralWarningMessage(login);
    if (generalMessage != null) {
        return generalMessage;
    }
    return "";
}

function getPasswordWarningMessage(password) {
    const generalMessage = getGeneralWarningMessage(password);
    if (generalMessage != null) {
        return generalMessage;
    } else if (password.length < 6) {
        return "Слишком коротко";
    }
    return "";
}

function validateLoginForm() {
    const username = $("#usernameInput").val().trim();
    const usernameWarning = getUsernameWarningMessage(username);
    if (usernameWarning) {
        $("#usernameWarning").css("visibility", "visible");
        $("#usernameWarning").html(usernameWarning);
    } else {
        $("#usernameWarning").css("visibility", "hidden");
    }

    const password = $("#passwordInput").val().trim();
    const passwordWarning = getPasswordWarningMessage(password);
    if (passwordWarning) {
        $("#passwordWarning").css("visibility", "visible");
        $("#passwordWarning").html(passwordWarning);
    } else {
        $("#passwordWarning").css("visibility", "hidden");

    }

    if (!usernameWarning && !passwordWarning) {
        $("#loginButton").prop("disabled", false);

    } else {
        $("#loginButton").prop("disabled", true);
    }
}


function login() {
    axios.post(`${API_URL}auth`, $("#loginForm").serialize())
        .then(response => {
            alert('Успешная авторизация. Токен: ' + response.data.token);
            console.log(response);
        })
        .catch(error => alert('Неверные данные, попробуйте еще раз.'));
}

$("#loginButton").click(login);
$("#loginForm").focusout(validateLoginForm);
