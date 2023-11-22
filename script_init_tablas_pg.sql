-- script inicial

create table tipo_usuario (cod_tipo INT,
						  nombre_tipo VARCHAR(30),
						  CONSTRAINT "pkCodTipo" PRIMARY KEY (cod_tipo),
						  UNIQUE (cod_tipo)
						  );

create table usuarios (id_usuario INT,
					   nombre VARCHAR(30),
					   clave VARCHAR(50),
					   t_usuario INT,
					   mail VARCHAR(99),
					  CONSTRAINT "pkUsuario" PRIMARY KEY (id_usuario),
					  CONSTRAINT "fkTipoUsuario" FOREIGN KEY (t_usuario)
					  REFERENCES tipo_usuario (cod_tipo)
					  );

create table pacientes ("numDoc" INT,
						nombre VARCHAR(99),
						apellido VARCHAR(99),
						mail VARCHAR(99),
						telefono VARCHAR(99),
						domicilio VARCHAR(99),
						CONSTRAINT "pkPaciente" PRIMARY KEY ("numDoc")
						);

INSERT INTO public.tipo_usuario(
	cod_tipo, nombre_tipo)
	VALUES (1, 'admin');
	
INSERT INTO public.tipo_usuario(
	cod_tipo, nombre_tipo)
	VALUES (2, 'doctor');
			   
INSERT INTO public.usuarios(
	id_usuario, nombre, clave, t_usuario, mail)
	VALUES (2, 'matiasb', 'clave', 1, 'matias@matias.com');
	
UPDATE public.usuarios
	SET t_usuario=2, mail='doctor@doctor.com'
	WHERE id_usuario = 1;
	
select * from usuarios
					   
SELECT id_usuario, nombre, clave, t_usuario, mail FROM usuarios ORDER BY id_usuario

-- Cambiar en usuarios id_usuario por id
UPDATE public.usuarios
	SET clave='pbkdf2:sha256:600000$wJ9ct2HBNXJs96dW$1cf364759b758475946299e88e70a075df153927935d58285563833302555254', mail='admin@admin.com'
	WHERE id_usuario=1;

-- Funcion del registro de usuarios

CREATE OR REPLACE FUNCTION registro_usuario()
RETURNS TRIGGER AS $$
BEGIN
	IF NEW.t_usuario = 1 THEN
		INSERT INTO pacientes("numDoc",nombre,apellido,mail,telefono,domicilio)
		VALUES (NEW.id, NEW.nombre, '',NEW.mail,'','');
		
	END IF;
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Crear Trigger que activa la funcion
CREATE TRIGGER usuario_registrado AFTER INSERT ON usuarios FOR EACH ROW EXECUTE FUNCTION registro_usuario();

Insert into tipo_usuario (cod_tipo,nombre_tipo) Values (1,'Paciente');

INSERT INTO public.usuarios(
	id, nombre, clave, t_usuario, mail)
	VALUES ('2','juan', 'pbkdf2:sha256:600000$wJ9ct2HBNXJs96dW$1cf364759b758475946299e88e70a075df153927935d58285563833302555254', 1, 'juan@juan.com' );