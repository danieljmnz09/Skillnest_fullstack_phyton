CREATE DATABASE IF NOT EXISTS esquema_usuarioss;
USE esquema_usuarioss;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    email VARCHAR(45) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO usuarios (nombre, apellido, email) VALUES
("Daniel", "Jimenez", "daniel@codingdojo.com"),
("Enrique", "Iglesias", "enrique@codingdojo.com"),
("Marcelo", "Cruz", "Marcelo@codingdojo.com"),
("Ricardo", "Montaner", "ricardo@codingdojo.com");