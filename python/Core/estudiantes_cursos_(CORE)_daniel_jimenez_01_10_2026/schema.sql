-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS esquema_estudiantes_cursos;

-- Seleccionar la base de datos para trabajar sobre ella
USE esquema_estudiantes_cursos;

-- Crear la tabla 'cursos'
CREATE TABLE IF NOT EXISTS cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Crear la tabla 'estudiantes' con clave foránea relacionada a 'cursos'
CREATE TABLE IF NOT EXISTS estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    edad INT NOT NULL,
    curso_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    -- Si se elimina un curso, se borran sus estudiantes asociados
    FOREIGN KEY (curso_id) REFERENCES cursos(id) ON DELETE CASCADE
);