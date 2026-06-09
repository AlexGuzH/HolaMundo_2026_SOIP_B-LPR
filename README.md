# 🚀 HolaMundo_2026_SOIP_B-LPR
Este proyecto consiste en un sistema de vanguardia para el Reconocimiento Automático de Placas Vehiculares (ALPR / LPR) diseñado bajo el paradigma de Edge AI (Inteligencia Artificial en el Borde). El núcleo del ecosistema está optimizado para ejecutarse en hardware embebido de bajo consumo, logrando un procesamiento fluido de video en tiempo real sin depender de costosos clústeres en la nube o GPUs de escritorio.
El pipeline divide la tarea de visión artificial en dos etapas optimizadas: 
* ETAPA 1: La localización geométrica milimétrica de la matrícula utilizando un modelo personalizado de YOLOv8
* ETAPA 2: La posterior extracción tipográfica mediante el motor de redes recurrentes de EasyOCR.

Los datos resultantes se validan sintácticamente y se transmiten mediante hilos asíncronos en formato JSON hacia un backend remoto en PHP, el cual realiza un cotejo instantáneo contra una base de datos MySQL de vehículos bajo reporte de robo, detonando alertas de alta prioridad en un Dashboard web interactivo.

# 🏆 Detalles del Concurso Competencia: HOLA MUNDO 2026
## CATEGORIA B-LPR
### Nombre del Equipo: SOIP

# 📍 Tabla de Contenidos
* Requisitos del Sistema
* Instalación Paso a Paso
* Configuración del Entorno
* Descarga de Datasets y Modelos
* Ejecución del Sistema
* Pruebas y Demostración de Endpoints
* Pruebas Automatizadas
* Estructura del Proyecto
* Tecnologías Utilizadas
* Métricas de Rendimiento
* Limitaciones Conocidas
* Créditos y Licencia

# 📋 Requisitos del Sistema
#### Hardware Mínimo y Recomendado
| Componente | Requisito Mínimo (Prototipo) | Requisito Recomendado (Despliegue Edge) | 
|--|--|--|
| Dispositivo | MacBook Air o PC de Escritorio | GPU gama media o superior | 
| Procesador | Intel Core i5 / Apple Silicon M1 | Apple Silicon SERIES M o GPU Nvidia | 
| Cámara | WebCam USB Estándar (720p)   Módulo de Cámara Oficial Pi o WebCam USB | 
| GPU / NPU | Integrada (Intel HD / Apple MPS) | CPU Nativo / Compatible con Raspberry Pi AI o NPU del mercado | 

## Entorno de Ejecución (Runtime)
* Python: Versión 3.9 o 3.10 (Estricto para evitar incompatibilidades de PyTorch en arquitecturas ARM).
* PHP: Versión 8.x habilitado con extensiones PDO para MySQL.
* Base de Datos: MySQL Server 8.0 o superior.

# 🛠️ Instalación Paso a Paso
Asumiendo un entorno completamente limpio en la máquina de destino, ejecuta los siguientes comandos según corresponda:

##### 1. Clonar el repositorio y preparar el sistema operativo
```Bash
# Clonar el proyecto
git clone https://github.com/[TU_USUARIO]/[NOMBRE_REPOSITORIO].git
cd [NOMBRE_REPOSITORIO]

# SOLO EN LINUX / RASPBERRY PI: Instalar librerías dinámicas esenciales de gráficos
sudo apt update && sudo apt install -y libgl1 libglib2.0-0
```

#### 2. Crear y activar el Entorno Virtual (PEP 668 Compliance)
```Bash
# Crear entorno aislado
python3 -m venv alpr_env

# Activar en macOS / Linux:
source alpr_env/bin/activate

# Activar en Windows (CMD):
alpr_env\Scripts\activate
```

#### 3. Instalar dependencias del ecosistema de IA
```Bash
# SOLO EN MACOS: Mitigación preventiva para arquitectura LibreSSL de Apple
pip install "urllib3<2"

# Instalar paquetes base (PyTorch y pesos se descargarán automáticamente)
pip install opencv-python ultralytics easyocr requests psutil
```

