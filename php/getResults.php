<?php
require_once('../php/csvToJSON.php');
$file = "../data/results.csv";
echo csvToJSON($file);
