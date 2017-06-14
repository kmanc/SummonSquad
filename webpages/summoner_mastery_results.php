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
		<h4>

			<?php

				//make sure input to python script is formatted correctly

				for ($i = 1; $i <= 5; $i += 1) {
					$sani[$i] = str_replace(' ','',$_POST["sum{$i}"]);
				}

				$path = '/var/www/html/Main.py';
				$python = '/usr/bin/python3.4';
				$script = $python . " " . $path . " -s " . $sani[1] . " " . $sani[2] . " " . $sani[3] . " " . $sani[4] . " " . $sani[5] . " -r " . $_POST["region"] . " -c " . $_POST["champnum"];
				$command = escapeshellcmd($script);
				$results = exec($command, $my_output, $status);
				$data_array = explode(",", $results);

				//make sure dictionaries havent messed up order of summoner names (hint: they have)

				$n = 1;
				for ($i = 0; $i <= 12; $i += 3) {
					$summonerName[$n] = str_replace(array('"', ' '), '' , $data_array[$i]);
					$n++;
				}

				//get the properly formatted bgs for the champions

				$j = 1;
				for ($i = 1; $i <= 13; $i += 3) {
					$champ[$j] = str_replace(array('"', ' ', '.', "'"), '' , $data_array[$i]);
					$j++;
				}
				//temp fix to get rid of double quotes around KogMaw's name (rito pls)
				
				for ($i = 1; $i <= 5; $i += 1) {
					$pattern = "/\"/"; 
					$replace = ""; 
					$fix_quote[$i] = preg_replace($pattern,$replace,$champ[$i]);
				}
				//standardize role names, e.g. DUO_CARRY turns to Carry, JUNGLE turns to Jungle
				$m = 1;
				for ($i = 2; $i <=14; $i += 3){
					$role[$m] = ucfirst(strtolower(preg_replace('/DUO_/', '', $data_array[$i])));
					$m++;
				}
				?>
			 </h4>
			<h2 class="error"><?php 
				if ($status != 0) {
					echo 'command run: ' . $command;
					echo '<br>';
					echo 'Status error:' . $status . '. Something went wrong.<br> Make sure all of your summoner names are spelled correctly.<br> Press the back button or click <a href="../index.html"><button class="buttonAdd">   Here   </button></a> to go back';
				}
				?>
			</h2>
			<div class="summoners">
				<div class="player1">
					<p class="p1">
						<?php echo strip_tags($summonerName[1]); ?>
					</p>
				</div><div class="player2">
					<p class="p2">
						<?php echo strip_tags($summonerName[2]); ?>
					</p>
				</div><div class="player3">
					<p class="p3">
						<?php echo strip_tags($summonerName[3]); ?>
					</p>
				</div><div class="player4">
					<p class="p4">
						<?php echo strip_tags($summonerName[4]); ?>
					</p>
				</div><div class="player5">
					<p class="p5">
						<?php echo strip_tags($summonerName[5]); ?>
					</p>
				</div>
			</div>
				<div class="readText">
					<div id="summ1">
							<?php
								echo '<p class="bot_text">';
								echo $summonerName[1];
								echo '<br>' . $fix_quote[1];
								echo '<br>' . $role[1];
								echo '</p>';
							?>
					</div><div id="summ2">
							<?php
								echo '<p class="bot_text">';
								echo $summonerName[2];
								echo '<br>' . $fix_quote[2];
								echo '<br>' . $role[2];
								echo '</p>';
							?>
					</div><div id="summ3">
							<?php
								echo '<p class="bot_text">';
								echo $summonerName[3];
								echo '<br>' . $fix_quote[3];
								echo '<br>' . $role[3];
								echo '</p>';
							?>
					</div><div id="summ4">
							<?php
								echo '<p class="bot_text">';
								echo $summonerName[4];
								echo '<br>' . $fix_quote[4];
								echo '<br>' . $role[4];
								echo '</p>';
							?>
					</div><div id="summ5">
							<?php
								echo '<p class="bot_text">';
								echo $summonerName[5];
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
	    $('div#summ1').mouseenter(function(){
	   		$('p.p1').css({
	   			'color' : 'rgba(230,230,230,1)',
				'transition-duration': '.4s', 
		    });
		    $('div.player1').css({
		    	'background-color' : 'rgba(0,0,0,.4)',
		    })
		}); 
	    $('div#summ1').mouseleave(function(){
	    	$('p.p1').css({
	    		'color' : 'rgba(0,0,0,0)',
				'transition-duration': '.4s', 
			});
		    $('div.player1').css({
		    	'background-color' : 'rgba(0,0,0,0)',
		    })
	    });
	    $('div#summ2').mouseenter(function(){
	   		$('p.p2').css({
	   			'color' : 'rgba(230,230,230,1)',
				'transition-duration': '.4s', 
		    });
		    $('div.player2').css({
		    	'background-color' : 'rgba(0,0,0,.4)',
		    })
		}); 
	    $('div#summ2').mouseleave(function(){
	    	$('p.p2').css({
	    		'color' : 'rgba(0,0,0,0)',
				'transition-duration': '.4s', 
			});
		    $('div.player2').css({
		    	'background-color' : 'rgba(0,0,0,0)',
		    })
	    });
	    $('div#summ3').mouseenter(function(){
	   		$('p.p3').css({
	   			'color' : 'rgba(230,230,230,1)',
				'transition-duration': '.4s', 
		    });
		    $('div.player3').css({
		    	'background-color' : 'rgba(0,0,0,.4)',
		    })
		}); 
	    $('div#summ3').mouseleave(function(){
	    	$('p.p3').css({
	    		'color' : 'rgba(0,0,0,0)',
				'transition-duration': '.4s', 
			});
		    $('div.player3').css({
		    	'background-color' : 'rgba(0,0,0,0)',
		    })
	    });
	    $('div#summ4').mouseenter(function(){
	   		$('p.p4').css({
	   			'color' : 'rgba(230,230,230,1)',
				'transition-duration': '.4s', 
		    });
		    $('div.player4').css({
		    	'background-color' : 'rgba(0,0,0,.4)',
		    })
		}); 
	    $('div#summ4').mouseleave(function(){
	    	$('p.p4').css({
	    		'color' : 'rgba(0,0,0,0)',
				'transition-duration': '.4s', 
			});
		    $('div.player4').css({
		    	'background-color' : 'rgba(0,0,0,0)',
		    })
	    });
	    $('div#summ5').mouseenter(function(){
	   		$('p.p5').css({
	   			'color' : 'rgba(230,230,230,1)',
				'transition-duration': '.4s', 
		    });
		    $('div.player5').css({
		    	'background-color' : 'rgba(0,0,0,.4)',
		    })
		}); 
	    $('div#summ5').mouseleave(function(){
	    	$('p.p5').css({
	    		'color' : 'rgba(0,0,0,0)',
				'transition-duration': '.4s',  
			});
		    $('div.player5').css({
		    	'background-color' : 'rgba(0,0,0,0)',
		    })
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