<?php

$conn = mysqli_connect('127.0.0.1', 'root', '', 'fypdb') or die(mysqli_connect_error());
$sql = "SELECT password, email FROM relatives";

$rs = mysqli_query($conn, $sql);

$checkLogin = false;

while ($rc = mysqli_fetch_assoc($rs)) {
    extract($rc);

    if (($email == $_POST['email']) and ($password == $_POST['password'])) {
        $checkLogin = true;
        echo "true";
        setcookie('userEmail', $email, time() + 60 * 60);
        setcookie('loginStatus', 0, time() + 60 * 60);
		mysqli_close($conn);
        break;
    }
}

if (!$checkLogin){
    echo "false";
}
?>
