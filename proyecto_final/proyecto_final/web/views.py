from django.shortcuts import render, redirect
from .models import Usuario
from .models import TokenUsuario
from .models import CatalogoIncidencia
from .models import ReporteDeIncidencia
from .models import TicketDeIncidencia
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
import json
import uuid
from datetime import date, datetime, timedelta
from django.utils.timezone import make_aware

# Create your views here.
def paginaPrincipal(request):
    if 'token' in request.session:
        print (request.session["token"])
        listaTokenDelUsuario=TokenUsuario.objects.filter(token=request.session["token"])
        if listaTokenDelUsuario.count()==1:
            loginrol=listaTokenDelUsuario[0].id_usuario.rol
            print(listaTokenDelUsuario[0].id_usuario.fecha_nac.year)
        else:
            logout(request)
        #  puedes consultar usuario
        # verificar el usuario
        # redirenccionar si no tiene permisos
        # return redirect('/generar-reporte')
        return render(request, 'index.html',{"rol":listaTokenDelUsuario[0].id_usuario.rol})
    else:
        return redirect('/iniciar-sesion')
    

def updateaReporte (request):
    estatus=request.POST.get('estatus',False)
    descripcion=request.POST.get('descripcion',False)
    id_reporte=request.POST.get('idReporte',False)
    objeto=ReporteDeIncidencia.objects.get(id_reporte=id_reporte)
    objeto.descripcion=descripcion
    objeto.estatus=estatus
    objeto.save()
    return redirect('/mostrar-reportes-admin')

def verUsuario(request):
    lista_usuario=TokenUsuario.objects.filter(token=request.session["token"])
    print(lista_usuario.count())
    if 'token' in request.session:
        print (request.session["token"])
        listaTokenDelUsuario=TokenUsuario.objects.filter(token=request.session["token"])
        if listaTokenDelUsuario.count()==1:
            loginrol=listaTokenDelUsuario[0].id_usuario.rol
    return render(request, 'back.html',{'lista_usuario':lista_usuario,'rol':loginrol})

def ayuda(request):
    return render(request, 'ayuda.html')

def verReporte(request,id_reporte):
    print(id_reporte)
    Reporte=serializers.serialize("json", [ReporteDeIncidencia.objects.get(id_reporte=id_reporte),])
    return JsonResponse(Reporte,safe=False)

def verTablasAdmins(request):
    tipoincidencia=request.GET.get('tipo',False)
    lista_de_incidencias=ReporteDeIncidencia.objects.filter(clave_de_incidencia=tipoincidencia)
    if 'token' in request.session:
        print (request.session["token"])
        listaTokenDelUsuario=TokenUsuario.objects.filter(token=request.session["token"])
        if listaTokenDelUsuario.count()==1:
            loginrol=listaTokenDelUsuario[0].id_usuario.rol
    return render(request, 'mostrar_tablas_admin.html',{"lista_de_incidencias":lista_de_incidencias, 'rol': loginrol})

def consultarDudar(request):
    return render(request, 'indexDuda.html')

def ingresarDudas(request):
    if request.method == 'POST':
        idUsuario=TokenUsuario.objects.get(token=request.session["token"]).id_usuario
        nombreUsuario=request.POST.get('nombre',False)
        descripcion=request.POST.get('dudas',False)
        TicketDeIncidencia.objects.create(id_usuario=idUsuario,
                                        nombre_usuario=nombreUsuario,
                                        comentario=descripcion,
                                        fecha_hora=None)
    return redirect('/ayuda')

def mostrarReportes(request):
    tipoincidencia=request.GET.get('tipo',False)
    lista_de_incidencias=ReporteDeIncidencia.objects.filter(clave_de_incidencia=tipoincidencia)
    print(lista_de_incidencias.count())
    return render(request,'Mostrar_tablas.html',{"lista_de_incidencias":lista_de_incidencias})

def mostrarReportesAdmin(request):
    tipoincidencia=request.GET.get('tipo',False)
    lista_de_incidencias=ReporteDeIncidencia.objects.filter(clave_de_incidencia=tipoincidencia)
    print(lista_de_incidencias.count())
    return render(request,'incidenciasAdmin.html',{"lista_de_incidencias":lista_de_incidencias})

def tiposIncidencia(request):
    return render(request, 'incidencias.html')

