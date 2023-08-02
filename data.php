 
<?php
 
   include('logo.php'); 
$tok1 = '",';
$tok2 = 'image:"';
$newStringx = $tok2.$newString.$tok1; 


$descr1 = '
     "stretching": "exactfit",
     "width": "100%", 
      aspectratio: "16:9",
  abouttext: "Join Us On Telegram",
  aboutlink: "https://t.me/TheTechieSiaOfficial",';
   
     $descr2 = '     description: "Join @TheTechieSiaOfficial",
            "logo":    {
        "file": "https://i.imgur.com/LU9XEm8.png",
        "margin": "30", 
        "link": "https://t.me/TheTechieSiaOfficial",
    },'; 

$descr = $descr1.$newStringx.$descr2;
 

    ?>