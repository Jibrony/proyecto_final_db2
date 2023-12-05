const options=document.getElementById("ayuda")
options.addEventListener("click", async (e) => {
    e.preventDefault();
    window.location.replace("http://127.0.0.1:8000/ingresar-duda/");
    
})