def generarReporte(request):
    if request.method == 'POST':
        tipo_incidencia=request.POST.get('incidencia',False)
        id_usuario=TokenUsuario.objects.get(token=request.session["token"]).id_usuario
        objCatalogoIncidencia=CatalogoIncidencia.objects.get(clave_incidencia=tipo_incidencia)
        print(objCatalogoIncidencia.incidencia)
        calle_principal=request.POST.get('calle_principal',False)
        calle_secundaria=request.POST.get('calle_secundaria',False)
        descripcion=request.POST.get('descripcion',False)
        ReporteDeIncidencia.objects.create(clave_de_incidencia=objCatalogoIncidencia,
                                        id_usuario=id_usuario,
                                        nombre_incidencia=objCatalogoIncidencia.incidencia,
                                        calle_principal=calle_principal,
                                        calle_secundaria=calle_secundaria,
                                        fecha_de_reporte=None,
                                        descripcion=descripcion)
    return render(request, 'generar_reporte.html')

def iniciarSesion(request):
    return render(request, 'iniciar.html')

def logout(request):
    if 'token' in request.session:
        del request.session["token"]
        # puedes consultar usuario
        # verificar el usuario
        # redirenccionar si no tiene permisos
        # return redirect('/generar-reporte')
        return redirect('/iniciar-sesion')
    else:
        return redirect('/iniciar-sesion')


def registro(request):
    print(' registro')
    if request.method == 'POST':

        nombre_usuario = request.POST.get('nombre', False)
        primer_apellido = request.POST.get('apellido1', False)
        segundo_apellido = request.POST.get('apellido2', '')
        fecha_nac = request.POST.get('fechaNacimiento', False)
        correo_electronico = request.POST.get('correo', False)
        password = request.POST.get('contraseña', False)
        numero_telefono = request.POST.get('telefono', False)

        # Verificar si el correo electrónico ya existe en la base de datos
        if Usuario.objects.filter(correo_electronico=correo_electronico).exists():
            print("El correo electrónico ya está registrado. Por favor, elige otro.")
            # Puedes agregar un mensaje de error y redirigir a la página de registro nuevamente
            return render(request, 'registrarse.html', {'error': 'El correo electrónico ya está registrado. Por favor, elige otro.'})
               # Convertir la fecha de nacimiento de string a objeto datetime
        fecha_nac = datetime.strptime(fecha_nac, '%Y-%m-%d').date()

        # Calcular la edad comparando con la fecha actual
        edad = (datetime.now().date() - fecha_nac) // timedelta(days=365.25)

        if edad < 18:
            print("El usuario debe ser mayor de 18 años para registrarse.")
            # Puedes agregar un mensaje de error y redirigir a la página de registro nuevamente
            return render(request, 'registrarse.html', {'error': 'Debes ser mayor de 18 años para registrarte'})

        # fecheObj=make_aware(datetime.strptime(fecha_nac, "%Y-%m-%d"))
        # print(fecheObj.year)
        # if (fechaObj.year - date.today.year) < 18 :
        #     print('hola mundo')
        # listaTokenDelUsuario=TokenUsuario.objects.filter(token=request.session["token"])
        
        print(f"Nombre: {nombre_usuario}")
        print(f"Primer Apellido: {primer_apellido}")
        print(f"Segundo Apellido: {segundo_apellido}")
        print(f"Fecha nacimiento: {fecha_nac}")
        print(f"correo: {correo_electronico}")
        print(f"pass: {password}")
        print(f"num: {numero_telefono}")
        
        Usuario.objects.create(nombre_usuario=nombre_usuario,
                            primer_apellido=primer_apellido,
                            segundo_apellido=segundo_apellido,
                            fecha_nac=fecha_nac,
                            correo_electronico=correo_electronico,
                            password=password,
                            numero_telefono=numero_telefono)
        print("Usuario creado correctamente.")
        print("Usuario guardado correctamente.")
        # Redireccionar a la página de inicio de sesión u otra página
        return redirect('/iniciar-sesion')  # Reemplaza con el nombre de tu vista de inicio de sesión

    # Si la solicitud no es POST, simplemente renderiza el formulario de registro
    return render(request, 'registrarse.html')

@csrf_exempt
def iniciarLogin(request):
    print("toy bien muchacho")
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        correo = body['correo']
        contra = body['contra']
        print(contra)
        print(correo) 
        r = Usuario.objects.filter(correo_electronico=correo, password=contra)
        if r.count() == 1:
            existe_token = TokenUsuario.objects.filter(id_usuario=r[0])
            myuuid = uuid.uuid4()
            if existe_token.count() == 1:
                TokenUsuario.objects.filter(id_usuario=r[0]).update(token=myuuid)
                print(r[0].id_usuario)
                print(myuuid)
            else:
                TokenUsuario.objects.create(id_usuario=r[0], token=myuuid)
            request.session["token"]=str (myuuid)
            dato = {'estatus': "ok"}
            return JsonResponse(dato)
        print(r.count())
        return JsonResponse({'estatus':'Error'})
