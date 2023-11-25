-- script inicial

create table tipo_usuario (cod_tipo INT,
						  nombre_tipo VARCHAR(30),
						  CONSTRAINT "pkCodTipo" PRIMARY KEY (cod_tipo),
						  UNIQUE (cod_tipo)
						  );

create table usuarios (id INT,
					   usuario VARCHAR(30),
					   clave VARCHAR(50),
					   t_usuario INT,
					   mail VARCHAR(99),
					  CONSTRAINT "pkUsuario" PRIMARY KEY (id_usuario),
					  CONSTRAINT "fkTipoUsuario" FOREIGN KEY (t_usuario)
					  REFERENCES tipo_usuario (cod_tipo)
					  );

create table pacientes (num_doc INT,
						nombre VARCHAR(99),
						apellido VARCHAR(99),
						mail VARCHAR(99),
						telefono VARCHAR(99),
						domicilio VARCHAR(99),
						CONSTRAINT "pkPaciente" PRIMARY KEY (num_doc)
						);

create table medicos (num_doc INT,
						nombre VARCHAR(99),
						apellido VARCHAR(99),
						legajo VARCHAR(4),
						mail VARCHAR(99),
						telefono VARCHAR(99),
						domicilio VARCHAR(99),
						CONSTRAINT "pkDoctor" PRIMARY KEY (num_doc)
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
	id, nombre, clave, t_usuario, mail)
	VALUES (1, 'Admin', 'pbkdf2:sha256:600000$dhAuQeZ7LCMsIeao$42e0eb7e04daedf3f944375ae162891d8af3f7c64440d3f07290495d035b0347', 3, 'admin@admin.com');
	


-- Doctor 1
INSERT INTO public.usuarios (id, nombre, clave, t_usuario, mail)
VALUES (2, 'DrSmith', 'pbkdf2:sha256:600000$3Nf2NYK9sG8csIPV$ebeec16c450a1d7f8e9bbc61fcd4fb9318b881e1133f431f4f25bb3685b7132b', 2, 'dr.smith@johndoe.com');

-- Doctor 2
INSERT INTO public.usuarios (id, nombre, clave, t_usuario, mail)
VALUES (3, 'DrJohnson', 'pbkdf2:sha256:600000$X4geqNidLMrSsAPM$ef7a6121bbb0af97a3b769763777263916cc1a6e6da9e326ad9457b89bca50e3', 2, 'dr.johnson@johndoe.com');

-- Doctor 3
INSERT INTO public.usuarios (id, nombre, clave, t_usuario, mail)
VALUES (4, 'DrAnderson', 'pbkdf2:sha256:600000$Boi0Lhmf2mG5uOgS$0596edb307f386607494cf755b746a7a494581563d5748378f474115b905d99a', 2, 'dr.anderson@johndoe.com');
	
-- Funcion del registro de usuarios

CREATE OR REPLACE FUNCTION registro_usuario()
RETURNS TRIGGER AS $$
BEGIN
	IF NEW.t_usuario = 1 THEN
		INSERT INTO pacientes(num_doc,nombre,apellido,mail,telefono,domicilio)
		VALUES (CAST(NEW.usuario AS INT), '','',NEW.mail,'','');
		
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Crear Trigger que activa la funcion
CREATE TRIGGER usuario_registrado AFTER INSERT ON usuarios FOR EACH ROW EXECUTE FUNCTION registro_usuario();

select * from usuarios
