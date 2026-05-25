import cv2
from ultralytics import YOLO
import easyocr
import math
import requests 
import threading 

# 1. Cargar Modelos
print("Cargando modelos...")
# Cambia 'yolov8n.pt' por tu 'best.pt' si ya tienes tu modelo entrenado
modelo_yolo = YOLO('yolov8n.pt') 
lector_ocr = easyocr.Reader(['es', 'en'], gpu=False)

# 2. Inicializar la Cámara (¡Esto era lo que faltaba!)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

print("Cámara iniciada. Presiona 'q' para salir.")

# 3. Configuración del Servidor PHP
ENDPOINT_PHP = "https://minimalcodetest.com/yolo/api2.php" 

def enviar_a_servidor(placa_leida):
    """Función que corre en segundo plano para enviar el JSON sin congelar el video"""
    try:
        payload = {"placa": placa_leida}
        
        # Aumentamos el timeout a 5 segundos por si el servidor online es lento
        respuesta = requests.post(ENDPOINT_PHP, json=payload, timeout=5)
        
        # Esto te ayudará a depurar. Imprimirá lo que el servidor responde.
        print(f"[SERVIDOR] Enviada: {placa_leida} | Código HTTP: {respuesta.status_code} | Respuesta: {respuesta.text}")
    except requests.exceptions.Timeout:
        print(f"[ERROR DE RED] El servidor tardó mucho en responder para la placa {placa_leida}")
    except Exception as e:
        print(f"[ERROR DE RED] Fallo al conectar: {e}")
        print(f"[ERROR DE RED] No se pudo conectar al PHP con la placa {placa_leida}")

# Variables para la optimización y memoria espacial
contador_frames = 0
frecuencia_ocr = 60
placa_cache = ""     
centro_anterior = (0, 0)
frames_vistos = 0
ultima_placa_enviada = "" 

# 4. Bucle Principal de Video
while cap.isOpened():
    exito, frame = cap.read()
    if not exito: break

    contador_frames += 1
    
    # Detección con YOLO (Usando 'mps' para aprovechar el chip de la Mac)
    resultados = modelo_yolo(frame, conf=0.5, imgsz=320, device='mps', verbose=False)
    
    # Limpieza si no hay placas en pantalla
    if len(resultados[0].boxes) == 0:
        frames_vistos += 1
        if frames_vistos > 15:
            placa_cache = ""
            ultima_placa_enviada = "" # Reseteamos para el próximo auto
    else:
        frames_vistos = 0

    for resultado in resultados:
        cajas = resultado.boxes
        for caja in cajas:
            x1, y1, x2, y2 = map(int, caja.xyxy[0])
            if x1 < 0 or y1 < 0 or x2 > frame.shape[1] or y2 > frame.shape[0]: continue

            # Lógica espacial (Distancia de la placa)
            cx = int((x1 + x2) / 2)
            cy = int((y1 + y2) / 2)
            distancia = math.hypot(cx - centro_anterior[0], cy - centro_anterior[1])

            if distancia > 150:
                placa_cache = "..."
                contador_frames = frecuencia_ocr # Forzamos lectura inmediata
                centro_anterior = (cx, cy)
                ultima_placa_enviada = "" 

            # Dibujar caja verde
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

            # Lógica de Lectura OCR
            if contador_frames % frecuencia_ocr == 0:
                recorte_placa = frame[y1:y2, x1:x2]
                recorte_gris = cv2.cvtColor(recorte_placa, cv2.COLOR_BGR2GRAY)
                texto_detectado = lector_ocr.readtext(recorte_gris, allowlist='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
                
                if texto_detectado:
                    texto_mas_grande = ""
                    max_altura = 0
                    
                    for resultado_ocr in texto_detectado:
                        caja_ocr = resultado_ocr[0] 
                        texto = resultado_ocr[1]
                        altura_texto = caja_ocr[2][1] - caja_ocr[0][1]
                        texto_limpio = texto.strip('-')
                        
                        # Filtro: Texto más grande y con más de 3 caracteres
                        if altura_texto > max_altura and len(texto_limpio) >= 3:
                            max_altura = altura_texto
                            texto_mas_grande = texto_limpio
                            
                    if texto_mas_grande:
                        placa_cache = texto_mas_grande
                        centro_anterior = (cx, cy)
                        
                        # MULTIHILO: Enviar al PHP si es una placa nueva y válida
                        if placa_cache != ultima_placa_enviada and len(placa_cache) >= 5:
                            ultima_placa_enviada = placa_cache
                            hilo_envio = threading.Thread(target=enviar_a_servidor, args=(placa_cache,))
                            hilo_envio.start()

            # Dibujar el texto leído en pantalla
            if placa_cache != "":
                cv2.rectangle(frame, (x1, y1 - 35), (x2, y1), (0, 0, 0), -1)
                cv2.putText(frame, placa_cache, (x1 + 5, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Mostrar ventana
    cv2.imshow('Sistema ROBUSTO ALPR - MacBook Air', frame)
    
    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'): break

# Limpieza final
cap.release()
cv2.destroyAllWindows()