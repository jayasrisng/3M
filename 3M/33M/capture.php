<html>
<style>
body{
	background-image: url("background.jfif");
}
</style>
<body >
<?php
$command=escapeshellcmd('python emotions.py');
$output=shell_exec($command);
echo "<p><font color=white>$output</font></p>";

/*
$command=escapeshellcmd("python project_code.py $mood");
$str=shell_exec($command);

$res = str_replace(array( '[','"',"'",']' ), '', $str);
$arr=(explode(",",$res));

$arr1=array(
    array($arr[0],$arr[1],$arr[2],$arr[3]),
    array($arr[4],$arr[5],$arr[6],$arr[7]),
    array($arr[8],$arr[9],$arr[10],$arr[11]),
    array($arr[12],$arr[13],$arr[14],$arr[15]),
    array($arr[16],$arr[17],$arr[18],$arr[19])
    );
for ($i=0;$i<=4;$i++){
	$name=$arr1[$i][0];
	$year=$arr1[$i][1];
	$artists=$arr1[$i][2];
	$link=$arr1[$i][3];
	echo "<h4><font color=white >$name</font></h4>";
	echo "<h4><font color=white >$year</font></h4>";
	echo "<h4><font color=white >$artists</font></h4>";
	echo "<a href=$link>click</a>";
	echo "<br>";
}
*/

echo "<p><font color=white >Image captured</font></p>";
?>
</body>
</html>

