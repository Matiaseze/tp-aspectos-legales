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
						
INSERT INTO public.usuarios(
	id_usuario, nombre, clave, t_usuario, mail)
	VALUES (1, 'matias', 'clave', null, null);
					   
