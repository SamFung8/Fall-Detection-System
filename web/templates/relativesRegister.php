<?php
  extract($_POST);
//  var_dump($_POST);

  $conn = mysqli_connect('127.0.0.1', 'root', '', 'fypdb') or die(mysqli_connect_error());
  $sql = "SELECT * FROM `relatives` WHERE `email` = '$email' ";
  $rs = mysqli_query($conn, $sql);
  $num = mysqli_num_rows($rs);

  if ($num != 0) {
    echo '<script language="javascript">';
    echo 'alert("This email has been used.")';
    echo '</script>';
    mysqli_close($conn);
    header("Refresh:0.1; url=register.php");
  } else {
    $sql = "INSERT INTO `relatives` VALUES ('$email', '$name', '$phone', '$gender', '$hkid', '$password', NULL)";
    mysqli_query($conn, $sql) or print(mysqli_error($conn));
    $num = mysqli_affected_rows($conn);
    mysqli_close($conn);
    echo '<script language="javascript">';
    echo 'alert("Sign Up Successful!")';
    echo '</script>';
    header("Refresh:0.1; url=index.php");
  }
?>

<!--error-->
<?php
//	extract($_POST);
//
//	$conn = mysqli_connect('127.0.0.1', 'root', '', 'fypdb') or die(mysqli_connect_error());
//	$sql = "SELECT * FROM `relatives` WHERE `email` = '$email' ";
//
//	$rs = mysqli_query($conn, $sql);
//	$num = mysqli_num_rows($rs);
//
//	$checkemail = false;
//
//	if ($num == 0) {
//		$checkemail = true;
//		echo "true";
//		$sql = "INSERT INTO `relatives` VALUES ('$email', '$name', '$phone', '$gender', '$hkid', '$password', NULL)";
//    	mysqli_query($conn, $sql) or print(mysqli_error($conn));
//    	mysqli_close($conn);
//	} else {
//		echo "false";
//	}
?>
