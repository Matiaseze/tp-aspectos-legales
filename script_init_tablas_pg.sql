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

create table pacientes (dni INT,
						nombre VARCHAR(99),
						descripcion VARCHAR(99),
						medico_actual INT,
						CONSTRAINT "pkPaciente" PRIMARY KEY (dni),
						CONSTRAINT "fkMedicoActual" FOREIGN KEY (medico_actual)
						REFERENCES usuarios (id_usuario));

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
