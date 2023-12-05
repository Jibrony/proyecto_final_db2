"""
URL configuration for proyectoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.iniciarSesion),
    path('iniciar-sesion/', views.iniciarSesion),
    path('home/', views.paginaPrincipal),
    path('registro/', views.registro),
    path('generar-reporte/', views.generarReporte),
    path('iniciar-login/', views.iniciarLogin),
    path('salir',views.logout),
    path('tipos-incidencia/',views.tiposIncidencia),
    path('mostrar-reportes/',views.mostrarReportes),
    path('ayuda/',views.ayuda),
    path('ver-reporte/<int:id_reporte>', views.verReporte),
    path('ingresar-duda/',views.consultarDudar),
    path('ingresar-dudas/',views.ingresarDudas),
    path('ver-usuario/',views.verUsuario),
    path('mostrar-tablas-admin/',views.verTablasAdmins),
    path('mostrar-reportes-admin/',views.mostrarReportesAdmin),
    path('updatea-reporte/',views.updateaReporte),
]
