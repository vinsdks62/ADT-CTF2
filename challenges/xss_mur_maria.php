<?php
$flag = "ESD{MUR_MARIA}";
$comment = "";
$message = "";

if(isset($_POST['comment'])){
    $comment = $_POST['comment'];

    // Détection d'une vraie injection XSS
    if(strpos($comment, "<script>") !== false || strpos($comment, "onerror=") !== false){
        $message = "✅ Flag trouvé : $flag";
    } else {
        $message = "Commentaire reçu : $comment";
    }
}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Mur Maria - XSS</title>
    <style>
        body { font-family: Arial; background-color: #1c1c1c; color: #f2f2f2; text-align: center; }
        h1 { color: #457b9d; }
        input, button { padding: 8px; margin: 5px; }
        .description { margin-bottom: 20px; }
    </style>
</head>
<body>
    <h1>Mur Maria - Cross-Site Scripting</h1>
    <p class="description">
        Vous commentez sur le Mur Maria.<br>
        Seule une injection subtile (JavaScript ou image malicieuse) vous permettra de récupérer le flag.
    </p>

    <form method="POST">
        Commentaire: <input type="text" name="comment">
        <button type="submit">Soumettre</button>
    </form>

    <p><?php echo $message; ?></p>
</body>
</html>
