<?php
/**
 * Created by IntelliJ IDEA.
 * User: maps_red
 * Date: 30/10/16
 * Time: 20:34
 */

if (isset($_POST['fullname'])) {
    $url = "127.0.0.1:5000/user";
    $fields_string = "";
    $fields = [
        'fullname' => urlencode($_POST['fullname']),
        'enterprise' => urlencode($_POST['enterprise']),
    ];

    foreach ($fields as $key => $value) {
        $fields_string .= $key.'='.$value.'&';
    }

    rtrim($fields_string, '&');

    $url = str_replace(' ', '%20', $url);
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_POST, count($fields));
    curl_setopt($ch, CURLOPT_POSTFIELDS, $fields_string);
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
        <title>API POST Result</title>
    </head>
    <body>
    <?= $parsed_json->result ?>
    </body>
    </html>

    <?php

}