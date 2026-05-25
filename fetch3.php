<?php
// 1. Decirle al navegador que esto es un JSON puro
header('Content-Type: application/json; charset=utf-8');
// 2. Permitir que se lea desde cualquier lado (CORS)
header('Access-Control-Allow-Origin: *');

// 2. ANTI-CACHÉ: Obligar al navegador y al servidor a NO guardar esta página
header("Cache-Control: no-store, no-cache, must-revalidate, max-age=0");
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache");

try {

    $host = 'localhost';
    $db   = 'minimal1_yoloproject';
    $user = 'minimal1_yolo'; // Cambia esto por tu usuario
    $pass = '99izaNQLbL8XV7B';     // Cambia esto por tu contraseña

    try {
        $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8mb4", $user, $pass);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        // echo "EVERYTHING OK";
    } catch (\PDOException $e) {
        die(json_encode(["error" => "Conexion fallida"]));
        echo "Fallo";
    }
    
    // Obtener las últimas 20 lecturas
    $stmt = $pdo->query("SELECT placa, fecha_hora, es_robo FROM lecturas ORDER BY id DESC LIMIT 20");
    $lecturas = $stmt->fetchAll(PDO::FETCH_ASSOC);

    echo json_encode($lecturas);

} catch (\PDOException $e) {
    // Si la base de datos falla, devuelve un JSON con el error real
    echo json_encode(["error" => "Error de BD: " . $e->getMessage()]);
}
?>