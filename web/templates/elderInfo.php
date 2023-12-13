<?php
?>
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
	<link rel="stylesheet" href="../style/agentIndex.css">
	<link href="../style/login.css" rel="stylesheet">

	<title>Elder Information</title>
</head>

<body>

	<script>
		setInterval(function() {

			var date = new Date();

			var time = date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate() + ' ' + (date.getHours() < 10 ? "0" : "") + date.getHours() + ":" + (date.getMinutes() < 10 ? "0" : "") + (date.getMinutes() - 1) + ":" + (date.getSeconds() < 10 ? "0" : "") + date.getSeconds();

			//			alert('time: ' + time);

			checkFall(time);

		}, 1000);

		function checkFall(time) {
			$.ajax({
				url: "checkFall.php",
				method: "POST",
				data: {
					time: time
				},
				success: function(data) {
					console.log(data);
					if (data == "true") {
						//						alert('test_true');
						alert("Emergence! \nElderly falling detected! \nPlease press OK to check the details.");
						window.location.href = 'fallRecord.php?fall_time=' + time;
					}
				}
			});
		}

	</script>


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
		<div class="ht_banner">
			<div class="container">
				<div class="container-main">
					<!-- Trigger/Open The Modal -->
					<button class="bn btn-outline-success margin" id="btn-plus"><span class="fa fa-plus"></span></button>

					<div id="modal-plus" class="modal-plus">
						<!-- Modal content -->
						<div class="modal-content">
							<span class="close">&times;</span>
							<h2>Add New Elderly</h2>
							<form action="../templates/elderadd.php" method="post">
								<fieldset>
									<legend>Elderly Information:</legend>
									<div class="row">
										<div class="col">Name: <input type="text" name="name" class="form-control"></div>
										<div class="col">HKID: <input type="text" name="hkid" class="form-control"></div>
									</div>
									<div class="row">
										<div class="col">Address: <input type="text" name="address" class="form-control"></div>
										<div class="col">Phone Number: <input type="number" name="phone" class="form-control"></div>
									</div>
									<br>
									<div class="col">Gender: <input type="radio" id="M" name="sex" value="M">Male
										<input type="radio" id="F" name="sex" value="F">Female</div>
								</fieldset>
								<br>
								<button type="submit" class="btn btn-primary" id="add">Submit</button>
								<button type="reset" class="btn btn-primary">Reset</button>
							</form>
						</div>
					</div>

					<div id="modal-edit" class="modal-edit">
						<!-- Modal content -->
						<div class="modal-content">
							<span class="close1">&times;</span>
							<h2>Edit Elderly</h2>
							<form action="" method="get">
								<fieldset>
									<legend>Elderly Information:</legend>
									<div class="row">
										<div class="col">Name: <input type="text" id="name" class="form-control" placeholder="Chan Tai Man"></div>
										<div class="col">HKID: <input type="text" id="hkid" class="form-control" placeholder="A1234567"></div>
									</div>
									<div class="row">
										<div class="col">Phone Number: <input type="number" id="phone" class="form-control" placeholder="12345678"></div>
										<div class="col">Address: <input type="textarea" id="address" class="form-control" placeholder="Flat Abc, Abc Building , Abc Street, Hong Kong"></div>
									</div>
									<br>
									<div class="col">Gender: <input type="radio" id="M">Male
										<input type="radio" id="F" checked>Female</div>
								</fieldset>
								<br>
								<button type="button" class="btn btn-primary" id="add" data-dismiss="modal">Submit</button>
								<button type="reset" class="btn btn-primary">Reset</button>
							</form>
						</div>
					</div>

					<?php
        $conn = mysqli_connect('127.0.0.1', 'root', '', 'fypdb') or die(mysqli_connect_error());
        $sql = "SELECT * FROM elderly";

        $rs = mysqli_query($conn, $sql);
        while ($rc = mysqli_fetch_assoc($rs)) {
//          var_dump($rc);
          extract($rc);
          
          if ($gender == "M") {
            $display = 'Male';
            $picture = 'elder02';
          } else {
              $display = 'Female';
              $picture = 'elder01';
          }
          
          echo"
              <div class='card'>
            <div class='card-horizontal'>
              <div class='img-square-wrapper'>
                <a href=''><img class='img-house' src='../img/$picture.jpg' alt='' width='350px' height'200'></a>
              </div>
              <div class='card-body'>
                <button class='bn btn-outline-success margin float-right'><span class='fa fa-remove'></span></button>
                <button class='bn btn-outline-success margin float-right' id='btn-edit'><span class='fa fa-edit'></span></button>
                <br>
                <p>Name: $name</p>
                <p>HKID: $hkid</p>
                <p>Address: $address</p>
                <p>Phone Number: $phoneNumber</p>
                <p>Gender: $display</p>
              </div>
            </div>
          </div>
          ";
        }
        ?>

					<!--
					<div class="card">
						<div class="card-horizontal">
							<div class="img-square-wrapper">
								<a href=""><img class="img-house" src="../img/elder01.jpg" alt=""></a>
							</div>
							<div class="card-body">
								<button class="bn btn-outline-success margin float-right"><span class="fa fa-remove"></span></button>
								<button class="bn btn-outline-success margin float-right" id="btn-edit"><span class="fa fa-edit"></span></button>
								<br>
								<p>Name: Chan Tai Man</p>
								<p>HKID: A1234567</p>
								<p>Address: Flat Abc, Abc Building , Abc Street, Hong Kong</p>
								<p>Phone Number: 12345678</p>
								<p>Gender: Female</p>
							</div>
						</div>
					</div>
					<div class="card">
						<div class="card-horizontal">
							<div class="img-square-wrapper">
								<a href=""><img class="img-house" src="../img/elder01.jpg" alt=""></a>
							</div>
							<div class="card-body">
								<button class="bn btn-outline-success margin float-right"><span class="fa fa-remove"></span></button>
								<button class="bn btn-outline-success margin float-right"><span class="fa fa-edit"></span></button>
								<br>
								<p>Name: Chan Tai Man</p>
								<p>HKID: A1234567</p>
								<p>Address: Flat Abc, Abc Building , Abc Street, Hong Kong</p>
								<p>Phone Number: 12345678</p>
								<p>Gender: Female</p>
							</div>
						</div>
					</div>
