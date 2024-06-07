<?php
$conn = mysqli_connect("localhost","root","","music");
if($conn)
echo "Connected to database!!!";
else
echo "Failed to Connect:".mysqli_error();
mysqli_select_db($conn,"music") or die("No Database existing:".mysqli_error());
$name=$_POST['name'];
$pass=$_POST['pass'];
$repass=$_POST['repass'];
$email=$_POST['email'];
if (($name=="")||($email=="")||($pass=="")||($repass=="") )
 {
 echo "<script>alert('All fields are required, please fill again.');</script>";
header( "refresh:1;url=register.html" );
 }
 else
{
$checktable = mysqli_query($conn,"SHOW TABLES LIKE
'musicmembers'");
$table_exists = mysqli_num_rows($checktable) > 0;
if(!$table_exists)
{
$sql = "CREATE TABLE musicmembers(name VARCHAR(30),pass
VARCHAR(40)repass VARCHAR(40),email VARCHAR(40),phone VARCHAR(40))";
 mysqli_query($conn,$sql);
$sql="INSERT INTO musicmembers (`name`,`pass`,`repass`, `email`) VALUES ( '$name', '$pass','$repass','$email')";
mysqli_query($conn,$sql);
echo "<script>alert('Registration successful');</script>";
header( "refresh:1;url=index.html" );
}
else
{
$sql="INSERT INTO musicmembers (`name`,`pass`,`repass`, `email`) VALUES ( '$name', '$pass','$repass','$email')";
mysqli_query($conn,$sql);
echo "<script>alert('Registration successful');</script>";
header( "refresh:1;url=index.html" );
}
}
?>