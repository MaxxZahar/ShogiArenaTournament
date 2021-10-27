<?php
if (isset($_POST['createfile'])) {
    $table = $_POST['table'];
    $header = '[' . $_POST['header'] . "]";
    $path = $_POST['filename'] . '.txt';
    $table = $header . "\r\n" . $table;
    $file = fopen("../temp/table.txt", 'w+');
    flock($file, LOCK_EX);
    fwrite($file, $table);
    flock($file, LOCK_UN);
    rewind($file);
    header("Content-Disposition: attachment; filename=\"" . basename($path) . "\"");
    header("Content-type: text/html; charset=utf-8");
    fpassthru($file);
    unlink("../temp/table.txt");
    exit();
}
