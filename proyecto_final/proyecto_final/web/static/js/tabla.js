
let table = new DataTable('#tabla');


const verReporte=async (id)=>{
    console.log(id)
    await fetch(`http://127.0.0.1:8000/ver-reporte/${id}`).then(respuesta=>respuesta.json()).then(respuestaJSON=>{
        
        let dato=JSON.parse(respuestaJSON)
        console.log(dato)
        document.getElementById("Id_reporte").innerHTML=dato[0].pk;
        document.getElementById("incidencia").innerHTML=dato[0].fields.nombre_incidencia;
        document.getElementById("estatus").innerHTML=dato[0].fields.estatus;
        document.getElementById("calle_principal").innerHTML=dato[0].fields.calle_principal;
        document.getElementById("calle_secundaria").innerHTML=dato[0].fields.calle_secundario || '';
        document.getElementById("fecha_de_reporte").innerHTML=dato[0].fields.fecha_de_reporte;
        document.getElementById("descripcionInfo").innerHTML=dato[0].fields.descripcion;
        ebModal.style.display = "block";
    })
};

var ebModal = document.getElementById('mySizeChartModal');
var ebSpan = document.getElementsByClassName("ebcf_close")[0];

ebSpan.onclick = function() {
    ebModal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == ebModal) {
        ebModal.style.display = "none";
    }
}

var ebModal2 = document.getElementById('mySizeChartModal2');
var ebSpan2 = document.getElementsByClassName("ebcf_close")[1];
ebSpan2.onclick = function() {
    ebModal2.style.display = "none";
}
window.onclick = function(event) {
    if (event.target == ebModal2) {
        ebModal2.style.display = "none";
    }
}
const editarReporte=async (id)=>{
    console.log(id)
    await fetch(`http://127.0.0.1:8000/ver-reporte/${id}`).then(respuesta=>respuesta.json()).then(respuestaJSON=>{
        
        let dato=JSON.parse(respuestaJSON)
        console.log(dato)
        document.getElementById("Id_reporte2").innerHTML=dato[0].pk;
        document.getElementById("estatus2").value=dato[0].fields.estatus;
        document.getElementById("incidencia2").innerHTML=dato[0].fields.nombre_incidencia;
        document.getElementById("calle_principal2").innerHTML=dato[0].fields.calle_principal;
        document.getElementById("calle_secundaria2").innerHTML=dato[0].fields.calle_secundario || '';
        document.getElementById("fecha_de_reporte2").innerHTML=dato[0].fields.fecha_de_reporte;
        document.getElementById("descripcionInfo2").value=dato[0].fields.descripcion;
        document.getElementById("idReporte").value=dato[0].pk;
        ebModal2.style.display = "block";
    })
};
