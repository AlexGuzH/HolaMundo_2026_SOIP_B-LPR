<?php
// Configuración de base de datos
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

// 1. Recibir JSON de Python
$json = file_get_contents('php://input');
$data = json_decode($json, true);

if ($data && isset($data['placa'])) {
    // 2. Limpieza y validación (Solo letras y números)
    $placa = strtoupper(preg_replace('/[^A-Z0-9]/', '', $data['placa']));
    
    // 3. Validar patrón (Omitir basura: exigir entre 5 y 9 caracteres)
    if (strlen($placa) >= 5 && strlen($placa) <= 9) {
        
        // 4. ¿Está en el catálogo de robos?
        $stmt_robo = $pdo->prepare("SELECT id FROM catalogo_robos WHERE placa = ?");
        $stmt_robo->execute([$placa]);
        $es_robo = $stmt_robo->fetch() ? 1 : 0;
        
        // 5. Registrar en la tabla de lecturas
        $stmt_insert = $pdo->prepare("INSERT INTO lecturas (placa, es_robo) VALUES (?, ?)");
        $stmt_insert->execute([$placa, $es_robo]);
        
        echo json_encode(["status" => "success", "placa" => $placa, "alerta" => $es_robo]);
    } else {
        echo json_encode(["status" => "ignored", "reason" => "Formato invalido"]);
    }
}
?>