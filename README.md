# 🚀 Real-Time ALPR System: Edge AI with YOLOv8 & EasyOCR

An advanced, high-fidelity **Automatic License Plate Recognition (ALPR / LPR)** system designed to operate under the **Edge AI** paradigm. This project achieves seamless 30 FPS video inference on a **Raspberry Pi 5** (CPU mode) by combining lightweight object detection, intelligent spatial filtering, and asynchronous multi-threaded data pipelines linked to a remote **PHP / MySQL** backend and live web dashboard.

---

## 🌟 Key Features

* **Edge AI Optimized:** Engineered specifically for resource-constrained hardware (Raspberry Pi 5 / macOS Apple Silicon) utilizing lightweight inference techniques.
* **Dual-Stage Deep Learning Pipeline:**
  * **Stage 1 (Detection):** Custom-trained **YOLOv8** nano model (`best.pt`) specialized in isolating vehicle license plates with sub-millisecond bounding box regression.
  * **Stage 2 (OCR):** Context-aware **EasyOCR** text extraction engine with restricted alphanumeric syntax (`allowlist`).
* **High-Performance Video Stabilization:** Implements conditional **Frame Skipping** and **Euclidean Distance Tracking** between frame centroid vectors to bypass redundant OCR calls and completely eliminate visual "ghosting".
* **Asynchronous Multi-Threaded Networking:** Leverages Python's `threading` library to offload JSON payload POST requests, ensuring zero frame-drop or video lagging due to network latency.
* **Live "Target of Interest" Dashboard:** Micro-backend architecture in **PHP 8.x** and **MySQL** that matches incoming plates against a high-priority "Hotlist" database in $\mathcal{O}(1)$ time complexity, pushing real-time CSS/JS blinking alerts to web operators.

---

## 🛠️ Architecture & Data Flow

1. **Ingestion:** Camera frames are ingested at a strictly balanced **640x480 pixels** resolution to optimize memory bus bandwidth.
2. **Inference:** YOLOv8 localizes the plate. If spatial movement exceeds a 150px threshold, an instant OCR cycle is triggered; otherwise, it operates on a standard 30-frame interval.
3. **Transmission:** Validated text strings (length bounded between 5 and 9 characters) are dispatched via non-blocking HTTP POST.
4. **Cotejo & Alerting:** The PHP webhook sanitizes inputs via Regular Expressions, logs entries, and alerts the web interface using dynamic *Cache-Busting* query markers.

---

## 📦 Repository Structure

```text
├── alpr_mac.py            # High-performance local prototype (Apple Silicon MPS support)
├── alpr_pi.py             # Production script configured for Raspberry Pi 5 ARM64 architecture
├── backend/
│   ├── api2.php           # REST Webhook for JSON ingestion, RegEx sanitization & DB logging
│   └── fetch.php          # Non-cached database reader with strict anti-cache HTTP headers
└── frontend/
    └── index.html         # Live monitoring dashboard with interactive visual theft alerts
```

# 🚀 Quick Start Guide
### 1. Backend & Database Setup
Import the following schema into your MySQL server:

```SQL
CREATE TABLE catalogo_robos (id INT AUTO_INCREMENT PRIMARY KEY, plate VARCHAR(15) NOT NULL UNIQUE);
CREATE TABLE lecturas (id INT AUTO_INCREMENT PRIMARY KEY, plate VARCHAR(15) NOT NULL, fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP, es_robo BOOLEAN DEFAULT FALSE);
```
2. Place api2.php and fetch.php inside your web hosting public directory and configure your database credentials.

### 2. Edge Device Installation (Raspberry Pi 5)
Ensure your system packages are updated and install vital graphic system dependencies:
```bash
sudo apt update && sudo apt install -y libgl1 libglib2.0-0
```
Set up a isolated Python Environment (PEP 668 compliance):

```bash
python3 -m venv alpr_env
source alpr_env/bin/activate
pip install opencv-python ultralytics easyocr requests
```

### 3. Execution
Change the ENDPOINT_PHP variable in alpr_pi.py to target your online server, and run the system:
```bash
# Force the system to use the local environment's explicit binary bin path
./alpr_env/bin/python alpr_pi.py
```

🗺️ Roadmap & Future Enhancements
[ ] Hardware Acceleration: Integrate the Raspberry Pi AI Kit (Hailo-8L NPU) via PCIe to run model inference completely off-CPU.

[ ] Real-Time Push: Upgrade the Frontend architecture from HTTP short polling to persistent WebSockets (Node.js/Ratchet) for instant (<50ms) server-push alerts.

[ ] Runtime Export: Compile the .pt weights into ONNX Runtime and Intel OpenVINO layouts to scale up raw FPS performance.


# 🔍 Solución de Problemas Comunes (Troubleshooting)
* ModuleNotFoundError: No module named 'cv2'

Causa: El entorno virtual no está activo o instalaste las librerías fuera de él.

Solución: Ejecuta source alpr_env/bin/activate (o su equivalente en Windows) y verifica con which python o where python que estás apuntando a la carpeta del proyecto.

* ImportError: libGL.so.1: cannot open shared object file

Causa: Común en Linux/Raspberry Pi. Faltan los enlaces del sistema para renderizar gráficos con OpenGL.

Solución: Corre sudo apt install -y libgl1.

* La ventana de video se abre pero se queda en negro o congela

Causa: Otro programa está usando la cámara web (Zoom, Teams, FaceTime) o el índice de la cámara en cv2.VideoCapture(0) es incorrecto.

Solución: Cierra aplicaciones que compitan por el periférico o intenta cambiar el índice a 1 o 2 (cv2.VideoCapture(1)).
