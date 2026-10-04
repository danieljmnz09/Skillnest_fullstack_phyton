CREATE DATABASE IF NOT EXISTS esquema_educacion;
USE esquema_educacion;

CREATE TABLE IF NOT EXISTS estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cursos (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre_curso VARCHAR(100) NOT NULL,
    descripcion TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS inscripciones (
    estudiante_id INT NOT NULL,
    curso_id INT NOT NULL,
    PRIMARY KEY (estudiante_id, curso_id),
    CONSTRAINT fk_estudiantes
        FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id_estudiante)
        ON DELETE CASCADE,
    CONSTRAINT fk_cursos
        FOREIGN KEY (curso_id) REFERENCES cursos(id_curso)
        ON DELETE CASCADE
);

-- Datos iniciales de prueba
INSERT INTO estudiantes (nombre, email) VALUES 
('Ana Gómez', 'ana@email.com'),
('Carlos Ruiz', 'carlos@email.com');

INSERT INTO cursos (nombre_curso, descripcion) VALUES 
('Python y Flask', 'Curso de desarrollo web con Flask'),
('Bases de Datos MySQL', 'Modelado y consultas SQL');