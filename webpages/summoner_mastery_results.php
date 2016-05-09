<html>
<head>
  <meta charset="utf-8">
  <link href='https://fonts.googleapis.com/css?family=Gentium+Basic:400,700italic' rel='stylesheet' type='text/css'>
  <link href='riot.css' rel='stylesheet' type='text/css'>
  <title>SummonSquad</title>
	<script src="../scripts/jquery.js"></script>
</head>
<body>
		<h1>SummonSquad</h1>
		<h4><?php

				//make sure input to python script is formatted correctly

				for ($i = 1; $i <= 5; $i += 1) {
					$sani[$i] = str_replace(' ','',$_POST["sum$i"]);
				}


				$path = '/var/www/html/Main.py';
				$python = '/usr/bin/python3.4';
				$script = $python . " " . $path . " " . $sani[1] . " " . $sani[2] . " " . $sani[3] . " " . $sani[4] . " " . $sani[5] . " " . $_POST["region"] . " " . $_POST["champnum"];
				$command = escapeshellcmd($script);
				$results = exec($command, $my_output, $status);
				$data_array = explode(",", $results);

				//get the properly formatted bgs for the champions

				$j = 1;
				for ($i = 1; $i <= 13; $i += 3) {
					$champ[$j] = str_replace(array('"', ' '), '' , $data_array[$i]);
					$j++;
				}

				//temp fix to get rid of double quotes around KogMaw's name (rito pls)
				
				$k = 1;
				for ($i = 1; $i <= 13; $i += 3) {
					$pattern = "/\"/"; 
					$replace = ""; 
					$fix_quote[$k] = preg_replace($pattern,$replace,$data_array[$i]);
					$k++;
				}

				//standardize role names, e.g. DUO_CARRY turns to Carry, JUNGLE turns to Jungle

				$m = 1;
				for ($i = 2; $i <=14; $i += 3){
					$role[$m] = ucfirst(strtolower(preg_replace('/DUO_/', '', $data_array[$i])));
					$m++;
				}

				?>
			 </h4>
			<div class="summoners">
				<h2 class="error"><?php 
					if ($status != 0) {
						echo 'Status error:' . $status . '. Something went wrong.<br> Make sure all of your summoner names are spelled correctly.<br> Press the back button or click <a href="../index.html"><button class="buttonAdd">   Here   </button></a> to go back';
					}
					?>
				</h2>
				<div class="readText">
					<div id="summ1">
							<?php
								echo '<p class="bot_text">';
								echo $_POST['sum1'];
								echo '<br>' . $fix_quote[1];
								echo '<br>' . $role[1];
								echo '</p>';
							?>
					</div><div id="summ2">
							<?php
								echo '<p class="bot_text">';
								echo $_POST['sum2'];
								echo '<br>' . $fix_quote[2];
								echo '<br>' . $role[2];
								echo '</p>';
							?>
					</div><div id="summ3">
							<?php
								echo '<p class="bot_text">';
								echo $_POST['sum3'];
								echo '<br>' . $fix_quote[3];
								echo '<br>' . $role[3];
								echo '</p>';
							?>
					</div><div id="summ4">
							<?php
								echo '<p class="bot_text">';
								echo $_POST['sum4'];
								echo '<br>' . $fix_quote[4];
								echo '<br>' . $role[4];
								echo '</p>';
							?>
					</div><div id="summ5">
							<?php
								echo '<p class="bot_text">';
								echo $_POST['sum5'];
								echo '<br>' . $fix_quote[5];
								echo '<br>' . $role[5];
								echo '</p>';
							?>
					</div>
				</div>
			</div>
<script>

	//jquery for changing the background on hover for champions
	$(document).ready(function(){
	    $('div#summ1').hover(function(){
	   		$('html').css({
				'background' : 'url(../bg/<?php echo $champ[1]; ?>.jpg) no-repeat center center fixed',
				'background-position' : '50% 10%',
				'-webkit-background-size' : 'cover',
				'-moz-background-size' : 'cover',
				'-o-background-size' : 'cover',
				'background-size' : 'cover',
				'transition-duration': '.3s' 
		    });
		}); 

	    $('div#summ2').hover(function(){
	   		$('html').css({
				'background' : 'url(../bg/<?php echo $champ[2]; ?>.jpg) no-repeat center center fixed',
				'background-position' : '50% 10%',
				'-webkit-background-size' : 'cover',
				'-moz-background-size' : 'cover',
				'-o-background-size' : 'cover',
				'background-size' : 'cover',
				'transition-duration': '.3s' 
		    });
		}); 
	    $('div#summ3').hover(function(){
	   		$('html').css({
				'background' : 'url(../bg/<?php echo $champ[3]; ?>.jpg) no-repeat center center fixed',
				'background-position' : '50% 10%',
				'-webkit-background-size' : 'cover',
				'-moz-background-size' : 'cover',
				'-o-background-size' : 'cover',
				'background-size' : 'cover',
				'transition-duration': '.3s' 
		    });
		}); 
	    $('div#summ4').hover(function(){
	   		$('html').css({
				'background' : 'url(../bg/<?php echo $champ[4]; ?>.jpg) no-repeat center center fixed',
				'background-position' : '50% 10%',
				'-webkit-background-size' : 'cover',
				'-moz-background-size' : 'cover',
				'-o-background-size' : 'cover',
				'background-size' : 'cover',
				'transition-duration': '.3s' 
		    });
		}); 
	    $('div#summ5').hover(function(){
	   		$('html').css({
				'background' : 'url(../bg/<?php echo $champ[5]; ?>.jpg) no-repeat center center fixed',
				'background-position' : '50% 10%',
				'-webkit-background-size' : 'cover',
				'-moz-background-size' : 'cover',
				'-o-background-size' : 'cover',
				'background-size' : 'cover',
				'transition-duration': '.3s' 
		    });
		}); 
	});
	$(window).load(function(){
   		$('html').css({
			'background' : 'url(../bg/<?php echo $champ[1]; ?>.jpg) no-repeat center center fixed',
			'background-position' : '50% 10%',
			'-webkit-background-size' : 'cover',
			'-moz-background-size' : 'cover',
			'-o-background-size' : 'cover',
			'background-size' : 'cover',
			'transition-duration': '.3s' 
	    });
	}); 

</script>
</body>
</html>