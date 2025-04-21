// Solution for isPalindrome in php: integers case
<?php

function isPalindrome($x){
    $x = (string) $x;
    $left = 0;
    $right = strlen($x) - 1;

    while ($left <= $right) {
        if($x[$left] != $x[$right]) return false;
        $left++;
        $right--;
    }
    return true;
}

echo isPalindrome(121) ."\n";
echo isPalindrome(10);