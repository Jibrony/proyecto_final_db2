/*
UNIVERSIDAD AUTÓNOMA DE BAJA CALIFORNIA SUR
DEPARTAMENTO ACÁDEMICO DE SISTEMAS COMPUTACIONALES
ING. DESARROLLO DE SOFTWARE
BASE DE DATOS II
ZUÑIGA ARCE JESÚS ANTONIO
AYON CAMACHO NEDEL ENRIQUE
CARBALLO CABALLERO JESUS ALBERTO
GUTIERREZ ARCE ANDREY JULIAN
IGNACIO SANCHEZ ZULIDANY
PROYECTO FINAL
*/

create database proyecto_final;
use proyecto_final;
-- drop database proyecto;

insert into web_catalogoincidencia (clave_incidencia, incidencia)values("CIBA1","baches");
insert into web_catalogoincidencia (clave_incidencia, incidencia)values("CIPA","Problemas de alumbrado");
insert into web_catalogoincidencia (clave_incidencia, incidencia)values("CIFA1","fuga de alcantarilla");
insert into web_catalogoincidencia (clave_incidencia, incidencia)values("CIPB1","basura en via publica");
select * from web_catalogoincidencia;

-- drop trigger if exists T_SEGUNDOAP_NULL;
delimiter $$
	CREATE TRIGGER T_SEGUNDOAP_NULL
    before INSERT ON web_usuario
    FOR EACH ROW
    BEGIN
    declare nulo varchar(10) default null;
	if new.segundo_apellido is null or new.segundo_apellido ="" then
		begin 
			set new.segundo_apellido=nulo;
		end;
    end if;
    
    END $$
delimiter ;

-- drop trigger if exists T_fechas_now_reporte_de_incidencia;
delimiter $$
	CREATE TRIGGER T_fechas_now_reporte_de_incidencia
    before INSERT ON web_reportedeincidencia
    FOR EACH ROW
    BEGIN
	if new.fecha_de_reporte is null  then
		begin 
			set new.fecha_de_reporte=now();
		end;
    end if;
    if new.calle_secundaria is null or new.calle_secundaria="" then
		begin 
			set new.calle_secundaria=null;
        end;
    end if;
    if new.descripcion is null or new.descripcion="" then
		begin 
			set new.descripcion="sin descripciÃ³n";
        end;
    end if;
    
    
    END $$
delimiter ;

-- drop trigger if exists T_fechas_hora_now_ticket_incidencia;

delimiter $$
	CREATE TRIGGER T_fechas_hora_now_ticket_incidencia
    before INSERT ON web_ticketdeincidencia
    FOR EACH ROW
    BEGIN
	if new.fecha_hora is null then
		begin 
			set new.fecha_hora=now();
		end;
    end if;
    
    END $$
delimiter ;
-- drop procedure if exists  Crear_reporte;
Delimiter //
create procedure Crear_reporte( in clave_incidencia char(5),nombre_incidencia varchar(50), calle_principal varchar(40), calle_secundaria varchar(40),fecha_de_reporte date,descripcion text)
begin 
    if (fecha_de_reporte>now())then
        begin 
        SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'la fecha no cuadra';
        end;
        else
            begin 
            insert into reporte_de_incidencia(clave_incidencia,nombre_incidencia,calle_principal,calle_secundaria,fecha_de_reporte,descripcion) 
            values(clave_incidencia,nombre_incidencia,calle_principal,calle_secundaria,fecha_de_reporte,descripcion);
            end;
    end if;

end //
delimiter ;
-- drop procedure if exists  Crear_usuario;
Delimiter //
create procedure Crear_usuario(in nombre_usuario varchar (40), primer_apellido varchar(40), segundo_apellido varchar (40), fecha_nacimiento date,correo_electronico varchar (50),contra varchar (16),no_telefono char(10) )
begin 
if (fecha_nacimiento>now())then
    begin 
    SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'la fecha no cuadra';
    end;
    else
    begin
    if (year(now())-(year(fecha_nacimiento))) < 18 then
        SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'menor de edad';
    else
        begin 
        insert into usuario(nombre_usuario,primer_apellido,segundo_apellido,fecha_nacimiento,correo_electronico,contra,no_telefono) 
        values(nombre_usuario,primer_apellido,segundo_apellido,fecha_nacimiento,correo_electronico,contra,no_telefono);
        end;
    end if;
    end;
end if;


end //
delimiter ;