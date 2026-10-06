CREATE DATABASE IF NOT EXISTS esquema_tasktrack DEFAULT CHARACTER SET utf8mb4;
USE esquema_tasktrack;

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  apellido VARCHAR(100) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  created_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Tabla de categorías relacionadas al usuario
CREATE TABLE IF NOT EXISTS categorias (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  usuario_id INT NOT NULL,
  created_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  CONSTRAINT fk_categorias_usuarios
    FOREIGN KEY (usuario_id) REFERENCES usuarios (id) ON DELETE CASCADE
);

-- Tabla de tareas asociadas a usuario y categoría
CREATE TABLE IF NOT EXISTS tareas (
  id INT NOT NULL AUTO_INCREMENT,
  titulo VARCHAR(255) NOT NULL,
  descripcion TEXT NULL,
  prioridad ENUM('Alta', 'Media', 'Baja') NOT NULL DEFAULT 'Media',
  estado ENUM('Pendiente', 'En progreso', 'Completada') NOT NULL DEFAULT 'Pendiente',
  fecha_limite DATE NOT NULL,
  usuario_id INT NOT NULL,
  categoria_id INT NOT NULL,
  created_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  CONSTRAINT fk_tareas_usuarios
    FOREIGN KEY (usuario_id) REFERENCES usuarios (id) ON DELETE CASCADE,
  CONSTRAINT fk_tareas_categorias
    FOREIGN KEY (categoria_id) REFERENCES categorias (id) ON DELETE CASCADE
);