# ⚙️ Configuración del Entorno
Variables del Script de Python (alpr_pi.py / alpr_mac.py)
Abre el script correspondiente con tu editor de texto y localiza la sección de configuración global para ajustar los siguientes parámetros:
* ENDPOINT_PHP: URL pública u online del servidor donde se aloja tu archivo de recepción (Por defecto: "http://localhost/alpr/api2.php"). Cambia este valor por la IP o dominio real de tu hosting.
* frecuencia_ocr: Frecuencia de frames para invocar a EasyOCR. Ajustado por defecto en 30 (1 lectura por segundo a 30 FPS). Eleva a 45 en la Raspberry Pi si deseas reducir la carga térmica de la CPU.

Configuración del Servidor PHP y Base de DatosEn la carpeta del servidor, abre los archivos api2.php y fetch_dashboard.php. Edita las primeras líneas relativas a la conexión 
```php
PDO:PHP$host = 'localhost';
$db   = 'minimal1_yoloproject';
$user = 'TU_USUARIO_DATABASE';
$pass = 'TU_CONTRASEÑA_DATABASE';
```

# 📦 Descarga de Datasets y Modelos
El modelo final fue entrenado utilizando el ecosistema de Roboflow mediante la unificación de tres conjuntos de datos (Climas adversos, entornos nocturnos de CCTV e imágenes móviles locales).
* Modelo Preentrenado (best.pt): Descarga el archivo de pesos finales generado tras las 100 épocas de entrenamiento en Google Colab. Coloca el archivo best.pt directamente en la raíz de este repositorio.
* Dataset de Respaldo: Si deseas replicar el entrenamiento, puedes descargar el paquete unificado en formato YOLOv8 exportándolo directamente desde la plataforma de Roboflow utilizando el archivo de configuración data.yaml provisto en este repositorio.

# 🚀 Ejecución del Sistema
Arranque del Pipeline de Visión Local (Edge)Asegúrate de tener tu entorno virtual activo y la cámara web conectada al equipo. Ejecuta el comando de inicio apuntando al binario local del entorno virtual para blindar la ejecución frente a permisos parásitos de usuario:
```Bash
# Ejecución estándar en macOS / Windows / Linux con WebCam USB:
./alpr_env/bin/python alpr_pi.py

# SOLO EN RASPBERRY PI si utilizas el módulo de cámara oficial por cable plano:
libcamerify ./alpr_env/bin/python alpr_pi.py
```

##### Acceso al Centro de Monitoreo (Dashboard)
* Asegúrate de que tus archivos de backend (api2.php y fetch_dashboard.php) estén corriendo bajo un servidor Apache/Nginx web activo con acceso a internet.
* Abre tu navegador e ingresa a la URL pública de tu interfaz: https://tu-dominio.com/dashboard_v2.html. El sistema actualizará las tablas de forma asíncrona cada 3 segundos.
# 🧪 Pruebas y Demostración de Endpoints
Endpoint Principal de Ingesta (api2.php)
* Método: POST
* Content-Type: application/json

Ejemplo de Petición (Payload enviado por Python):
```bash
JSON{
  "placa": "PYM-71-68"
}
```

Ejemplo de Respuesta de Éxito del Servidor:
```basj
JSON{
  "status": "success",
  "placa": "PYM7168",
  "alerta": 1,
  "estado": "Guanajuato"
}
```

###### 💡 Nota de diseño: El backend remueve automáticamente guiones y espacios especiales mediante expresiones regulares antes de procesar el cotejo de seguridad y la asignación del estado geográfico.

# 📋 Pruebas AutomatizadasPara validar que los componentes críticos de hardware e inteligencia artificial de tu máquina local responden correctamente antes de lanzar el pipeline de producción en red, ejecuta el script de pruebas unitarias locales:
```
Bash./alpr_env/bin/python test_alpr.py
```

¿Qué evalúa este script de prueba?
* Instanciación y carga de la arquitectura de pesos base de YOLOv8.
* Descarga y verificación de los diccionarios lingüísticos de EasyOCR en la memoria RAM.
* Conexión física y apertura del búfer de video de tu cámara web por el índice predeterminado (0).

