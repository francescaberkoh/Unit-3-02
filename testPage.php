
<?php
/*Created on Mar 7, 2019
Created for: ICS3U
@author: Francesca Berkoh
This program is the guessing game
*/

$number= $_POST['number_entered'];
$submitbutton= $_POST['submit'];
$randomnumber= mt_rand(1,10);




/*Create the widgets*/
?>

<form action="" method="POST">
Guess a integer between 1 and 10: 
<input type="text" name="number_entered" value=''/> <br><br>
Result: 


<?php 
/*When the button is clicked the user will recieve feedback*/
if ($submitbutton){

if ($number != $randomnumber)
{
echo "Incorrect guess. The correct number was $randomnumber. Maybe next time..";
}
else 
{
echo "$randomnumber is the correct guess. You got it right.";
}
}

?>


<br><br>
<input type="submit" name="submit" value="Search"/><br><br>
</form>
