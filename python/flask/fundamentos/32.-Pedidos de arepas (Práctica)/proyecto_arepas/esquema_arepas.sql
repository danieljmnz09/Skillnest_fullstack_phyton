CREATE DATABASE IF NOT EXISTS esquema_arepas DEFAULT CHARACTER SET utf8mb4;
USE esquema_arepas;

CREATE TABLE IF NOT EXISTS pedidos (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(255) NOT NULL,
  relleno VARCHAR(255) NOT NULL,
  cantidad INT NOT NULL,
  created_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Datos iniciales opcionales de prueba
INSERT INTO pedidos (nombre, relleno, cantidad) VALUES 
('Carlos Gómez', 'Reina Pepiada', 3),
('María López', 'Pabellón', 2);
