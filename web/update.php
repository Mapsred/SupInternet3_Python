<?php
/**
 * Created by IntelliJ IDEA.
 * User: maps_red
 * Date: 30/10/16
 * Time: 23:13
 */

if (isset($_POST['index'])) {
    $parameters = ['fullname' => $_POST['fullname']];
    if (isset($_POST['index']) && !empty($_POST['index'])) {
        $parameters['index'] = ($_POST['index']);
        $parameters['value'] = ($_POST['value']);
    } else {
        $parameters['index'] = "state";
        $parameters['value'] = ($_POST['state']);

    }
    $url = "127.0.0.1:5000/user/".$_POST['fullname'];

    var_dump($parameters);
    $url = str_replace(' ', '%20', $url);
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "PUT");
    curl_setopt($ch, CURLOPT_HEADER, false);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($parameters));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $data = curl_exec($ch);
    curl_close($ch);
    $parsed_json = json_decode($data);
?>

    <!doctype html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>API PUT Result</title>
    </head>
    <body>
    <?= $parsed_json->result ?>
    </body>
    </html>

    <?php
}