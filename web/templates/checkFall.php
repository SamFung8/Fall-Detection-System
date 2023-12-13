<?php
	extract($_POST);
//	var_dump($_POST);
//echo "$time";
	$conn = mysqli_connect('127.0.0.1', 'root', '', 'fypdb') or die(mysqli_connect_error());
	$sql = "SELECT * FROM `fall_record` WHERE `fall_date` = '$time'";
	$rs = mysqli_query($conn, $sql);
	$num = mysqli_num_rows($rs);
	$checkFall = false;

	if ($num == 1){
		$checkFall = true;
		echo "true";
		mysqli_close($conn);
	}

	if (!$checkFall){
		echo "false";
	}
?>