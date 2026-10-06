CREATE DATABASE IF NOT EXISTS esquema_seguidores DEFAULT CHARACTER SET utf8mb4;
USE esquema_seguidores;

CREATE TABLE IF NOT EXISTS usuarios (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(255) NOT NULL,
  apellido VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  created_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS seguidores (
  usuario_id INT NOT NULL,
  seguidor_id INT NOT NULL,
  created_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (usuario_id, seguidor_id),
  CONSTRAINT fk_usuarios_has_seguidores_usuario
    FOREIGN KEY (usuario_id) REFERENCES usuarios (id) ON DELETE CASCADE,
  CONSTRAINT fk_usuarios_has_seguidores_seguidor
    FOREIGN KEY (seguidor_id) REFERENCES usuarios (id) ON DELETE CASCADE
);