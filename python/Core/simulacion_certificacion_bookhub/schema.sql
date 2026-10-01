CREATE DATABASE IF NOT EXISTS bookhub
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
USE bookhub;

CREATE TABLE IF NOT EXISTS users (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    surname VARCHAR(60) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS books (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(160) NOT NULL,
    author VARCHAR(120) NOT NULL,
    genre VARCHAR(60) NOT NULL,
    published_on DATE NOT NULL,
    description TEXT NOT NULL,
    user_id INT UNSIGNED NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_books_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_books_user (user_id),
    INDEX idx_books_title (title)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS favorites (
    user_id INT UNSIGNED NOT NULL,
    book_id INT UNSIGNED NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, book_id),
    CONSTRAINT fk_favorites_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_favorites_book FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE,
    INDEX idx_favorites_book (book_id)
) ENGINE=InnoDB;
