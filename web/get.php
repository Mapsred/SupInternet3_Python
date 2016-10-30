<?php
if (isset($_POST['crit_value'])) {
    $url = "127.0.0.1:5000/user/".$_POST['crit_value'];
    $url = str_replace(' ', '%20', $url);
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $data = curl_exec($ch);
    curl_close($ch);
    $parsed_json = json_decode($data);


    $fullname=$parsed_json->result->firstname . " ".$parsed_json->result->lastname;

    ?>

    <!doctype html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>API GET Result</title>
    </head>
    <body>
        id: <?= $parsed_json->result->id ?> <br>
        nom entier: <?= $fullname ?> <br>
        entreprise: <?= $parsed_json->result->enterprise ?> <br>
        statut: <?= $parsed_json->result->state ?>
    </body>
    </html>

<?php

}