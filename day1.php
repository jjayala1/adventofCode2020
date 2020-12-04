<?php

$datos = file("day1.txt");
$t = 0;

for($i = 0; $i < count($datos); $i++){
    for($j = $i+1; $j < count($datos); $j++){
            $a = substr($datos[$i],0,-1);
            $b = substr($datos[$j],0,-1);

            if($a + $b == 2020){
                echo $a * $b . "\n";
                break(2);
            }
            $t++;
    }
}
echo $t;

?>

