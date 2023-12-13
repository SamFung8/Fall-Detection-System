<!DOCTYPE html>
<html lang="en">

<head>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
	<script src="/js/jquery-3.5.1.js"></script>
	<link rel="stylesheet" href="/css/agentIndex.css">
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
	<link href="../style/common.css" rel="stylesheet">

	<link href="../style/login.css" rel="stylesheet">

	<title>Index</title>
</head>

<body>
	<div class="header_bar">
		<div class="icon">
			<a href="index.php">
				<img id="logo" src="../img/logo.png" alt="Avatar">
			</a>
		</div>
		<div class="cta_list">
			<div class="btn_login">
				<button class="btn_all" onclick="openNav()">Login</button>
			</div>
			<div class="">
				<button class="btn_all btn_register" onclick="goToRegister()">Create an account</button>
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

	<script>
		function goToRegister() {
			window.location.href = 'register.php';
		}

	</script>


	<main>

		<div id="mySidenav" class="sidenav">

			<a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>

			<div class="login_control">

				<div class="login_type">
				
				</div>
				<div style="margin-top: 20px;"></div>


				


				<div id="login_Caretaker">
				
					<div class="imgcontainer">
						<img id="caretaker_img" src="../img/login.png" alt="Avatar" class="avatar">
						<p></p>
						<p>Caretaker</p>
					</div>
					<div class="container">

						<label for="email">
							<b>Email</b>
						</label>
						<input type="email" name="email" id="email_C" placeholder="Enter Email" required>

						<br>

						<label for="psw">
							<b>Password</b>
						</label>
						<input type="password" name="psw" id="password_C" placeholder="Enter Password" required>

						<br>
						<br>

						<button class="btn_submit" type="button" onclick="checkCaretakerLogin()"><b>Login</b></button>

						<div>&nbsp;</div>
						<div>&nbsp;</div>
						<div>&nbsp;</div>
						<div>&nbsp;</div>
						<div>&nbsp;</div>
						<div>&nbsp;</div>
						<div>&nbsp;</div>
					</div>
				</div>


			</div>
		</div>

		<script>
			//Show and Hide the login form

			function openNav() {
				document.getElementById("mySidenav").style.width = "100%";
			}

			function closeNav() {
				document.getElementById("mySidenav").style.width = "0";
			}


		</script>

		<script>
			//check user login

			function checkRelativesLogin() {
				var password = document.getElementById('password_R').value;
				var email = document.getElementById('email_R').value;
				$.ajax({
					url: "checkRelativesLogin.php",
					method: "POST",
					data: {
						password: password,
						email: email
					},
					success: function(data) {
						console.log(data);
						if (data == "true") {
							alert("Login success!");
							window.location.href = 'elderInfo.php';
						} else {
							alert("Sorry, wrong password or email!");
						}
					}
				});
			}

			function checkCaretakerLogin() {
				var password = document.getElementById('password_C').value;
				var email = document.getElementById('email_C').value;
				$.ajax({
					url: "checkCaretakerLogin.php",
					method: "POST",
					data: {
						password: password,
						email: email
					},
					success: function(data) {
						console.log(data);
						if (data == "true") {
							alert("Login success!");
							window.location.href = 'elderInfo.php';
						} else {
							alert("Sorry, wrong password or email!");
						}
					}
				});
			}

		</script>


		<div class="control_products">
			<div>&nbsp;</div>
			<h1 style="text-align: center;">Fall Detect</h1>
			<hr>
			<div class="promote" style="border: 0px solid #ddd;">
				
				<div class="control_subProducts">
					<div class="sub_promote" style="border: 0px solid #ddd;">

					</div>
					<img class="photo" src="../img/02.jpg" alt="" style="width:30%;">
					<div class="sub_promote" style="border: 0px solid #ddd;">

					</div>
				</div>
				<div class="control_subProducts">

					<img class="photo" src="../img/01.jpg" alt="" style="width:30%;">

					<div class="sub_promote" style="border: 0px solid #ddd;">
						<p style="font-size: 20px; text-align: center;">
							<br>
							<br>
							When we start to walk as babies, falling over is a natural part of the learning process. But as we age, falling becomes more serious – and for some, it can be fatal. Our system will constantly scan by the camera and detect the people's skeleton and use those data to analyze the people do they fall. Then, the system will send an alert from this website.
						</p>
					</div>
				</div>
			</div>

			<div>&nbsp;</div>

		</div>


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
