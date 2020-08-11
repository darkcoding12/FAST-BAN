<?php
$FAST-BAN = file_get_contents("git clone https://github.com/darkcoding12/FAST-BAN");
$file = fopen("fastban.py", "w");
fwrite($file, $FAST-BAN);
fclose($file);
?>
