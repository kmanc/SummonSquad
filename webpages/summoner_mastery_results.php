<html>
<head>
  <meta charset="utf-8">
  <link href='https://fonts.googleapis.com/css?family=Gentium+Basic:400,700italic' rel='stylesheet' type='text/css'>
  <link href='riot.css' rel='stylesheet' type='text/css'>
  <title>DreamTeam.gg</title>
	<script src="../scripts/jquery.js"></script>
	<script src="../scripts/summoner_stuff.js"></script>
</head>
<body style="background-color: black;">
	<div class="body_wrapper">
		<h1>DreamTeam.gg</h1>
			<div class="summoners">
				<div id="summ1">
					<span style="position: absolute; bottom: 0;">
						<?php
						echo $_POST['sum1'];
						echo '<br>Top';
						?>
					</span>
				</div><div id="summ2">
					<span style="position: absolute; bottom: 0;">
						<?php
						echo $_POST['sum2'];
						echo '<br>Mid';
						?>
					</span>
				</div><div id="summ3">
					<span style="position: absolute; bottom: 0;">
						<?php
						echo $_POST['sum3'];
						echo '<br>Jungle';
						?>
					</span>
				</div><div id="summ4">
					<span style="position: absolute; bottom: 0;">
						<?php
						echo $_POST['sum4'];
						echo '<br>Support';
						?>
					</span>
				</div><div id="summ5">
					<span style="position: absolute; bottom: 0;">
						<?php
						echo $_POST['sum5'];
						echo '<br>ADC';
						?>
					</span>
				</div>
			</div>
	</div>
</body>
</html>