<?php

$datos = file("day1.txt");
$t=0;

for($i = 0; $i < count($datos); $i++){
    for($j = $i+1; $j < count($datos); $j++){
        for($k = $j+1; $k < count($datos); $k++){
            $a = substr($datos[$i],0,-1);
            $b = substr($datos[$j],0,-1);
            $c = substr($datos[$k],0,-1);
            #echo "$a + $b + $c\n";

            if($a + $b + $c == 2020){
                #echo "$a + $b + $c\n";
                #echo $a + $b + $c . "\n";
                echo $a * $b * $c . "\n";
                break(3);
            }
            $t++;
        }
    }
}

echo $t;
?>

