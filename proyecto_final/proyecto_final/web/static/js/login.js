const hacerLogin = async (usuario, contra) => {
    await fetch("http://127.0.0.1:8000/iniciar-login/", {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        method: 'POST',
        body: JSON.stringify({ correo: usuario, contra: contra })
    }).then(respuesta => respuesta.json()
    ).then(respuestajson => {
        if (respuestajson.estatus == "Error") {
            Swal.fire({
                title: "The Internet?",
                text: "That thing is still around?",
                icon: "error"
            });
        }else if (respuestajson.estatus=='ok'){
            window.location.replace('http://127.0.0.1:8000/home/');
        }
    });
}


const formulario = document.getElementById("formulario");

formulario.addEventListener("submit", async (e) => {
    e.preventDefault();
    console.log("como ta muchacho?");
    const correo = document.getElementById("correo");
    const contra = document.getElementById("contra");
    hacerLogin(correo.value, contra.value);
})

