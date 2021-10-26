<?php
require_once('../php/csvToJSON.php');
$file = "../data/players.csv";
echo csvToJSON($file);
