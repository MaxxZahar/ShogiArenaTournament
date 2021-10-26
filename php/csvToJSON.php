<?php
function csvToJSON($fname)
{
    if (!($fp = fopen($fname, 'r'))) {
        die('Can not open the file');
    }
    $key = fgetcsv($fp, '1024', ';');
    $json = array();
    while ($row = fgetcsv($fp, "1024", ";")) {
        $json[] = array_combine($key, $row);
    }
    fclose($fp);
    return json_encode($json, JSON_UNESCAPED_UNICODE);
}
