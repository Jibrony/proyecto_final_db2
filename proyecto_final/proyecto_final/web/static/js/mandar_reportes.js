const options=document.getElementById("ver-reportes-btn")
options.addEventListener("click", async (e) => {
    e.preventDefault();
    window.location.replace("http://127.0.0.1:8000/mostrar-reportes-admin/");
    
})