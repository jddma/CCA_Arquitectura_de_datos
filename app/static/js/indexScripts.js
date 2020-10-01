$(document).ready(function () {

    $("#btn").click(function () {
        formSubmit();
    });

    $(".btn-alert-exit").click(function () {
        $("#alert").removeClass("alert-active");
    });

    function formSubmit() {
        if ($("#email")[0].checkValidity()) {
            if ($("#password")[0].checkValidity()) {
                let msgData = {};
                msgData["email"] = $("#email").val();
                msgData["password"] = $("#password").val();
                msgData = JSON.stringify(msgData);

                let requestSettings = {
                    "url": "/controllers/login",
                    "method": "POST",
                    "timeout": 0,
                    "headers": {
                        "Content-Type": "application/json"
                    },
                    "data": msgData,
                    error: function () {
                        showAlert("Error");
                    }
                };

                $.ajax(requestSettings).done(function (response) {
                    switch (response) {
                        case "Credentials error":
                            showAlert("Datos incorrectos");
                            break;
                        case "Success":
                            location.href = "/panel";
                            break;
                    }
                });
            }
            else {
                showAlert("Ingrese una contraseña");
            }
        }
        else {
            showAlert("Ingrese un correo válido");
        }
    }

    function showAlert(mensaje) {
        $(".login-box")[0].reset();
        $("#alert").contents().filter(function () {
            return this.nodeType === 3;
        }).remove();
        $("#alert").append(mensaje)
        $("#alert").addClass("alert-active");
    }

});