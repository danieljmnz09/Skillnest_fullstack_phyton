# ERD de BookHub

```mermaid
erDiagram
    USERS ||--o{ BOOKS : publica
    USERS ||--o{ FAVORITES : guarda
    BOOKS ||--o{ FAVORITES : recibe

    USERS {
        int id PK
        varchar name
        varchar surname
        varchar email UK
        varchar password_hash
        timestamp created_at
    }
    BOOKS {
        int id PK
        varchar title
        varchar author
        varchar genre
        date published_on
        text description
        int user_id FK
        timestamp created_at
    }
    FAVORITES {
        int user_id PK, FK
        int book_id PK, FK
        timestamp created_at
    }
```

`users` y `books` tienen una relación uno a muchos: cada libro pertenece a un usuario. `favorites` resuelve la relación muchos a muchos entre lectores y libros; su clave primaria compuesta impide duplicar favoritos. Las claves foráneas usan `ON DELETE CASCADE`.
