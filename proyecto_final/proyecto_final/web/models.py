from django.db import models
import datetime

# Create your models here.


class Usuario(models.Model):
    id_usuario=models.AutoField(primary_key=True)
    nombre_usuario=models.CharField(max_length=40,null=False)
    primer_apellido=models.CharField(max_length=40,null=False)
    segundo_apellido=models.CharField(max_length=40,null=True)
    fecha_nac=models.DateField(null=False)
    correo_electronico=models.CharField(max_length=40,null=False,unique=True)
    password=models.CharField(max_length=40,null=False)
    numero_telefono=models.CharField(max_length=10,null=False)
    rol=models.CharField(max_length=40, default="usuario")


class CatalogoIncidencia(models.Model):
    clave_incidencia=models.CharField(max_length=5,primary_key=True,null=False,unique=True)
    incidencia=models.CharField(max_length=60,unique=False,null=False)


class ReporteDeIncidencia(models.Model):
    id_reporte=models.AutoField(primary_key=True)
    clave_de_incidencia=models.ForeignKey(CatalogoIncidencia, on_delete=models.CASCADE)
    id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_incidencia=models.CharField(max_length=60,null=False)
    calle_principal=models.CharField(max_length=40,null=False)
    calle_secundaria=models.CharField(max_length=40,null=True)
    fecha_de_reporte=models.DateField(null=False)
    descripcion=models.TextField(null=True)
    estatus=models.CharField(max_length=15,default='Enviado',null=False)


class TicketDeIncidencia(models.Model):
    id_ticket=models.AutoField(primary_key=True)
    id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_usuario=models.CharField(max_length=60)
    comentario=models.TextField(null=False)
    fecha_hora=models.DateTimeField(null=True)


class TokenUsuario(models.Model):
    id_usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    token=models.CharField(max_length=100)



