<html>
<style>
body{
	background-image: url("background.jfif");
}
</style>
<body >
<?php
$conn = mysqli_connect("localhost","root","","music");
mysqli_select_db($conn,"music") or die("No Database existing:".mysql_error());
$name=$_REQUEST['name'];
$pass=$_REQUEST['pass'];
$sql="SELECT name FROM musicmembers WHERE name='$name' and
pass='$pass'";
$result=mysqli_query($conn,$sql);
$count=mysqli_num_rows($result);
if ($count==1)
{
echo "<p> <font color=white font face='verdana'>Welcome <b>".$name.",</b></font></p>";
echo "<p><font color=white font face='verdana'> Do you want to play based on your mood?</font></p>";
echo "<form action='capture.php'>
<button> Capture</button></form>";
echo "<p><font color=white font face='verdana'>Note:Press (space) to capture and (q) to exit</font></p>";
 echo "<br><form action='index.html'><input type='submit'
value='Logout'/></form>";
}
else{
 echo "<script> alert('invalid details!');</script>";
 header( "refresh:1;url=index.html" );
 }

?>
</body>
</html>