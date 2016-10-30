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

    var_dump($parsed_json);
}