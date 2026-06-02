erDiagram
    catalogo_robos {
        int id PK
        varchar placa UK "Unique"
    }

    lecturas {
        int id PK
        varchar placa
        timestamp fecha_hora "DEFAULT current_timestamp()"
        tinyint es_robo "DEFAULT 0"
        varchar estado "DEFAULT 'Desconocido'"
    }

    datos {
        bigint id PK
        decimal valor "10,2"
    }

    %% Relación lógica controlada por la capa de software (PHP/API)
    lecturas }o--o| catalogo_robos : "coteja_existencia (Lógica)"
