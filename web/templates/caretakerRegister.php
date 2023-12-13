<?php
  extract($_POST);
//  var_dump($_POST);

  $conn = mysqli_connect('127.0.0.1', 'root', '', 'fypdb') or die(mysqli_connect_error());
  $sql = "SELECT * FROM `caretaker` WHERE `email` = '$email' ";
  $rs = mysqli_query($conn, $sql);
  $num = mysqli_num_rows($rs);

  if ($num != 0) {
    echo '<script language="javascript">';
    echo 'alert("This email has been used.")';
    echo '</script>';
    mysqli_close($conn);
    header("Refresh:0.1; url=register.php");
  } else {
    $sql = "INSERT INTO `caretaker` VALUES ('$email', '$name', '$phone', '$hkid', '$password', '$socialWorkerID', '$gender', NULL)";
    mysqli_query($conn, $sql) or print(mysqli_error($conn));
    $num = mysqli_affected_rows($conn);
    mysqli_close($conn);
    echo '<script language="javascript">';
    echo 'alert("Sign Up Successful!")';
    echo '</script>';
    header("Refresh:0.1; url=index.php");
  }
?>