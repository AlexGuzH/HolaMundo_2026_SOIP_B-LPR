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