-->
				</div>
			</div>
		</div>
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

	<script>
		// Get the modal
		var modal_plus = document.getElementById("modal-plus");
		var modal_edit = document.getElementById("modal-edit");
		// Get the button that opens the modal
		var btn_plus = document.getElementById("btn-plus");
		var btn_edit = document.getElementById("btn-edit");
		// Get the <span> element that closes the modal
		var span = document.getElementsByClassName("close")[0];
		var span1 = document.getElementsByClassName("close1")[0];
		var span2 = document.getElementsByClassName("close2")[0];
		var span3 = document.getElementsByClassName("closed")[0];


		// When the user clicks the button, open the modal 
		btn_plus.onclick = function() {
			modal_plus.style.display = "block";
		}
		btn_edit.onclick = function() {
			modal_edit.style.display = "block";
		}

		// When the user clicks on <span> (x), close the modal
		span.onclick = function() {
			modal_plus.style.display = "none";
		}
		span1.onclick = function() {
			modal_edit.style.display = "none";
		}
		// When the user clicks anywhere outside of the modal, close it
		window.onclick = function(event) {
			if (event.target == modal_plus && modal_edit) {
				modal_plus.style.display = "none";
				modal_edit.style.display = "none";
			}
		}
		$(document).ready(function() {
			$('#add').click(function() {
				$('#new-property ').css("display", "block");
				modal_plus.style.display = "none";
			});
			$('#edit').click(function() {
				$('#price1').html("$40M");
				modal_edit.style.display = "none";
			});
		});

	</script>
</body>

</html>
