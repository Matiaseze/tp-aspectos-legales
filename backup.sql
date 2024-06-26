PGDMP         ,                {            flask-restapi    13.11    13.11     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16932    flask-restapi    DATABASE     o   CREATE DATABASE "flask-restapi" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Spanish_Argentina.1252';
    DROP DATABASE "flask-restapi";
                postgres    false            �            1255    17046    registro_usuario()    FUNCTION     +  CREATE FUNCTION public.registro_usuario() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
	IF NEW.t_usuario = 1 THEN
		INSERT INTO pacientes(id,num_doc,nombre,apellido,mail,telefono,domicilio)
		VALUES (NEW.id, CAST(NEW.usuario AS INT), '','',NEW.mail,'','');
		
	END IF;
	RETURN NEW;
END;
$$;
 )   DROP FUNCTION public.registro_usuario();
       public          postgres    false            �            1259    17037    medicos    TABLE     �  CREATE TABLE public.medicos (
    id integer NOT NULL,
    num_doc integer NOT NULL,
    nombre character varying(99),
    apellido character varying(99),
    genero character varying(10),
    legajo character varying(4),
    mail character varying(99),
    telefono character varying(99),
    domicilio character varying(99),
    CONSTRAINT medicos_genero_check CHECK (((genero)::text = ANY ((ARRAY['masculino'::character varying, 'femenino'::character varying])::text[])))
);
    DROP TABLE public.medicos;
       public         heap    postgres    false            �            1259    17028 	   pacientes    TABLE     �  CREATE TABLE public.pacientes (
    id integer NOT NULL,
    num_doc integer NOT NULL,
    nombre character varying(99),
    apellido character varying(99),
    genero character varying(10),
    mail character varying(99),
    telefono character varying(99),
    domicilio character varying(99),
    CONSTRAINT pacientes_genero_check CHECK (((genero)::text = ANY ((ARRAY['masculino'::character varying, 'femenino'::character varying])::text[])))
);
    DROP TABLE public.pacientes;
       public         heap    postgres    false            �            1259    17013    tipo_usuario    TABLE     k   CREATE TABLE public.tipo_usuario (
    cod_tipo integer NOT NULL,
    nombre_tipo character varying(30)
);
     DROP TABLE public.tipo_usuario;
       public         heap    postgres    false            �            1259    17018    usuarios    TABLE     �   CREATE TABLE public.usuarios (
    id integer NOT NULL,
    usuario character varying(30),
    clave character varying(102),
    t_usuario integer,
    mail character varying(99),
    is_confirmed boolean
);
    DROP TABLE public.usuarios;
       public         heap    postgres    false            �          0    17037    medicos 
   TABLE DATA           k   COPY public.medicos (id, num_doc, nombre, apellido, genero, legajo, mail, telefono, domicilio) FROM stdin;
    public          postgres    false    203   �       �          0    17028 	   pacientes 
   TABLE DATA           e   COPY public.pacientes (id, num_doc, nombre, apellido, genero, mail, telefono, domicilio) FROM stdin;
    public          postgres    false    202   �       �          0    17013    tipo_usuario 
   TABLE DATA           =   COPY public.tipo_usuario (cod_tipo, nombre_tipo) FROM stdin;
    public          postgres    false    200   �       �          0    17018    usuarios 
   TABLE DATA           U   COPY public.usuarios (id, usuario, clave, t_usuario, mail, is_confirmed) FROM stdin;
    public          postgres    false    201   �       2           2606    17017    tipo_usuario pkCodTipo 
   CONSTRAINT     \   ALTER TABLE ONLY public.tipo_usuario
    ADD CONSTRAINT "pkCodTipo" PRIMARY KEY (cod_tipo);
 B   ALTER TABLE ONLY public.tipo_usuario DROP CONSTRAINT "pkCodTipo";
       public            postgres    false    200            8           2606    17045    medicos pkDoctor 
   CONSTRAINT     Y   ALTER TABLE ONLY public.medicos
    ADD CONSTRAINT "pkDoctor" PRIMARY KEY (id, num_doc);
 <   ALTER TABLE ONLY public.medicos DROP CONSTRAINT "pkDoctor";
       public            postgres    false    203    203            6           2606    17036    pacientes pkPaciente 
   CONSTRAINT     ]   ALTER TABLE ONLY public.pacientes
    ADD CONSTRAINT "pkPaciente" PRIMARY KEY (id, num_doc);
 @   ALTER TABLE ONLY public.pacientes DROP CONSTRAINT "pkPaciente";
       public            postgres    false    202    202            4           2606    17022    usuarios pkUsuario 
   CONSTRAINT     R   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT "pkUsuario" PRIMARY KEY (id);
 >   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT "pkUsuario";
       public            postgres    false    201            :           2620    17047    usuarios usuario_registrado    TRIGGER     {   CREATE TRIGGER usuario_registrado AFTER INSERT ON public.usuarios FOR EACH ROW EXECUTE FUNCTION public.registro_usuario();
 4   DROP TRIGGER usuario_registrado ON public.usuarios;
       public          postgres    false    201    204            9           2606    17023    usuarios fkTipoUsuario    FK CONSTRAINT     �   ALTER TABLE ONLY public.usuarios
    ADD CONSTRAINT "fkTipoUsuario" FOREIGN KEY (t_usuario) REFERENCES public.tipo_usuario(cod_tipo);
 B   ALTER TABLE ONLY public.usuarios DROP CONSTRAINT "fkTipoUsuario";
       public          postgres    false    201    200    2866            �   �   x�U�K� ��?�� @K;���F�[7H1��`h=�G�b�va���f0�����\3u0�Q=�q��2h���c���(?��5\���	Z)�~�,�CR����0}ѣwK.O���,�M]�R8��q
2���I�C:\�p0����ڵ:������y�K"gk� ����
6�Z���q�<���ut%���U�      �      x������ � �      �   )   x�3�HL�L�+I�2��MM�L��2�tL�������� �s�      �   _  x�uбn1���7�H�R�8-������B�T��k}���\g
���H߭t8���K[���b�J�\��W/_�'�?l�;��`΄̡�i�V�"�O!���Մ�N�9
�a�� ��:>�]���:��"tO����?�-l|.�m������Ĭ�T1:�J-[�ɷ�ؤ�ϒ�7��o�B����� ]����Ή�O�����J`�|�7���C����t�9������F�|�"�bJ�QHPff��,)��XF�\�rt��%�g��j�w=7����C�m|���],�T�Q���#,X��tLL<�1��@#a�	��R\�R�����7���b����9     