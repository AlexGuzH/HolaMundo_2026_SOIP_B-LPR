graph TD
    subgraph Capa1 [CAPA 1: DISPOSITIVO EDGE - Raspberry Pi 5 / Mac]
        A[Sensor de Video / WebCam<br>640x480 @ 30 FPS] --> B[Segmentación Espacial<br>YOLOv8 Nano]
        B --> C{¿Caja de Placa<br>Detectada?}
        C -- No --> A
        C -- Sí --> D[Algoritmo de Control<br>Distancia Euclidiana]
        D --> E{¿Cambio de Posición<br>ó Frame % 30 == 0?}
        E -- No --> F[Servir Texto de<br>Placa en Caché]
        E -- Sí --> G[Motor CRNN<br>EasyOCR]
        G --> H[Bifurcación en Segundo Plano<br>Python Threading]
        F --> H
    end

    subgraph Capa2 [CAPA 2: SERVIDOR BACKEND - Cloud Hosting]
        H -->|Request HTTP POST JSON| I[Endpoint Receptor PHP<br>api2.php / api_paralela.php]
        I --> J[Limpieza de Cadena<br>Sanitización RegEx]
        J --> K{¿Coincide con<br>Patrones de Estado?}
        K -->|SELECT| L[(Base de Datos MySQL<br>minimal1_yoloproject)]
        L -->|Cotejo de Existencia| M{¿Registrado en<br>catalogo_robos?}
        M -->|INSERT tabla lecturas<br>es_robo = 0 ó 1| L
    end

    subgraph Capa3 [CAPA 3: INTERFAZ CLIENTE - Navegador]
        N[Alerts4.html] -->|Petición Cronometrada<br>Fetch API cada 3s| O[Agregador de Datos<br>fetch_dashboard.php]
        O -->|SELECT Contadores y Tablas| L
        L -->|Response JSON Sincronizado| O
        O -->|Cache-Busting Variable| N
        N --> P{¿Existe registro con<br>es_robo == 1?}
        P -- Sí --> Q[🚨 DETONAR ALERTA ROJA<br>Banderazo Global]
        P -- No --> R[✅ Renderizar Fila Normal<br>Estatus OK]
    end

    %% Estilos de las Capas para visualización en GitHub (Modo Oscuro / Claro)
    style Capa1 fill:#1a252f,stroke:#2c3e50,stroke-width:2px,color:#fff
    style Capa2 fill:#114b43,stroke:#16a085,stroke-width:2px,color:#fff
    style Capa3 fill:#5b2c22,stroke:#e74c3c,stroke-width:2px,color:#fff
    
    %% Estilos de bloques críticos
    style Q fill:#e74c3c,stroke:#c0392b,stroke-width:2px,color:#fff
    style L fill:#2980b9,stroke:#1f618d,stroke-width:2px,color:#fff
    style R fill:#27ae60,stroke:#1e8449,stroke-width:2px,color:#fff
