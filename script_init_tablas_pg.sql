-- script inicial

-- DROP DATABASE IF EXISTS "flask-restapi";

CREATE DATABASE "flask-restapi"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Argentina.1252'
    LC_CTYPE = 'Spanish_Argentina.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

create table tipo_usuario (cod_tipo INT,
						  nombre_tipo VARCHAR(30),
						  CONSTRAINT "pkCodTipo" PRIMARY KEY (cod_tipo),
						  UNIQUE (cod_tipo)
						  );

create table usuarios (id INT,
					   usuario VARCHAR(30),
					   clave VARCHAR(102),
					   t_usuario INT,
					   mail VARCHAR(99),
					   is_confirmed BOOLEAN,
					  CONSTRAINT "pkUsuario" PRIMARY KEY (id),
					  CONSTRAINT "fkTipoUsuario" FOREIGN KEY (t_usuario)
					  REFERENCES tipo_usuario (cod_tipo)
					  );
					  
create table pacientes (id INT,
						num_doc INT,
						nombre VARCHAR(99),
						apellido VARCHAR(99),
						genero VARCHAR(10) CHECK (genero IN ('masculino', 'femenino')),
						mail VARCHAR(99),
						telefono VARCHAR(99),
						domicilio VARCHAR(99),
						CONSTRAINT "pkPaciente" PRIMARY KEY (id, num_doc)
						);

create table medicos	(id INT,
					  	num_doc INT,
						nombre VARCHAR(99),
						apellido VARCHAR(99),
						genero VARCHAR(10) CHECK (genero IN ('masculino', 'femenino')),
						legajo VARCHAR(4),
						mail VARCHAR(99),
						telefono VARCHAR(99),
						domicilio VARCHAR(99),
						CONSTRAINT "pkDoctor" PRIMARY KEY (id, num_doc)
						);

INSERT INTO public.tipo_usuario(
	cod_tipo, nombre_tipo)
	VALUES (1, 'Paciente');
	
INSERT INTO public.tipo_usuario(
	cod_tipo, nombre_tipo)
	VALUES (2, 'Medico');
	
INSERT INTO public.tipo_usuario(
	cod_tipo, nombre_tipo)
	VALUES (3, 'Admin');
			   
INSERT INTO public.usuarios(
	id, usuario, clave, t_usuario, mail, is_confirmed)
	VALUES (1, 'Admin', 'pbkdf2:sha256:600000$dhAuQeZ7LCMsIeao$42e0eb7e04daedf3f944375ae162891d8af3f7c64440d3f07290495d035b0347', 3, 'admin@admin.com', True);
	
-- Insert para el Dr. Smith
INSERT INTO medicos (id, num_doc, nombre, apellido, genero, legajo, mail, telefono, domicilio)
VALUES (1, 123456, 'John', 'Smith', 'masculino', 'L001', 'dr.smith@johndoe.com', '123-456-7890', 'Dirección 123');

INSERT INTO public.usuarios (id, usuario, clave, t_usuario, mail, is_confirmed)
VALUES (2, 'DrSmith', 'pbkdf2:sha256:600000$3Nf2NYK9sG8csIPV$ebeec16c450a1d7f8e9bbc61fcd4fb9318b881e1133f431f4f25bb3685b7132b', 2, 'dr.smith@johndoe.com', True);

-- Insert para el Dr. Johnson
INSERT INTO medicos (id, num_doc, nombre, apellido, genero, legajo, mail, telefono, domicilio)
VALUES (2, 789012, 'Robert', 'Johnson', 'masculino', 'L002', 'dr.johnson@johndoe.com', '987-654-3210', 'Otra Dirección 456');

INSERT INTO public.usuarios (id, usuario, clave, t_usuario, mail, is_confirmed)
VALUES (3, 'DrJohnson', 'pbkdf2:sha256:600000$X4geqNidLMrSsAPM$ef7a6121bbb0af97a3b769763777263916cc1a6e6da9e326ad9457b89bca50e3', 2, 'dr.johnson@johndoe.com', True);

-- Insert para el Dr. Anderson
INSERT INTO medicos (id, num_doc, nombre, apellido, genero, legajo, mail, telefono, domicilio)
VALUES (3, 345678, 'Michael', 'Anderson', 'femenino', 'L003', 'dra.anderson@johndoe.com', '555-123-4567', 'Calle Principal 789');

INSERT INTO public.usuarios (id, usuario, clave, t_usuario, mail, is_confirmed)
VALUES (4, 'DraAnderson', 'pbkdf2:sha256:600000$Boi0Lhmf2mG5uOgS$0596edb307f386607494cf755b746a7a494581563d5748378f474115b905d99a', 2, 'dr.anderson@johndoe.com', True);

-- Funcion del registro de usuarios

CREATE OR REPLACE FUNCTION registro_usuario()
RETURNS TRIGGER AS $$
BEGIN
	IF NEW.t_usuario = 1 THEN
		INSERT INTO pacientes(id,num_doc,nombre,apellido,mail,telefono,domicilio)
		VALUES (NEW.id, CAST(NEW.usuario AS INT), '','',NEW.mail,'','');
		
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Crear Trigger que activa la funcion
CREATE TRIGGER usuario_registrado AFTER INSERT ON usuarios FOR EACH ROW EXECUTE FUNCTION registro_usuario();
