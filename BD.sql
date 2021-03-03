CREATE DATABASE IF NOT EXISTS app_consola;
use app_consola;

CREATE TABLE usuarios(
    id_user int(25) auto_increment not null,
    nombre_user varchar(100),
    apellido_user varchar(255),
    email_user varchar(150) not null,
    password_user varchar(255) not null,
    fecha_registro_user date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id_user),
    CONSTRAINT uq_email UNIQUE(email_user)
)ENGINE=InnoDB;

CREATE TABLE notas(
    id_notas int(25) auto_increment not null,
    usuario_id int(25) not null,
    titulo_notas varchar(150) not null,
    descripcion_notas MEDIUMTEXT,
    fecha_registro_notas date not null,
    CONSTRAINT pk_notas PRIMARY KEY(id_notas),
    CONSTRAINT fk_usuario_id FOREIGN KEY (usuario_id) REFERENCES usuarios(id_user)
)ENGINE=InnoDB;