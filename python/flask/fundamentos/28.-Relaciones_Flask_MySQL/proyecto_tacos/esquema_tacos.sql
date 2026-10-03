-- ==========================================================
-- CREAR BASE DE DATOS Y TABLAS
-- ==========================================================

CREATE DATABASE IF NOT EXISTS esquema_tacos;
USE esquema_tacos;

-- TABLA RESTAURANTES
CREATE TABLE IF NOT EXISTS restaurantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- TABLA TACOS
CREATE TABLE IF NOT EXISTS tacos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tortilla VARCHAR(45),
    guiso VARCHAR(45),
    salsa VARCHAR(45),
    restaurante_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_tacos_restaurantes
        FOREIGN KEY (restaurante_id)
        REFERENCES restaurantes(id)
        ON DELETE CASCADE
);

-- TABLA COMPLEMENTOS
CREATE TABLE IF NOT EXISTS complementos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_complemento VARCHAR(45) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- TABLA INTERMEDIA (MUCHOS A MUCHOS)
CREATE TABLE IF NOT EXISTS complementos_en_tacos (
    complemento_id INT NOT NULL,
    taco_id INT NOT NULL,
    PRIMARY KEY (complemento_id, taco_id),
    CONSTRAINT fk_ct_complementos
        FOREIGN KEY (complemento_id)
        REFERENCES complementos(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_ct_tacos
        FOREIGN KEY (taco_id)
        REFERENCES tacos(id)
        ON DELETE CASCADE
);

-- DATOS DE PRUEBA
INSERT INTO restaurantes (nombre) VALUES 
('Tacos El Sol'), 
('Tacos Central'), 
('Tacos Don Pepe');

INSERT INTO tacos (tortilla, guiso, salsa, restaurante_id) VALUES 
('Maíz', 'Carne', 'Verde', 1),
('Harina', 'Pollo', 'Roja', 1),
('Maíz', 'Carnitas', 'Verde', 2);

INSERT INTO complementos (nombre_complemento) VALUES 
('Queso Extra'), 
('Guacamole'), 
('Cebollitas Cambray');