# 📂 Estructura del Proyecto
```bash
Plaintext
├── [NOMBRE_REPOSITORIO]/
│   ├── alpr_mac.py           # Script optimizado para macOS utilizando aceleración gráfica MPS
│   ├── alpr_pi.py            # Script optimizado para producción en CPU ARM de Raspberry Pi 5
│   ├── test_alpr.py          # Script de pruebas automatizadas y diagnóstico de periféricos
│   ├── best.pt               # Pesos de la red neuronal convolucional entrenada (No subir a Git)
│   ├── .gitignore            # Exclusiones estrictas para evitar subir entornos virtuales y temporales
│   ├── backend/
│   │   ├── api2.php          # Webhook receptor JSON. Sanitiza caracteres y busca reportes de robo
│   │   └── fetch_dashboard.php # Agregador de datos indexados. Genera JSON con métricas y segmentación
│   └── frontend/
│       └── dashboard_v2.html # Interfaz Bento Box de monitoreo con refresco asíncronico anti-caché
```

# 🛠️ Tecnologías Utilizadas
* Python 3.9+: Lenguaje base para el pipeline de inteligencia artificial y control en el borde.
* YOLOv8 (Ultralytics): Red neuronal convolucional libre de anclajes para detección y segmentación de objetos.
* EasyOCR: Motor OCR profundo basado en CRNN (Capas Convolucionales + BiLSTM + Clasificador CTC).
* OpenCV: Biblioteca de visión artificial para la manipulación matricial de video e inyección de gráficos en el frame.
* PHP 8.x: Procesamiento síncrono en backend y capa de servicios REST API.
* MySQL: Motor de persistencia relacional indexado para control de datos históricos y catálogos de cotejo.
* HTML5 / CSS3 (Grid Bento Layout) / JavaScript (Fetch API): Capa de presentación visual reactiva.

# 📊 Métricas de Rendimiento
El entrenamiento del modelo maestro en la nube arrojó métricas estadísticas con un alto nivel de certeza frente al subconjunto de imágenes de validación en condiciones climáticas complejas:
* Precisión (Precision): 92.5% (Tasa mínima de falsos positivos en el aislamiento de la caja delimitadora).
* Sensibilidad (Recall): 89.1% (Eficacia del localizador para evitar omisiones de vehículos en movimiento).
* mAP@50 (Mean Average Precision): 91.4% (Área total bajo la curva de balance de fidelidad del modelo).

# 🧪 Pruebas Automatizadas y de Calidad de Software

El sistema cuenta con una suite completa de pruebas unitarias e integración que validan los flujos críticos del pipeline (sintaxis alfanumérica, algoritmos vectoriales de distancia y simulación de respuestas de la API REST) sin requerir hardware de cámara activo.

### Ejecución de las Pruebas

Asegúrate de tener el entorno virtual activo antes de arrancar los casos de prueba:

```bash
# 1. Activar el entorno virtual si no lo está
source alpr_env/bin/activate  # En macOS/Linux
.\alpr_env\Scripts\activate   # En Windows

# 2. Ejecutar la suite automatizada nativa
python -m unittest tests_alpr.py -v
```

# ⚠️ Limitaciones Conocidas
1.- Ausencia de Aceleración de Hardware en ARM: Al ejecutar YOLOv8 en modo CPU pura dentro de la Raspberry Pi 5, el procesador se ve sometido a un alto estrés térmico, requiriendo disipación activa obligatoria para evitar degradación de FPS.<br>
2.- Ambigüedad en Caracteres Similares: Bajo condiciones extremas de oscuridad o ángulos agudos, el motor OCR general puede confundir caracteres de morfología similar (como el número 0 con la letra O).<br>
3.- Latencia por HTTP Polling: El panel web consulta datos mediante un temporizador ciego cada 3 segundos, lo que introduce una ventana máxima de retraso de 2.9 segundos para reflejar una alerta en pantalla desde que el coche es capturado por la cámara.<br>

# 👥 Créditos y Licencia
### Miembros del Equipo: 
* FRANCISCO HUNAHPU SAHÁGUN GONZÁLEZ - Desarrollador Secundario - Líder de Equipo / Estudiante de Tecnologías de la Información.
* MANUEL ALEJANDRO GUZMÁN HERNANDEZ - Desarrollador Principal / Estudiante de Maestría en Tecnologías de la Información.

#### Ubicación del Desarrollo
Guanajuato, México.

# ⚠️ Licencia
Este proyecto se distribuye bajo la Licencia [INGRESA EL TIPO DE LICENCIA, EJ. MIT O LICENCIA ACADÉMICA PÚBLICA]. Consulta el archivo adjunto para más detalles.
