<!DOCTYPE html>
<html lang="en">

<head>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
  <link href="../style/common.css" rel="stylesheet">

  <link href="../style/login.css" rel="stylesheet">
  <link href="../style/fallRecord.css" rel="stylesheet">

  <title>Index</title>
</head>

<body>
  <div class="header_bar">
    <div class="icon">
      <a href="elderInfo.php">
        <img id="logo" src="../img/logo.png" alt="Avatar">
      </a>
    </div>
    <div class="cta_list">
      <div class="">
        <button class="btn_all btn_register" onclick="logout()">Logout</button>
        <script>
          function logout() {
            window.location.href = 'logout.php';
          }

        </script>
      </div>
    </div>
  </div>
  <div style="margin-top: 64px;"></div>

  <ul class="ht_slideshow" style="z-index: -100;">
    <li><span></span></li>
    <li><span></span></li>
    <li><span></span></li>
    <li><span></span></li>
    <li><span></span></li>
    <li><span></span></li>
  </ul>


  <main>




    <div class="control_products">

      <div>&nbsp;</div>

      <?php
				extract($_GET);
//				var_dump($_GET);
				$conn = mysqli_connect('127.0.0.1', 'root', '', 'fypdb') or die(mysqli_connect_error());
				$sql = "SELECT MAX(`fall_record_id`) as `fall_max_id` FROM `fall_record`";
				$rs = mysqli_query($conn, $sql);
				$rc = mysqli_fetch_assoc($rs);
				extract($rc);
				$fall_id = $fall_max_id;
				$sql = "SELECT DISTINCT elderly.name, fall_record.fall_date ,fall_record.fall_gif FROM `fall_record`, elderly WHERE `fall_record_id` = '$fall_id' and fall_record.elderly_id = elderly.id";
				$rs = mysqli_query($conn, $sql);
				$rc = mysqli_fetch_assoc($rs);
				extract($rc);
				echo("<h3>Name: $name</h3>");
				echo("<h5>Fall Time: $fall_date</h5>");
				mysqli_close($conn);
			?>


      <div class="promote">
        <br>
        <div class="control_subProducts">
          <div class="sub_promote">
            <input type="button" class="btn_gif btn_all " value="Call Hospital" onclick="callHospital()">
          </div>
          <div class="sub_promote">
            <input type="button" class="btn_gif btn_all " value="Cancel" onclick="cancel()">
          </div>


        </div>
        <script>
          function callHospital() {
            alert("System has called the Hospital.");
            window.location.href = 'elderInfo.php';
          }

          function cancel() {
            alert("Alert canceled.");
            window.location.href = 'elderInfo.php';
          }

          function fallLive() {
            window.location.href = 'http://10.106.128.13:9000/video_feed';
          }
        </script>
        <br>
        <!--								<img class="fallGif" src="../gif_data/test.gif" alt="">-->
        <img class="fallGif" src="<?php echo"../gif_data/$fall_gif";?>" alt="">
        <div>&nbsp;</div>
        <div class="sub_promote">
          <input type="button" class="btn_gif btn_all " value="Live" onclick="fallLive()">
        </div>
      </div>

      <div>&nbsp;</div>

    </div>

    <div>&nbsp;</div>
    <div>&nbsp;</div>
    <div>&nbsp;</div>
    <div>&nbsp;</div>
    <div>&nbsp;</div>
    <div>&nbsp;</div>
    <div>&nbsp;</div>
  </main>

  <footer class="page-footer">
    <div class="container">
      <div class="row">
        <div class="col-12 col-lg-7">
          <h5 class="white-text">About Us</h5>
          <p class="grey-text text-lighten-4">You can use rows and columns here to organize your footer content.</p>
        </div>
        <div class="col-12 col-lg-5">
          <h5 class="white-text">Contact Us</h5>
          <input id="h_destination" type="email" class="ht_input" placeholder="Username" />
          <textarea class="ht_input mb-4" rows="4" placeholder="Your message"></textarea>
          <a href="#!" class="btn btn-outline-ht float-right mb-4">Send</a>
        </div>
      </div>
    </div>
    <div class="footer-copyright">
      <div class="container">
        &copy; 2020, Fall Detection
        <a class="float-right" href="#!">Terms &amp; Condition</a>
      </div>
    </div>
  </footer>
</body>

</html>
