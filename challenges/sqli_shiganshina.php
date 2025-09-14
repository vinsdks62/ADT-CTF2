<?php
$flag = "ESD{RECON_SHIGANSHINA}";

// Liste étendue d'utilisateurs
$users = [
    ['id'=>1,'name'=>'Eren'],
    ['id'=>2,'name'=>'Mikasa'],
    ['id'=>3,'name'=>'Armin'],
    ['id'=>4,'name'=>'Levi'],
    ['id'=>5,'name'=>'Hange'],
    ['id'=>6,'name'=>'Erwin'],
    ['id'=>7,'name'=>'Jean'],
    ['id'=>8,'name'=>'Connie'],
    ['id'=>9,'name'=>'Sasha'],
    ['id'=>10,'name'=>'Historia']
];

$message = "";

if(isset($_POST['id'])){
    $input = $_POST['id'];

    // Vérification plus subtile pour simuler SQLi
    if(strpos($input, "OR") !== false && strpos($input, ">") !== false){
        $message = "✅ Flag trouvé : $flag";
    } else {
        $message = "Utilisateur : ";
        foreach($users as $user){
            if($user['id'] == $input) $message .= $user['name'];
        }
    }
}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Shiganshina - SQL Injection</title>
    <style>
        body { font-family: Arial; background-color: #1c1c1c; color: #f2f2f2; text-align: center; }
        h1 { color: #e63946; }
        input, button { padding: 8px; margin: 5px; }
        .description { margin-bottom: 20px; }
    </style>
</head>
<body>
    <h1>Shiganshina - SQL Injection</h1>
    <p class="description">
        Vous infiltrez Shiganshina et tentez de récupérer les informations sur tous les soldats.<br>
        Seule une requête subtile vous permettra de découvrir le flag.
    </p>

    <form method="POST">
        ID du soldat: <input type="text" name="id">
        <button type="submit">Soumettre</button>
    </form>

    <p><?php echo $message; ?></p>
</body>
</html>
